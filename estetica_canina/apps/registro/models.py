from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Cita(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha_cita = models.DateField()


    def str(self):
        return self.nombre

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)

    def str(self):
        return self.nombre_usuario


