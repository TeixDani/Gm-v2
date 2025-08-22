
from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def home(request):
    return render(request, "home.html")

def carrinho(request):
    return render(request, "carrinho.html")

def cartao(request):
    return render(request, "cartao.html")

def contato(request):
    return render(request, "contato.html")

