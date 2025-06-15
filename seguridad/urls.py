from django.urls import path,include 
from .views import acceder,homePage,salir
from django.contrib.auth import views
urlpatterns = [
    path('',acceder,name="login"),
    path('home/',homePage,name="home"),
    path('logout/',salir,name="logout"),
]