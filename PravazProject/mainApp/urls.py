from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login_pagina),
]