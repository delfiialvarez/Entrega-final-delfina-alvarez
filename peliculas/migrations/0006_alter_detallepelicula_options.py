# Generated by Django 4.1.4 on 2023-02-02 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0005_alter_detallepelicula_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallepelicula',
            options={'verbose_name': 'pelicula', 'verbose_name_plural': 'pelicula'},
        ),
    ]
