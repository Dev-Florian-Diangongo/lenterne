from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

USER = get_user_model()

class LoginView(TokenObtainPairView) :
    serializer_class = TokenObtainPairSerializer

class ApiRegisterView(APIView):
    def post(self, request, *args, **kwargs) :
        username = request.data.get("username")
        password = request.data.get("password")
        if  User.objects.filter(username=username).exists() :
            return Response({"detail":"le nom d'utilisateur entré existe déjà dans notre système. Veuillez vous connecter "}, status=status.HTTP_400_BAD_REQUEST)
        if username is None or password is None :
            return Response({"deatil":"tous les champs sont obligatoires"},  status=status.HTTP_400_BAD_REQUEST)
        user = USER.objects.create_user(username=username, password=password)
        if user :
            refres_token = RefreshToken.for_user(user)
            return Response({"detail":f"l'utilisateur  {username}  est créé avec succès ! ", "refresh":str(refres_token), "access":str(refres_token.access_token)}, status=status.HTTP_201_CREATED)
class LogoutUserView(APIView):
    def post(self, request, *args, **kwargs) :
        try :
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail":"Deconnexion réussi"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e :
            return Response({"detail": str(e)} ,status=status.HTTP_400_BAD_REQUEST)
            
        
