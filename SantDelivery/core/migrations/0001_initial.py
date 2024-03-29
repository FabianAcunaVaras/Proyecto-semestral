
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabecera_Pedidos',
            fields=[
                ('idCabPedido', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Cabecera Pedido')),
                ('FechaPedido', models.DateTimeField(verbose_name='Fecha Hora Pedido')),
                ('ObsPedido', models.CharField(max_length=200, verbose_name='Observación del Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Clientes',
            fields=[
                ('idEstadoCliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Estado Clientes')),
                ('GlosaEstado', models.CharField(max_length=50, verbose_name='Glosa Estado Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Despacho',
            fields=[
                ('idEstadoDespacho', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Estado Despacho')),
                ('GlosaEstadoDespacho', models.CharField(max_length=50, verbose_name='Glosa Estado Despacho')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Producto',
            fields=[
                ('idEstadoProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Estado Producto')),
                ('GlosaEstadoProducto', models.CharField(max_length=50, verbose_name='Glosa Estado Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Repartidor',
            fields=[
                ('idEstadoRepartidor', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Estado Repartidor')),
                ('GlosaEstadoRepartidor', models.CharField(max_length=50, verbose_name='Glosa Estado Repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('idRepartidor', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Repartidor')),
                ('Rut', models.IntegerField(verbose_name='Rut Repartidor')),
                ('DvRut', models.CharField(max_length=1, verbose_name='DvRut Repartidor')),
                ('NombreCompleto', models.CharField(max_length=200, verbose_name='Nombre Completo Repartidor')),
                ('Telefono', models.CharField(max_length=12, verbose_name='Telefóno Cliente')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Dirección Cliente')),
                ('Mail', models.CharField(max_length=50, verbose_name='E-mail Cliente')),
                ('EstadoReparidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado_repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('NombreProducto', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('DescripcionProducto', models.CharField(max_length=1000, verbose_name='Descripción Producto')),
                ('ValorProducto', models.IntegerField(verbose_name='Valor Producto')),
                ('IdEstadoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Pedidos',
            fields=[
                ('idDetPedido', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Detalle del Pedido')),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad Productos')),
                ('ObsProducto', models.CharField(max_length=200, verbose_name='Observación del Producto')),
                ('idCabPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cabecera_pedidos')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idClientes', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Clientes')),
                ('Rut', models.IntegerField(verbose_name='Rut Cliente')),
                ('DvRut', models.CharField(max_length=1, verbose_name='DvRut Cliente')),
                ('NombreCompleto', models.CharField(max_length=200, verbose_name='Nombre Completo Cliente')),
                ('Telefono', models.CharField(max_length=12, verbose_name='Telefóno Cliente')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Dirección Cliente')),
                ('Mail', models.CharField(max_length=50, verbose_name='E-mail Cliente')),
                ('Password', models.CharField(max_length=10, verbose_name='Password Cliente')),
                ('EstadoCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado_clientes')),
            ],
        ),
        migrations.AddField(
            model_name='cabecera_pedidos',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clientes'),
        ),
        migrations.AddField(
            model_name='cabecera_pedidos',
            name='idEstadoDespacho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado_despacho'),
        ),
        migrations.AddField(
            model_name='cabecera_pedidos',
            name='idRepatidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.repartidor'),
        ),
    ]
