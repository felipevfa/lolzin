# coding: utf-8
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class lolzinUserManager(BaseUserManager):
	def create_user(self, username, email, password, photo):
		if not username:
			raise ValueError("Defina um nome de usuário.")

		if not email:
			raise ValueError("Forneça um e-mail válido.")

		if not password or len(password) < 6:
			raise ValueError("Por favor, insira uma senha entre 6 e 16 caracteres.")

		if not photo:
			user = self.model(nick=username,
						  	  identifier=self.normalize_email(email), 
						 	 )
		else:
			user = self.model(nick=username,
							  identifier=self.normalize_email(email),
							  photo=photo
							 )

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password, photo):
		if not username:
			raise ValueError("Defina um nome de usuário.")

		if not email:
			raise ValueError("Forneça um e-mail válido.")

		if not password or len(password) < 6:
			raise ValueError("Por favor, insira uma senha entre 6 e 16 caracteres.")

		if not photo:
			user = self.model(identifier=username,
						  	  email=self.normalize_email(email), 
						 	 )
		else:
			user = self.model(identifier=username,
							  email=self.normalize_email(email),
							  photo=photo
							 )

		user.is_admin = True
		user.set_password(password)
		user.save(using=self._db)
		return user

class lolzinUser(AbstractBaseUser):
	identifier = models.EmailField(max_length=120, unique=True)
	nick = models.CharField(max_length=20, unique=True)
	points = models.IntegerField(default=0)
	rank_position = models.CharField(max_length=10, null=True)
	league = models.CharField(max_length=10, default='unranked')
	numQuestions = models.IntegerField(default=0)
	cQuestions = models.IntegerField(default=0)
	photo = models.FileField(upload_to='lolzin/avatars', default=0)
	winrate = models.FloatField(default=50)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'nick'
	REQUIRED_FIELDS = ['identifier']

	objects = lolzinUserManager()

	def get_full_name(self):
		return self.nick

	def get_short_name(self):
		return self.nick

	def __str__(self):
		return self.nick


# class User(models.Model):
# 	nick = models.CharField(max_length=20, unique=True)
# 	password = models.CharField(max_length=16)
# 	points = models.IntegerField(default=0)
# 	rank_position = models.CharField(max_length=10, null=True)
# 	league = models.CharField(max_length=10, default='Bronze V') 
# 	totalQuestoes = models.IntegerField(default=0)
# 	qtdAcertos = models.IntegerField(default=0)
# 	photo = models.FileField(upload_to='avatars',default=0)
	
# 	def __str__(self):
# 		return self.nick
# 		
		