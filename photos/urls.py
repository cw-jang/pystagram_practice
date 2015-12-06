# photos/urls.py
from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', views.view_photo, name='view_photo'),
	url(r'^create/$', views.create_photo, name='create_photo'),
]