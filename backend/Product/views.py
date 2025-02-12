from django.shortcuts import render
from .serializers import SerialierPanier
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Panier

class PanierView(APIView) :
    def post(self, request, *args, **kwargs) :
        if request.method == "POST" :
            user = request.data.get["user"]
            status_panier = request.data.get["status_panier"]
            total_montant_panier = request.data.get["total_montant_panier"]
            if user != None and status_panier != None and total_montant_panier != None:
                panier = Panier.objects.create(
                    user=user,
                    status_panier = status_panier,
                    total_montant_panier=total_montant_panier
                )
                if panier :
                    return Response({
                        'detail':"Panier créé avec succès !"
                    }, status=status.HTTP_201_CREATED)
            else :
                return Response({"detail":"echec de créatio du panier !"}, status=status.HTTP_400_BAD_REQUEST)
        else :
            return Response({"detail":"method not allowed !"}, status=status.HTTP_403_FORBIDDEN)
                    