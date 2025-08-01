# Generated by Django 4.2 on 2025-06-28 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0004_rename_categorias_productos_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cabeceraVentas',
            fields=[
                ('venta_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nrodoc', models.CharField(max_length=12)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='ruc_dni',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeracion', models.CharField(max_length=15)),
                ('serie', models.CharField(max_length=3)),
                ('tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='detalleVentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.productos')),
                ('venta_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.cabeceraventas')),
            ],
        ),
        migrations.AddField(
            model_name='cabeceraventas',
            name='cliente_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.cliente'),
        ),
        migrations.AddField(
            model_name='cabeceraventas',
            name='tipo_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.tipo'),
        ),
    ]
