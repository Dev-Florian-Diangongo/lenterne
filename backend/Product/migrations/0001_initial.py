
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie_Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commanded', models.DateField(auto_now_add=True)),
                ('montant_total_commande', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(max_length=120)),
                ('adresse_livraison', models.TextField()),
                ('mode_paiement', models.CharField(choices=[('carte_credit', 'Carte Credit'), ('paypal', 'PayPal')], max_length=20)),
                ('date_expedition', models.DateField()),
                ('date_livraison', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status_panier', models.CharField(choices=[('cours', 'En cours'), ('abandonne', 'abandonné')], max_length=20)),
                ('total_montant_panier', models.DecimalField(decimal_places=2, max_digits=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('stock', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='image_product')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_expiration', models.DateField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.categorie_produit')),
            ],
        ),
        migrations.CreateModel(
            name='Commande_Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price_au_moment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_article', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.produit')),
            ],
        ),
    ]
