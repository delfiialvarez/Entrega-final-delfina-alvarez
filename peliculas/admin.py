from django.contrib import admin
from peliculas.models import Peliculas

@admin.register(Peliculas)
class Peliculasadmin(admin.ModelAdmin):
    list_display = ("nombre", "director", "año_de_lanzamiento", "estado", "portada")
    list_filter = ("estado",)
    search_fields = ("nombre",)
