

from rest_framework import serializers
from .models import (
    Panier, Produit, Categorie_Produit, Commande, Commande_Produit

)

class SerialierPanier(serializers.ModelSerializer) :
    class Meta :
        model  = Panier
        fields = ["user","status_panier", "total_montant_panier"]

