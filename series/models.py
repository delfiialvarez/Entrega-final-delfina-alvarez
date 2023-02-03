from django.db import models

class Series(models.Model):

    ESTADO_CHOICES = (
        ("En proceso", "En proceso"),
        ("Terminada", "Terminada"),
    )

    nombre = models.CharField(max_length=150)
    cantidad_de_temporadas = models.IntegerField()
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices= ESTADO_CHOICES)
    donde_ver = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=1000)
    portada = models.ImageField(upload_to="portadas_series", null=True, blank=True)
    año_de_lanzamiento = models.IntegerField()
    estado_personal = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"
