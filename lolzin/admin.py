#coding: utf-8
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import lolzinUser

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

	class Meta:
		model = lolzinUser
		fields = ('identifier', 'nick', 'photo')
		labels = { 'identifier': 'E-mail', 'nick': 'Nome de Usuário', 'photo': 'Avatar' }

	def check_password(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("As senhas devem ser iguais.")
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()

		return user

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = lolzinUser
		fields = ('identifier', 'nick', 'password', 'photo', 'points', 'rank_position', 'league',
				  'numQuestions', 'cQuestions', 'is_admin', 'is_active', 'is_superuser',
				  )

	def clean_password(self):
		return self.initial["password"]

class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('identifier', 'points', 'league', 'rank_position', 'numQuestions', 'cQuestions', 'is_admin',)
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('identifier', 'password',)}),
		('Dados de Usuário', {'fields': ('points', 'league', 'rank_position', 'numQuestions', 'cQuestions',)}),
		('Permissões', {'fields': ('is_admin',)}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('identifier', 'email', 'photo', 'password1', 'password2')
			}),
		)
	search_fields = ('email', 'identifier')
	ordering = ('identifier',)
	filter_horizontal = ()

admin.site.register(lolzinUser, UserAdmin)
admin.site.unregister(Group)