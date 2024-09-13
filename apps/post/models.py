from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    order = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title