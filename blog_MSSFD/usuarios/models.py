from django.db import models
from django.utils import timezone
#creacion de campos de la tabla usuarios
class Usuarios(models.Model):
    nombre = models.CharField(max_length=1000, default='DEFAULT VALUE')
    img = models.FileField()
    web = models.CharField(max_length=700, default='DEFAULT VALUE')
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
	    db_table = 'usuarios'