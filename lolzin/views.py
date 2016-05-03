# coding: utf-8
import random
import json
import urllib2
from django import forms
from lolzin.models import lolzinUser
from lolzin.forms import UserSignupForm, UserAuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.db import IntegrityError
from django.db.models import Q
from lollib import loltermos, rids, random_question_item, update_user,solicitar_campeoes
from django.http import JsonResponse
from django.core.urlresolvers import reverse
import logging
import lollib
logger = logging.getLogger(__name__)


win_gif = lollib.win_gif 

fail_gif = lollib.fail_gif 

## Campeões
CHAMPIONS = []

def view_api(request):
	logger.debug('view_api')
	logger.debug('view_api')
	data = {
		'mamao' : 'melao',
		'limao' : 'aviao'
	}
	return JsonResponse(data)

	

def basic(request):
	logger.debug('basic')
	global CHAMPIONS
	
	if(request.method != 'POST'):
		# Se o vetor de campeões estiver vazio, solicita o vetor.
		if not CHAMPIONS:
			CHAMPIONS = solicitar_campeoes()
		
		item_correto, opts, atributo,item_dict = random_question_item()

		champ_name = str(random.choice(list(CHAMPIONS['data'])))
		lista_skin = CHAMPIONS['data'][champ_name]['skins']
		skin_number = str(random.choice(lista_skin)['num'])
		background_link = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + champ_name + "_" + skin_number + ".jpg"
		item_img_link = "http://ddragon.leagueoflegends.com/cdn/5.23.1/img/item/"+str(item_dict["id"])+".png"
		imgsrc_liga = None
		if request.user.is_authenticated():
			liga_str = request.user.league.split()[0]
			if liga_str == 'unranked':
				liga_img_index = 0
			else:
				liga_img_index = lollib.ligas.index(liga_str)+1
				imgsrc_liga = 'lolzin/img/rank'+str(liga_img_index)+'.png'
			
		contexto  = {
			'item_name':item_dict['name'],
			'stats' : item_dict["stats"],
			'item_id':item_dict["id"],
			'item_correto' :  opts[item_correto],
			'opts' : opts,
			'atributo' : loltermos[atributo],
			'imgsrc' : item_img_link,
			'background' : background_link,
			'imgsrcliga' : imgsrc_liga,
		}
		logger.debug(background_link)
		return render(request,'lolzin/basic.html', contexto)
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
				request.user, pts = update_user(request.user,resposta)
				request.user.save()
			else:
				pts = 0

			win_img ,fail_img = random.choice(win_gif),random.choice(fail_gif)

			if (pts < 0):
				pts = abs(pts)

			contexto = { 'resposta': resposta, 'win_img': win_img, 'fail_img': fail_img, 'pontos': pts }
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
		has_db_errors = False

		if form.is_valid():
			errors = form.check_values()

			if errors['user_error']:
				error_msg = error_msg + 'Usuário já cadastrado.<br>'
				has_db_errors = True

			if errors['email_error']:
				error_msg = error_msg + 'E-mail já cadastrado.<br>'
				has_db_errors = True

			if has_db_errors:
				return render(request, 'lolzin/signup.html', { 'form': form, 'signup_msg': error_msg })
			else:
				user = form.save()
				user.save()

				new_user = authenticate(username=request.POST['nick'], 
										password=request.POST['password1'])
				auth_login(request, new_user)

				return HttpResponseRedirect('/lolzin/user_cp.html')
	else:
		form = UserSignupForm()

	return render(request, 'lolzin/signup.html', {'form': form })	
	

def login(request):
	form = UserAuthenticationForm()
	logger.debug('login')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect('lolzin/user_cp.html')

				login(request, user)
				return HttpResponseRedirect('lolzin/user_cp.html')
			else:
				return render(request, 'lolzin/login.html', { 'login_msg': 'Conta desativada.', 'form': form })
		else:
			return render(request, 'lolzin/login.html', { 'login_msg': 'Combinação de usuário e senha incorreta.', 'form': form })
	else:
		return render(request, 'lolzin/login.html', { 'form': form })


def logout(request):
	logger.debug('logout')
	auth_logout(request)
	return HttpResponseRedirect(reverse('basic'))

def profile(request,username):
	user = lolzinUser.objects.get(nick=username)
	liga_str = user.league.split()[0]
	if liga_str == 'unranked':
		liga_img_index = 0
	else:
		liga_img_index = lollib.ligas.index(liga_str)+1
	contexto = {
		'profile_user' : user,
		'imgsrc_liga' : 'lolzin/img/rank'+str(liga_img_index)+'.png',
		'background' : lollib.profile_background[liga_str]
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
	return render(request, 'lolzin/ranking.html', { 'users': users })

