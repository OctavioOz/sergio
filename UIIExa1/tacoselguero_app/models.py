from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente=models.PositiveSmallIntegerField()
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    orden=models.CharField(max_length=100)
    pago=models.CharField(max_length=100)
    cantidad=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombres