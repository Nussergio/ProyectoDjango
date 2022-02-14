from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from ssl import create_default_context
from tabnanny import verbose
from django.db import models
from django.forms import CharField

# Create your models here.

class servicio(models.Model):
    titulo=models.CharField(max_length=50)
    Contento=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateField(auto_now=True)
    updated=models.DateField(auto_now=True)
    
    class Meta:
        verbose_name='servicio'
        verbose_name='servicios'
    def __str__(self):
        return self.titulo
        