from models import lolzinUser

class CustomBackend(object):
	def authenticate(self, nick=None, password=None):
		try:
			user = lolzinUser.objects.get(nick=nick, password=password)
		except lolzinUser.DoesNotExist:
			return None
		return user

	def get_user(self, email):
		try:
			return lolzinUser.objects.get(identifier=email)
		except lolzinUser.DoesNotExist:
			return None

	def get_user_by_nick(self, nick):
		try:
			return lolzinUser.objects.get(nick=nick)
		except lolzinUser.DoesNotExist:
			return None


