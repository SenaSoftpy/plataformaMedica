from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name="inicio"),
    path('login/', views.login_pagina, name="login"),
    path('registro/', views.registro_pagina, name="registro"),
]
