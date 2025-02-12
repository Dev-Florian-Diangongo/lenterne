import requests
import json

# URL de l'API
url = "http://127.0.0.1:8000/produits/"

# Paramètres de filtrage : ici, tu filtres par la catégorie avec l'ID 1
params = {'categorie': 'jus'}

# Faire la requête GET avec les paramètres
response = requests.get(url=url, params=params)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    print(response.json())  # Afficher la réponse JSON (les produits)
else:
    print(f"Erreur {response.status_code}: Impossible de récupérer les produits.")
