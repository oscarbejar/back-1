from turtle import back
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "front/home.html")

def perfil(request):

    return render(request, "front/home.html")


def sitios(request):

    return render(request, "front/home.html")