# Generated by Django 2.2.7 on 2019-11-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0022_cliente_cuit'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='descripcion_en_resumen_bancario',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]