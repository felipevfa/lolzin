# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from lolzin.lollib import api


class lolzinUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	points = models.IntegerField(default=0)
	league = models.CharField(max_length=10, default='unranked')
	numQuestions = models.IntegerField(default=0)
	cQuestions = models.IntegerField(default=0)
	photo = models.FileField(upload_to='lolzin/avatars', default=0)
	winrate = models.FloatField(default=50)
	

	

	def make_league(self):
		if(self.numQuestions<10):
			return 'unranked'

		pontuacao = self.points
		if pontuacao < api.pontos_de_liga[0] :
			return 'Bronze 5'
		if pontuacao >= pontos_de_liga[6] :
			return 'Faker'
		if pontuacao >= pontos_de_liga[5]:
			return 'Mestre'
		x = 0
		while(pontuacao > pontos_de_liga[x+1]):
			x += 1

		liga = ligas[x]
		resto = pontuacao - pontos_de_liga[x]
		intervalo = pontos_de_liga[x+1] - pontos_de_liga[x]
		intervalo /= 5
		resto  = int(resto/intervalo)
		print resto,intervalo,pontos_de_liga[x],pontos_de_liga[x+1],pontuacao- pontos_de_liga[x]
		return liga + ' '+ str(5-resto)


	def update_user(self,resposta):
		self.numQuestions += 1
		total = self.numQuestions
		if(resposta):
			self.cQuestions += 1
		acertos =  self.cQuestions
		winrate = 	float(acertos)/total
		if(resposta):
			pts = 10**((winrate+1)**2)
		else:
			pts = -self.points*0.075
		winrate = int(100*winrate)/100.0
		if(total<10):
			if(pts>0):
				pts = pts**((total*5+50)/100.0)+acertos
			else:
				pts = -((-pts)**((total*5+50)/100.0))
		self.points += pts
		self.winrate = winrate
		self.league = self.make_league()
		self.save()
		return int(pts)


