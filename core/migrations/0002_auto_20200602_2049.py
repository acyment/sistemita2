# Generated by Django 3.0.6 on 2020-06-02 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado'),
        ),
    ]