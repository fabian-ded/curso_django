from django.urls import path
from . import views

urlpatterns = [
    # path("admin/":'como se debe llamar en la url para que se pueda ver', "admin.site.urls":la ruta donde debe buscar django para mostrar si el usuario busco por esa url)
    path('', views.index),
    path('estado/', views.estado),
    path('Hola/<str:username>', views.Hola),#ese "<str:username>" funciona para esperar un parametro que nos de el usuario y al recibirlo mostrar el contenido que se debe enviar, como en el ejemplo de views
    path('projects/', views.projects, name='projects'),# al colocar el "name=projects" estamos diciendo que ahora con solo el name podemos utilizar esta url donde se necesite con tan solo el name 
    path('tasks/', views.tasks, name='tasks'),#ademas el "name" ayuda por si llego en algun momento a cambiar la url pues con solo el name no pasa nada asi se cambie el nombre de la ruta que tenga o cambie
    path('create_task/', views.Create_task, name='create_task'),#el name es como un identificador para esta ruta
    path('create_project/', views.Create_Project, name='create_project')
]
