from django.db import models

class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, default='Desconocido')  # Nuevo campo

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='productos')
    f_vencimiento = models.DateField(null=True, blank=True)  # Nuevo campo


    def __str__(self):
        return self.nombre
