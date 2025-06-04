from django.contrib import admin
from .models import *



class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "description")
admin.site.register(Categorie, CategorieAdmin)



class ArticlePage(admin.ModelAdmin):
    list_display = ("nom", "prix", "quantite")
admin.site.register(Article, ArticlePage)


class VentePage(admin.ModelAdmin):
    list_display = ("quantite", "prix_total")
admin.site.register(Vente, VentePage)


class ClientPage(admin.ModelAdmin):
    list_display = ("nom", "prenoms", "contact", "email")
admin.site.register(Client, ClientPage)