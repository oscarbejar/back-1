from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Lugares(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='lugares')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='lugar'
        verbose_name_plural='lugares'

def __str__(self):
    return self.titulo