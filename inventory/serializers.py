from inventory.models import Producto, Proveedor
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'cantidad'
        )


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = (
            'id',
            'nombre',
            'descripcion',
            'tel',
            'email'
        )