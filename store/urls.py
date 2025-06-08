from django.urls import path
from . import views

urlpatterns = [
    #path("admin/":'como se debe llamar en la url para que se pueda ver', "admin.site.urls":la ruta donde debe buscar django para mostrar si el usuario busco por esa url)
    path('', views.Hola),
    path('estado/', views.estado) 
]
