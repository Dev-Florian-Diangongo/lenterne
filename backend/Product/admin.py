from django.contrib import admin
from .models import (
    Panier, Categorie_Produit, Produit, Commande, Commande_Produit
)

class AdminPanier(admin.ModelAdmin) :
    list_display = [
        "user","date_created","status_panier","total_montant_panier"
    ]
class AdminCategorieProduit(admin.ModelAdmin) :
    list_display = [
        "name"
    ]
class AdminProduit(admin.ModelAdmin) :
    list_display =  [
        "name",
        "categorie",
        "price",
        "stock",
        "image",
        "date_ajout",
        "date_expiration"
    ]
class AdminCommande(admin.ModelAdmin) :
    list_display = [
        "user",
        "date_commanded",
        "montant_total_commande",
        "status",
        "adresse_livraison",
        "mode_paiement",
        "date_expedition",
        "date_livraison"
    ]
class AdminCommandeProduit(admin.ModelAdmin) :
    list_display = [
        "commande",
        "produit",
        "quantity",
        "price_au_moment",
        "total_article"
    ]
admin.site.register(Panier, AdminPanier)
admin.site.register(Categorie_Produit, AdminCategorieProduit)
admin.site.register(Produit, AdminProduit)
admin.site.register(Commande, AdminCommande)
admin.site.register(Commande_Produit, AdminCommandeProduit)