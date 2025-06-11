from django.urls import path

from backend.views import index, article, categorie, client, vente

urlpatterns = [
    path('', index, name= "index"),
    path('categorie/', categorie, name= "categorie"),
    path('article/', article, name= "article"),
    path('client/', client, name= "client"),
    path('vente/', vente, name= "vente"),
]
