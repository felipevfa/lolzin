from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'signup', views.signup, name='signup'),
    url(r'feedback', views.feedback, name='feedback'),
    url(r'login', views.login, name='login'),
    url(r'user_cp', views.user_cp, name='user_cp'),
    url(r'logout', views.logout, name='logout'),
    url(r'ranking', views.ranking, name='ranking'),
    url(r'gogoapi',views.view_api, name='gogoapi'),
    url(r'profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'game', views.game, name='game')
]