
from django.urls import path
from .views import (LoginView, LogoutUserView, ApiRegisterView)

urlpatterns = [
    path('register/', ApiRegisterView.as_view(), name="register_user"),
    path('login_user/', LoginView.as_view(), name="login_user"),
    path('logout_user/', LogoutUserView.as_view(), name="logout_user"),
]
