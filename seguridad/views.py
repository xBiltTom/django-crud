from django.shortcuts import render

# Create your views here.
def acceder(request):
    return render(request,'login.html')