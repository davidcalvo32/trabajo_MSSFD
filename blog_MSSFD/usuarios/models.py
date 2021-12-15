from django.db import models
from django.utils import timezone

# Creación de campos de la tabla de usuario

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=100, default='')
    img = models.FileField()
    web = models.CharField(max_length=500, default = 'DEFAULT VALUE')
    descripcion= models.TextField(default='Mi descripcion')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = "usuarios"