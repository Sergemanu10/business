from datetime import datetime
from django.shortcuts import render
from .models import Partenaire

# Create your views here.

def index(request):
    return render(request, 'index.html', context = {"date": datetime.today()})


def article(request):
    return render(request, 'article.html')


def categorie(request):
    return render(request, 'categorie.html')

def client(request):
    return render(request, 'client.html')

def vente(request):
    return render(request, 'vente.html')


def footer(request):
    partenaires = Partenaire.objects.all()[:5] # Les 5 premiers partenaires
    context = {
        'partenaire': partenaires,
        'nom_site': 'business'
    }
    return render(request, 'footer.html', context)

def contact(request):
    return (request, 'contact.html')
