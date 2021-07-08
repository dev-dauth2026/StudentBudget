from django.contrib import admin
from django.urls import path
from . import views
from studentrent import views

urlpatterns = [
    path('', views.index, name='index'),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("search/", views.search, name="search"),
    path("renter_search/", views.renter_search, name="renter_search"),
    path("renter_dashboard/", views.renter_dashboard, name="renter_dashboard"),
    path("renter_search/", views.renter_search, name="renter_search"),
     
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("renter_login/", views.renter_login, name="renter_login"),
    path("renter_signup/", views.renter_signup, name="renter_signup"),
    path("landlord_login/", views.renter_login, name="renter_login"),
    path("lanlord_signup/", views.renter_signup, name="renter_signup"),
    path("<int:pk>", views.details.as_view(), name="details"),
    path("renter_payment/", views.renter_payment, name="renter_payment"),
    path("apply<int:pk>/", views.apply.as_view(), name="apply"),
    path("logout/", views.logout, name="logout"),
    #path("addtofavorite<int:f_pk>/", views.addtofavorite.as_view(), name="addtofavorite"),
   
    
    ]