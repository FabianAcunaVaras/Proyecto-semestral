from django.forms import ModelForm
from .models import Estado_Clientes, Estado_Despacho, Estado_Repartidor, Estado_Producto , Clientes, Repartidor, Productos, Cabecera_Pedidos, Detalle_Pedidos

class Estado_ClientesForm(ModelForm):

    class Meta:
        model = Estado_Clientes
        fields = ['idEstadoCliente', 'GlosaEstado']



class Estado_DespachoForm(ModelForm):

    class Meta:
        model = Estado_Despacho
        fields = ['idEstadoDespacho', 'GlosaEstadoDespacho']


class Estado_RepartidorForm(ModelForm):

    class Meta:
        model = Estado_Repartidor
        fields = ['idEstadoRepartidor', 'GlosaEstadoRepartidor']



class Estado_ProductoForm(ModelForm):

    class Meta:
        model = Estado_Producto
        fields = ['idEstadoProducto', 'GlosaEstadoProducto']





class ClientesForm(ModelForm):

    class Meta:
        model = Clientes
        fields =['idClientes', 'Rut', 'DvRut', 'NombreCompleto' ,'Telefono', 'Direccion' ,'Mail', 'Password', 'EstadoCliente']



class RepartidorForm(ModelForm):

    class Meta:
        model = Repartidor
        fields =['idRepartidor', 'Rut', 'DvRut', 'NombreCompleto' ,'Telefono', 'Direccion' ,'Mail', 'EstadoReparidor']


class ProductosForm(ModelForm):

    class Meta:
        model = Productos
        fields =['idProducto', 'NombreProducto', 'DescripcionProducto', 'ValorProducto' ,'IdEstadoProducto']



class Cabecera_PedidosForm(ModelForm):

    class Meta:
        model = Cabecera_Pedidos
        fields =['idCabPedido', 'FechaPedido', 'ObsPedido', 'idCliente' ,'idRepatidor', 'idEstadoDespacho']



class Detalle_PedidosForm(ModelForm):

    class Meta:
        model = Detalle_Pedidos
        fields =['idCabPedido', 'idDetPedido', 'idProducto', 'Cantidad' ,'ObsProducto']

        
