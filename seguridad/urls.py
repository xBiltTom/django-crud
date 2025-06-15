from django.urls import path,include 
from .views import acceder,homePage
from django.contrib.auth import views
urlpatterns = [
    path('',acceder,name="login"),
    path('home/',homePage,name="home"),
]