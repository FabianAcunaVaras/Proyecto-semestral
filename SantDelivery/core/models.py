from django.db import models



# Create your models here.
class Estado_Clientes(models.Model):
    idEstadoCliente = models.AutoField(primary_key=True, verbose_name="Id Estado Clientes")
    GlosaEstado = models.CharField(max_length=50, verbose_name="Glosa Estado Cliente")

    def __str__(self):
        return self.GlosaEstado

class Estado_Despacho(models.Model):
    idEstadoDespacho = models.AutoField(primary_key=True, verbose_name="Id Estado Despacho")
    GlosaEstadoDespacho = models.CharField(max_length=50, verbose_name="Glosa Estado Despacho")

    def __str__(self):
        return self.GlosaEstadoDespacho

class Estado_Repartidor(models.Model):
    idEstadoRepartidor = models.AutoField(primary_key=True, verbose_name="Id Estado Repartidor")
    GlosaEstadoRepartidor = models.CharField(max_length=50, verbose_name="Glosa Estado Repartidor")

    def __str__(self):
        return self.GlosaEstadoRepartidor

class Estado_Producto(models.Model):
    idEstadoProducto = models.AutoField(primary_key=True, verbose_name="Id Estado Producto")
    GlosaEstadoProducto = models.CharField(max_length=50, verbose_name="Glosa Estado Producto")

    def __str__(self):
        return self.GlosaEstadoProducto

class Clientes(models.Model):
    idClientes = models.AutoField(primary_key=True, verbose_name="Id Clientes")
    Rut = models.IntegerField(verbose_name="Rut Cliente")
    DvRut = models.CharField(max_length=1, verbose_name="DvRut Cliente")
    NombreCompleto = models.CharField(max_length=200, verbose_name="Nombre Completo Cliente")
    Telefono = models.CharField(max_length=12, verbose_name="Telefóno Cliente")
    Direccion = models.CharField(max_length=100, verbose_name="Dirección Cliente")
    Mail = models.CharField(max_length=50, verbose_name="E-mail Cliente")
    Password = models.CharField(max_length=10, verbose_name="Password Cliente")
    idEstadoCliente = models.ForeignKey(Estado_Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.DvRut

class Repartidor(models.Model):
    idRepartidor = models.AutoField(primary_key=True, verbose_name="Id Repartidor")
    Rut = models.IntegerField(verbose_name="Rut Repartidor")
    DvRut = models.CharField(max_length=1, verbose_name="DvRut Repartidor")
    NombreCompleto = models.CharField(max_length=200, verbose_name="Nombre Completo Repartidor")
    Telefono = models.CharField(max_length=12, verbose_name="Telefóno Cliente")
    Direccion = models.CharField(max_length=100, verbose_name="Dirección Cliente")
    Mail = models.CharField(max_length=50, verbose_name="E-mail Cliente")
    EstadoReparidor = models.ForeignKey(Estado_Repartidor, on_delete=models.CASCADE)

    def __str__(self):
        return self.DvRut

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Id Producto")
    NombreProducto = models.CharField(max_length=100, verbose_name="Nombre Producto")
    DescripcionProducto = models.CharField(max_length=1000, verbose_name="Descripción Producto")
    ValorProducto = models.IntegerField(verbose_name="Valor Producto")
    IdEstadoProducto = models.ForeignKey(Estado_Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NombreProducto

class Cabecera_Pedidos(models.Model):
    idCabPedido = models.AutoField(primary_key=True, verbose_name="Id Cabecera Pedido")
    FechaPedido = models.DateTimeField(verbose_name="Fecha Hora Pedido")
    ObsPedido = models.CharField(max_length=200, verbose_name="Observación del Pedido")
    idCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    idRepatidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    idEstadoDespacho = models.ForeignKey(Estado_Despacho, on_delete=models.CASCADE)

    def __str__(self):
        return self.FechaPedido

class Detalle_Pedidos(models.Model):
    idCabPedido = models.ForeignKey(Cabecera_Pedidos, on_delete=models.CASCADE)
    idDetPedido = models.AutoField(primary_key=True, verbose_name="Id Detalle del Pedido")
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(verbose_name="Cantidad Productos")
    ObsProducto = models.CharField(max_length=200, verbose_name="Observación del Producto")
    
    def __str__(self):
        return self.ObsProducto