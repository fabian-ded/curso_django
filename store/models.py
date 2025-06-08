from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    
class Task(models.Model):
    title = models.CharField(max_length=100)#para un numero de textos permitidos escribir
    description = models.TextField()#para textos mucho mas largos
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)#Aqui se hace la relacion de las dos clases o mejor dicho de las dos tablas
    #ademas utilizamos la funcion de cascada que hace que si se elimina un proyecto se eliminen los datos que se tienen relacionados a ese
    
    