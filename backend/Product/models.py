
from django.db import models 
from User.models import User
class Panier(models.Model) :
    STATUS_PANIER = [
        ("cours","En cours"),
        ("abandonne", "abandonné")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status_panier = models.CharField(max_length=20, choices=STATUS_PANIER)
    total_montant_panier = models.DecimalField(decimal_places=2, max_digits=12)
    
    def __str__(self):
        return f"{self.user} ({self.status_panier}) ({self.total_montant_panier})"
    
class Categorie_Produit(models.Model) :
    name = models.CharField(max_length=120)
class Produit(models.Model) :
    name = models.CharField(max_length=120)
    categorie = models.ForeignKey(Categorie_Produit, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="image_product")
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateField()

class Commande(models.Model) :
    MODE_PAIEMENT = (
        ("carte_credit", "Carte Credit"),
        ('paypal', "PayPal")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commanded = models.DateField(auto_now_add=True)
    montant_total_commande = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=120)
    adresse_livraison = models.TextField()
    mode_paiement = models.CharField(max_length=20, choices=MODE_PAIEMENT)
    date_expedition = models.DateField()
    date_livraison  = models.DateField()
    def __str__(self) :
        return f"{self.user.username} ({self.montant_total_commande})"

class Commande_Produit(models.Model) :
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_au_moment = models.DecimalField(max_digits=12, decimal_places=2)
    total_article = models.IntegerField()
    def save(self, *args, **kwargs):
        self.total_article = self.quantity * self.price_au_moment
        super().save(*args, **kwargs)
    def __str__(self) :
        return f"{self.commande} ({self.produit.name})"
    