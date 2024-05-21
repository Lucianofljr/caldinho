from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contato, name="contato"),
    path("produto/", views.produto, name="produto"),
    path("cardapio/", views.cardapio, name="cardapio"),
    path("config/", views.config, name="config"),
]