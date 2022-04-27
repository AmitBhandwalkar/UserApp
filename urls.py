from django.urls import path
from . import views

urlpatterns = [
    path('registerPage/',views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logIn/', views.logIn, name='logIn'),
     path('logOut/', views.logOut, name='logOut'),
]
