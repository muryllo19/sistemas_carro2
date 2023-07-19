from django.db import models

# Create your models here.
class carro(models.Model):

    placa = models.CharField(max_length=255)
    ano = models.IntegerField()
    modelo = models.CharField(max_length= 255)
    cor = models.CharField(max_length=255)
    

def __str__(self):
    return self.modelo





