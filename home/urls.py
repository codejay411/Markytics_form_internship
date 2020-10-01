from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('userpage/', views.userpage, name='userpage')
]


