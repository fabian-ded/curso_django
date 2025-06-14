from django.shortcuts import render, redirect #render se utiliza para mostrar que diferentes htmls que tenemos en nuestro template y que se puedan utilizar aqui, ademas el "redirect" se utiliza para colocar direcciones en la url para irnos a otro lugar o otro html
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404 #esta importacion de libreria es para que nos muestre un error 404 si es que lo hay
from .forms import CreateNewTask, CreateNewProject

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
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):#se recibe un id mediante la url que es recibido como un parametro en esta funcion
    #task = Task.objects.get(id=id)#se hace la consulta en la base de datos
    #task =get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {'taske': tasks})

def Create_task(request):
    #print(request.GET['title'])#para buscar la informacion recibida
    if request.method == 'GET':#aqui estamos diciendo que si nos estan visitando del metodo "get" no renderice el html normal que tenemos de interface
        return render(request, "tasks/create_task.html", {
        "form": CreateNewTask() #llamamos la funcion que creamos para hacer una plantilla de imput para los html
    })
    else: #pero aqui estamos diciendo que si nos estan visitando de otro metodo pues se ejecuta esta linea, para que se incerten esos datos a la base de datos si nos estan visitando con el metodo "POST"
        Task.objects.create(
            title=request.POST['title'],description=request.POST['description'],Project_id=request.POST['id_project'])#apunte importante si no funciona la relacion que tenemos en el model que tenemos como base de datos, sirve tambien rebizar directamente la base de datos creada que tenemos con esos modelos porque tal vez hay veces que django nombra o agrega mas caracteres a nuestras columnas de la base de datos y como el model lo tenemos tal cual al momento de ejecutar algo para guardar puede salir error entonces es importante tambien mirar la base de datos.
        return redirect("/tasks/")

def Create_Project(request):
    if request.method == 'GET':
        return render (request, "projects/create_project.html", {"forms": CreateNewProject() })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        #return render (request, "projects/create_project.html", {"forms": CreateNewProject() })
        return redirect("/projects/")
        