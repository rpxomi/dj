from django.db import models

# CREATE YOUR MODELS HERE
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=4, decimal_places=3) #ej: 1.000

    def __str__(self):
        return self.nombre
