from django.db import models
from django.utils import timezone

# Creación de campos de la tabla de entradas

class Entradas(models.Model):
    titulo = models.CharField(max_length=300, default='')
    contenido= models.TextField (default="Texto del post")
    img_destacada = models.FileField()
    slug = models.CharField(max_length=2500, default= 'DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = "entradas"