from django.contrib import admin
from django.urls import path
from storeapp import views

urlpatterns = [
    
    path('', views.index ,name='index'),
    path('home/', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', views.login_view,name='login'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('starter/', views.starter),
    
]
