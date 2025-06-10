from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def Hola(request, username):#aqui el username es el dato que debe reciir para funcionar esta funcion
    print(username)#se muestra el username que ingreso el usuario mediante la url
    return HttpResponse("<h1>Hola %s</h1>" %username)

def estado(request):
    return HttpResponse("<h2>Comó estás?</h2>")

def index(request):
    return HttpResponse("index page")

def projects(request):
    proyectos = list(Project.objects.values())#.objects: Es un tipo administrador por defecto que crea Django, y a través de él, accedemos a los métodos para interactuar con la base de datos.
    return JsonResponse(proyectos, safe=False)

def tasks(request, id):#se recibe un id mediante la url que es recibido como un parametro en esta funcion
    #task = Task.objects.get(id=id)#se hace la consulta en la base de datos
    task =get_object_or_404(Task, id=id)
    return HttpResponse("tasks: %s " %  task.title)