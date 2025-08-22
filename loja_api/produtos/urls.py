from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name="lista_produtos"),  # raiz já abre lista com pesquisa
    path('home/', views.home, name="home"),                 # home fica em /home/
    path('carrinho/', views.carrinho, name="carrinho"),
    path('cartao/', views.cartao, name="cartao"),
    path('contato/', views.contato, name="contato"),
]
