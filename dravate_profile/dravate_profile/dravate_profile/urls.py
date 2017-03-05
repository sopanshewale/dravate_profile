from django.contrib import admin
from django.contrib.auth import views  as login_views
from django.conf.urls import include, url
from . views import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^accounts/', include('login.urls')),
    url(r'^login$', login_views.login, name='login', ),
    url(r'^logout$', login_views.logout, {'next_page': '/login'}),

]
