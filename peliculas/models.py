from django.db import models

class Peliculas(models.Model):
    nombre = models.CharField(max_length=150)
    director = models.CharField(max_length=100)
    año_de_lanzamiento = models.IntegerField()
    estado = models.BooleanField(default=False)
    portada = models.ImageField(upload_to="portadas_peliculas", null=True, blank=True)
    sinopsis = models.CharField(max_length=1000)
    recaudacion = models.FloatField()
    donde_ver = models.CharField(max_length=50)
    genero = models.CharField(max_length=100)
    duracion = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"










