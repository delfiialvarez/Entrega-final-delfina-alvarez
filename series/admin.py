from django.contrib import admin

from series.models import Series

@admin.register(Series)
class Seriesadmin(admin.ModelAdmin):
    list_display = ("nombre", "director", "año_de_lanzamiento", "estado", "portada")
    list_filter = ("estado",)
    search_fields = ("nombre",)
