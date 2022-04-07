from django.contrib import admin
from django.urls import path,include, re_path
from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^sign-up$', views.signup),
    url(r'^ajax-sign-up$', views.ajaxsignup),
    url(r'^ajax-login$', views.ajaxlogin),
    url(r'^logout$', views.logout),
    url(r'^ajax-save-photo',views.ajaxsavephoto),   
    url(r'^ajax-photo-feed',views.ajaxphotofeed),
    url(r'^(?P<username>[a-zA-Z0-9_]+)$', views.profile),
    url(r'^ajax-profile-feed', views.ajaxprofilefeed),
    url(r'^ajax-set-profile-pic$', views.ajaxsetprofilepic),
    url(r'^ajax-like-photo$',views.ajaxlikephoto),
    url(r'^ajax-follow$',views.ajaxfollow),
]