from django.urls import path
from .apiviews import Bought, UserCreate, LoginView

urlpatterns = [
    path('users/', UserCreate.as_view(), name="user_create"),
    path('users/buy/', Bought.as_view(), name='bought'),
    path("login/", LoginView.as_view(), name="login"),
]
