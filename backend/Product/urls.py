

from django.urls import path, include
from .views import PanierView

urlpatterns = [
    path("ajout_panier/", PanierView.as_view(), name="ajout_panier"),
]
