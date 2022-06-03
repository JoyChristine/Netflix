from . import views
from django.contrib import admin
from django.urls import re_path as url
from django.conf.urls import include

urlpatterns = [
    # url(r'^$', views.welcome,name='welcome'),
    url(r'^',views.movies,name='movies'),
]
    
