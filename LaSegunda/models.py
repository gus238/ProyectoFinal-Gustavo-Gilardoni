from django.db import models
from django.contrib.auth.models import User


class Amigo(models.Model):

    nombre = models.CharField(max_length=40)
    nacimiento = models.IntegerField()
    imagen = models.ImageField(upload_to='la_segunda_objetos', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Nacimiento: {self.nacimiento}"

class Avatar2(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='la_segunda_avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

'''class ObjetoImagen(models.Model):

    imagen = models.ImageField(upload_to='la_segunda_objetos', null=True, blank=True)'''
