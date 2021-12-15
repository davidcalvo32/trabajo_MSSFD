from django.db import models
from django.utils import timezone

# Creación de campos de detalles del blog

class DetallesBlog(models.Model):
    detalles = models.CharField(max_length=5000, default='')
    logo= models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = "detallesblog"