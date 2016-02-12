from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
		url(r'^', include('lolzin.urls')),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

