# Generated by Django 4.1.4 on 2023-02-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
