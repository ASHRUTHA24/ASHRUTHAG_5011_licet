from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs,name='songs'),
    path('songs/<int:id>', views.songpost,name='songpost'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('watchlater', views.watchlater,name='watchlater'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact')
]
