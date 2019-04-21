from django.urls import path
from .apiviews import Bought, UserCreate, LoginView, ResetPassword
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/', UserCreate.as_view(), name="user_create"),
    path('users/buy/', Bought.as_view(), name='bought'),
    path("login/", LoginView.as_view(), name="login"),
    path("reset_password/", ResetPassword.as_view(), name="reset_password"),
]
