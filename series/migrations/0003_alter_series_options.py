# Generated by Django 4.1.4 on 2023-02-03 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_alter_series_año_de_lanzamiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Serie', 'verbose_name_plural': 'Series'},
        ),
    ]