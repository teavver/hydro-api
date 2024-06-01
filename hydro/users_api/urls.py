from django.urls import path
from .views import UserCreate, UserLogin

urlpatterns = [
    path("register/", UserCreate.as_view(), name="user-register"),
    path("login/", UserLogin.as_view(), name="user-login"),
]
