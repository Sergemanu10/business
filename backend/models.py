from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=True, blank=True)


class Article(models.Model):
    nom = models.CharField(max_length=50, unique=True, null=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantite = models.IntegerField(null=False)


class Vente(models.Model):
    quantite = models.IntegerField(null=False)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)


class Client(models.Model):
    nom = models.CharField(max_length=100, unique=True, null=False)
    prenoms = models.CharField(max_length=100, unique=True, null=False)
    contact = models.CharField(max_length=20, null=False)
    email = models.EmailField()