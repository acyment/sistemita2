# Generated by Django 2.2.10 on 2020-03-11 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0029_auto_20200224_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagoimpuestoalcheque',
            name='pago',
        ),
    ]
