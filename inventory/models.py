from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    cantidad = models.IntegerField(null=False, default=10)

    def __unicode__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=200, null=False)
    tel = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=60, null=False)

    def __unicode__(self):
        return self.nombre