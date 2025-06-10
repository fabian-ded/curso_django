from django.contrib import admin
from .models import Project, Task

# Register your models here.
admin.site.register(Project)#aqui es para que en la parte de administrador tambien aparezca nuestos models que creamos en la aplicacion
admin.site.register(Task)