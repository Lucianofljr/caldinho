from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def config(request):
    return render(request, 'config.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request):
    return render(request, 'produto.html')

def cardapio(request):
    return render(request, 'cardapio.html')
