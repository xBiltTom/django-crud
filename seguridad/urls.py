from django.urls import path,include 
from .views import acceder
urlpatterns = [path('',acceder,name="login"),]