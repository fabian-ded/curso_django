"""
URL configuration for nuevoproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import Hola #forma de llamar la funcion que tenemos en la aplicacion
from store import views # segunda forma de llamar la funcion de nuestra aplicacion

urlpatterns = [
    path('admin/', admin.site.urls), #path("admin/":'como se debe llamar en la url para que se pueda ver', "admin.site.urls":la ruta donde debe buscar django para mostrar si el usuario busco por esa url)
    path('', Hola), #forma 1
    path('estado/', views.estado) #forma 2
]
