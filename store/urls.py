from django.urls import path
from . import views

urlpatterns = [
    #path("admin/":'como se debe llamar en la url para que se pueda ver', "admin.site.urls":la ruta donde debe buscar django para mostrar si el usuario busco por esa url)
    path('', views.index),
    path('estado/', views.estado),
    path('Hola/<str:username>', views.Hola),#ese "<str:username>" funciona para esperar un parametro que nos de el usuario y al recibirlo mostrar el contenido que se debe enviar
    path('projects/', views.projects),
    path('tasks/', views.tasks),
]
