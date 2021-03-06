# Generated by Django 3.0.7 on 2020-07-29 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='moneda',
            field=models.CharField(choices=[('P', '$'), ('D', 'U$$')], default='P', max_length=1),
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('fecha', models.DateField()),
                ('moneda', models.CharField(choices=[('P', '$'), ('D', 'U$$')], default='P', max_length=1)),
                ('monto', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
            options={
                'verbose_name': 'orden de compra',
                'verbose_name_plural': 'ordenes de compras',
                'ordering': ('fecha',),
            },
        ),
    ]
