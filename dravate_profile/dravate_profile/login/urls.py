from django.conf.urls import include, url
from django.contrib.auth import views  as login_views
from login.views import  profile_form, profile
from . import views 

urlpatterns = [ 
    url(r'^password/change/$', login_views.password_change, { 'template_name': 'password_change_form.html'}, name='password_change'),
    url(r'^password/change/done/$', login_views.password_change_done, {'template_name': 'password_change_done.html'}, name='password_change_done'),
    url(r'^profile$', profile,),
    url(r'^profile/$', profile,),
    url(r'^profile/edit$', profile_form,),
]

