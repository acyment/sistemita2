# Generated by Django 2.2.7 on 2020-02-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0027_auto_20200222_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientocuenta',
            name='estado',
        ),
        migrations.AddField(
            model_name='movimientocuenta',
            name='cobrado',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
    ]
