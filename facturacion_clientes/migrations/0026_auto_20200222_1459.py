# Generated by Django 2.2.7 on 2020-02-22 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0025_pagoliqueedaconsultor_facturador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoliqueedaconsultor',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion_clientes.FacturaCliente'),
        ),
    ]
