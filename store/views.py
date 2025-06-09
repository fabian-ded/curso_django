from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hola(request, username):#aqui el username es el dato que debe reciir para funcionar esta funcion
    print(username)#se muestra el username que ingreso el usuario mediante la url
    return HttpResponse("<h1>Hola %s</h1>" %username)

def estado(request):
    return HttpResponse("<h2>Comó estás?</h2>")

def index(request):
    return HttpResponse("index page")