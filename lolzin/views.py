# coding: utf-8
import json
from random import choice
import urllib2
from django import forms
from lolzin.models import lolzinUser,User
from lolzin.forms import UserSignupForm,UserAuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.db import IntegrityError
from django.db.models import Q
from lollib import loltermos, rids
from django.http import JsonResponse
from django.core.urlresolvers import reverse
import logging
from lolzin.lollib import win_gif,fail_gif
from lolzin.lollib import api,profile_background

logger = logging.getLogger(__name__)


def index(request):
	logger.debug('index')

	form = UserAuthenticationForm()
	top = lolzinUser.objects.all().order_by('-points').exclude(numQuestions=0)[0:10]
	

	context = {
		'form': form,
		'top_ten': top,
	}	

	return render(request, 'lolzin/index.html', context);

def game(request):
	logger.debug('basic')
	
	if(request.method != 'POST'):
		# Se o vetor de campeões estiver vazio, solicita o vetor.
		random = api.random_item()
		item = api.random_item()	
		question = api.random_item_question(item)
		ct = {
			'background' : api.random_champion_background(),
			'item_name' : item['name']  
		}
		ct.update(item)
		ct.update(question)
		return render(request,'lolzin/game.html', ct)
	else:
		pts = 0.0
		if not request.POST.has_key('choice'):
			return HttpResponse('vc precisa escolher uma opcao fion')
		else:
			if (request.POST['choice'] == '1'):
				resposta = 1
			else:
				resposta = 0
			
			if request.user.is_authenticated():
				pts = request.user.lolzinuser.update_user(resposta)
			else:
				pts = 0

			win_img = choice(win_gif)
			fail_img =  choice(fail_gif)

			if (pts < 0):
				pts = abs(pts)

			contexto = { 'resposta': resposta,
				'win_img': win_img,
				'fail_img': fail_img,
				'pontos': pts }
			request.session['temp_data'] = contexto

			return HttpResponseRedirect(reverse("feedback"))

def feedback(request):
	contexto = { 'resposta': request.session['temp_data']['resposta'],
				 'win': request.session['temp_data']['win_img'],
				 'fail': request.session['temp_data']['fail_img'],
				 'pts': request.session['temp_data']['pontos']
	}

	return render(request, 'lolzin/feedback.html', contexto)

#print data

#############################
#		  USUÁRIO			#
#############################


# Formulário de cadastro.

def signup(request):
	logger.debug('signup')
	error_msg = ''

	if request.method == 'POST':
		form = UserSignupForm(request.POST, request.FILES)

		if form.is_valid():
				form.save()

				new_user = authenticate(username=request.POST['username'], 
										password=request.POST['password1'])
				
				auth_login(request, new_user)

				return HttpResponseRedirect(reverse('profile',args=[new_user.username]))

	else:
		form = UserSignupForm()

	return render(request, 'lolzin/signup.html', {'form': form })	
	

def login(request):
	form = UserAuthenticationForm()
	logger.debug('login')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print username
		print password
		user = authenticate(username=username, password=password)
		print user
		print user
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				return HttpResponseRedirect(reverse('profile', kwargs={'username': user.username}))
			else:
				return HttpResponse('mamao')
				return render(request, 'lolzin/login.html', { 'login_msg': 'Conta desativada.', 'form': form })
		else:
			return HttpResponse('melao')
			return render(request, 'lolzin/login.html', { 'login_msg': 'Combinação de usuário e senha incorreta.', 'form': form })
	else:
		return render(request, 'lolzin/login.html', { 'form': form })


def logout(request):
	logger.debug('logout')
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))

def profile(request,username):
	user = User.objects.get(username=username)
	liga_str = user.lolzinuser.league.split()[0]
	if liga_str == 'unranked':
		liga_img_index = 0
	else:
		liga_img_index = lollib.ligas.index(liga_str)+1
	contexto = {
		'profile_user' : user,
		'imgsrc_liga' : 'lolzin/img/rank'+str(liga_img_index)+'.png',
		'background' : profile_background[liga_str]
	}
	return render(request,'lolzin/profile.html', contexto)

def user_cp(request):
	logger.debug('user_cp')

	if request.user.is_authenticated():
		return render(request, 'lolzin/user_cp.html')
	else:
		form = UserAuthenticationForm()
		return render(request, 'lolzin/login.html', { 'login_msg': 'Você precisa estar logado para acessar essa página.', 
												 'form': form })

def ranking(request):
	logger.debug('ranking')
	users = lolzinUser.objects.all().order_by('-points').exclude(numQuestions=0)
	p = Paginator(users, 15)

	page = request.GET.get('page')

	try:
		rank_page = p.page(page)
	except PageNotAnInteger:
		rank_page = p.page(1)
	except EmptyPage:
		rank_page = p.page(p.num_pages)

	context = {
		'ranking': p,
		'rank_page': rank_page
	}

	return render(request, 'lolzin/ranking.html', context)

