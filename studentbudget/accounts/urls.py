
from django.urls import path

from . import views

urlpatterns = [
     path("index", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("renter_login", views.renter_login, name="renter_login"),
    path("renter_signup", views.renter_signup, name="renter_signup"),
     path("details", views.details, name="details"),
    path("logout", views.logout, name="logout"),
   
    ]