#coding: utf-8
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from lolzin.models import lolzinUser
from admin import UserCreationForm


class UserSignupForm(UserCreationForm):
	photo = forms.FileField(label="Avatar", required=False)

	class Meta:
		model = lolzinUser
		fields = ("nick", "identifier", "password1", "password2",)
		labels = { 'identifier': 'E-mail', 
				   'nick': 'Nome de Usuário'
				 }

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.nick = self.cleaned_data["nick"]
		user.photo = self.cleaned_data["photo"]
		
		#if self.photo:
		#	user.photo = self.cleaned_data["photo"]

		if commit:
			user.save()

		return user

	def check_values(self):
		nick = self.cleaned_data["nick"]
		email = self.cleaned_data["identifier"]
		errors = { 'user_error': False,
		           'email_error': False 
		         }

		try:
			if (lolzinUser.objects.get(nick=nick)):
				errors['user_error'] = True
		except lolzinUser.DoesNotExist:
			errors['user_error'] = False

		try:
			if (lolzinUser.objects.get(identifier=email)):
				errors['email_error'] = True
		except lolzinUser.DoesNotExist:
			errors['email_error'] = False

		return errors;

class UserAuthenticationForm(AuthenticationForm):
	username = forms.CharField(label='Nome de Usuário', max_length=20)
	password = forms.CharField(label='Senha', widget=forms.PasswordInput)

	class Meta:
		model = lolzinUser
		fields = ('nick', 'password')
		labels = { 'username': 'Nome de Usuário', 'password': 'Senha' }

	

