from django.db import models

# Create your models here.

class Rol(models.Model):
    choices_rol = (
        ('Tecnico','tecnico'),
        ('Catador','catador'),
        ('Barista','barista')
    )
    estado_choices = models.CharField(max_length=100, choices=choices_rol)
    
    def __str__(self) -> str:
        return self.estado_choices