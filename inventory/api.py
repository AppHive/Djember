from inventory.models import Producto,Proveedor
from serializers import ProductoSerializer,ProveedorSerializer
from rest_framework import generics


class ProductoMixin(object):
    """
    Clase base (Mixin) que comprende el listado de todas
    la coleccion de productos e indica el serializer a
    utilizar para los endpoints.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProveedorMixin(object):
    """
    Clase base (Mixin) que comprende el listado de todas
    la coleccion de proveedores e indica el serializer a
    utilizar para los endpoints.
    """
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProductoList(ProductoMixin, generics.ListCreateAPIView):
    """
    Clase que hereda de ProductoMixin e implementa las vistas
    genericas de DRF para mostrar el listado de productos
    o para crear un nuevo producto.
    """
    pass


class ProductoDetail(ProductoMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Clase que hereda de ProductoMixin e implementa las vistas
    genericas de DRF para mostrar un Producto en especial,
    actualizar un producto o para eliminar un producto.
    """
    pass


class ProveedorList(ProveedorMixin, generics.ListCreateAPIView):
    """
    Clase que hereda de ProveedorMixin e implementa las vistas
    genericas de DRF para mostrar el listado de proveedores
    o para crear un nuevo proveedor.
    """
    pass


class ProveedorDetail(ProveedorMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Clase que hereda de ProveedorMixin e implementa las vistas
    genericas de DRF para mostrar un Proveedor en especial,
    actualizar un proveedor o para eliminar un proveedor.
    """
    pass


