from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Juego(models.Model):

    nombre = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    jugadores = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Empresa: {self.empresa} - Categoria: {self.categoria} - Jugadores: {self.jugadores}"

class Influencer(models.Model):

    nombre = models.CharField(max_length=40)
    nacimiento = models.IntegerField()
    imagen = models.ImageField(upload_to='app_generica_objetos', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Nacimiento: {self.nacimiento}"


class Plataforma(models.Model):

    nombre = models.CharField(max_length=40)
    ceo = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Ceo: {self.ceo}"
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
