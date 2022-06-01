from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.welcome,name='welcome'),
    path('accounts/profile/', views.dashboard,name='dashboard'),
]
