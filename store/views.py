from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hola(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def estado(request):
    return HttpResponse("<h2>Comó estás?</h2>")