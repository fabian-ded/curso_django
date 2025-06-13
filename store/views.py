from django.shortcuts import render #render se utiliza para mostrar que diferentes htmls que tenemos en nuestro template y que se puedan utilizar aqui
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404 #esta importacion de libreria es para que nos muestre un error 404 si es que lo hay

# Create your views here.
def Hola(request, username):#aqui el username es el dato que debe reciir para funcionar esta funcion
    print(username)#se muestra el username que ingreso el usuario mediante la url
    return HttpResponse("<h1>Hola %s</h1>" %username)

def estado(request):
    nombre = 'Carlos'
    return render(request, 'estado.html', {'username': nombre})

def index(request):
    titulo = 'Django!!' #infromacion que queremos pasar al html 
    return render(request,'index.html', {'title': titulo})#aqui se utiliza la función render para mostrar la plantilla 'index.html'y el objeto 'request' contiene información sobre la solicitud web actual.
    #el "{title:titulo} es para mostrar esa infomacion que tenemos en la variables de titulo pasarla a title y este lo pasamos al archivo html de index.html"

def projects(request):
    #proyectos = list(Project.objects.values())#.objects: Es un tipo administrador por defecto que crea Django, y a través de él, accedemos a los métodos para interactuar con la base de datos.
    projects = Project.objects.all()#para traer toda la informacion de la base de datos
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):#se recibe un id mediante la url que es recibido como un parametro en esta funcion
    #task = Task.objects.get(id=id)#se hace la consulta en la base de datos
    #task =get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'task.html', {'taske': tasks})