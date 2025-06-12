from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name #aqui se retorna o muestra el nombre del proyecto que se tiene en la base de datos
    
    
class Task(models.Model):
    title = models.CharField(max_length=100)#para un numero de textos permitidos escribir
    description = models.TextField()#para textos mucho mas largos
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)#Aqui se hace la relacion de las dos clases o mejor dicho de las dos tablas
    #ademas utilizamos la funcion de cascada que hace que si se elimina un proyecto se eliminen los datos que se tienen relacionados a ese
    done = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title + ' - ' + self.Project.name #aqui se retorna el titulo y ademas se úede mostrar el nombre del proyecto de la otra tabla que esta relaccionada
    
    