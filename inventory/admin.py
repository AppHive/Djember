from django.contrib import admin
from inventory.models import Producto, Proveedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Proveedor)