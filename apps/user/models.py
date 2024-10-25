from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.rol.models import Rol
from django.db.models import SET_NULL

class User(AbstractUser):
    cedula = models.CharField(max_length=20,null=True)
    edad = models.CharField(max_length=20, unique=True,null=True)
    fkrol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username


# Create your models here.
