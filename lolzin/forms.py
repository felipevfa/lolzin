#coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from lolzin.models import lolzinUser


class UserSignupForm(UserCreationForm):
	photo = forms.FileField(label="Avatar", required=False)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self):
		user = User.objects.create_user(self.cleaned_data['username'],	
			email = self.cleaned_data['email'],
			password = self.cleaned_data['password1'],)
		
		
		lu = lolzinUser()
		lu.photo = self.cleaned_data["photo"]
		lu.user = user
		lu.save()
		
		return lolzinUser

class UserAuthenticationForm(AuthenticationForm):
	
	class Meta:
		model = User
		fields = ('username', 'password')
		# labels = { 'username': 'Username'), 'password': _('Password') }

