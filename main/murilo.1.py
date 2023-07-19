from django.db import models

# Create your models here.
class aluno(models.Model):

    fabricaçao = models.CharField(max_length=255)
    ano = models.IntegerField()
    marca = models.MarcaField()
    placa = models.PlacaField(null=True)
    description = models.TextField()

def __str__(self):
    return self.modelo
