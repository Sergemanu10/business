from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'article.html')


def categorie(request):
    return render(request, 'categorie.html')

def client(request):
    return render(request, 'client.html')

def vente(request):
    return render(request, 'vente.html')