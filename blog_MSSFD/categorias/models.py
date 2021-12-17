from django.db import models
from django.utils import timezone

# Creación de campos de la tabla de categorías

class Categorias(models.Model):
    nombre = models.CharField(max_length=100, default='')
    detalles= models.CharField(max_length=1000, default='descripción de la categoría')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = "categorias"