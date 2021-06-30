from django.forms import ModelForm
from .models import Estado_Clientes,Estado_Despacho,Estado_Repartidor,Estado_Producto,Clientes,Repartidor,Productos

class Estado_ClientesForm(ModelForm):
    class Meta:
        model = Estado_Clientes
        fields = ['idEstadoCliente', 'GlosaEstado']

class Estado_RepartidorForm(ModelForm):
    class Meta:
        model = Estado_Repartidor
        fields = ['idEstadoRepartidor', 'GlosaEstadoRepartidor']

class Estado_DespachoForm(ModelForm):
    class Meta:
        model = Estado_Despacho
        fields = ['idEstadoDespacho', 'GlosaEstadoDespacho']

class Estado_ProductoForm(ModelForm):
    class Meta:
        model = Estado_Producto
        fields = ['idEstadoProducto', 'GlosaEstadoProducto']

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['idClientes', 'Rut', 'DvRut', 'NombreCompleto', 'Telefono', 'Direccion', 'Mail', 'Password', 'EstadoCliente']

class RepartidorForm(ModelForm):
    class Meta:
        model = Repartidor
        fields = ['idRepartidor', 'Rut', 'DvRut', 'NombreCompleto', 'Telefono', 'Direccion', 'Mail', 'EstadoCliente']

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['idProducto', 'NombreProducto', 'DescripcionProducto', 'ValorProducto', 'IdEstadoProducto']
