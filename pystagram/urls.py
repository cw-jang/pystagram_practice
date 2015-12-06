from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.views import login 
from django.contrib.auth.views import logout


# from photos.urls import urlpatterns as phtos_url

urlpatterns = [

	url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name':'login.html'}, name='login_url'), 
    url(r'^logout/$', logout, {'next_page':'/login/'}, name='logout_url'),
    
]
