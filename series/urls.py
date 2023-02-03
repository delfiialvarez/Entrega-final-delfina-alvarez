from django.urls import path

from series.views import crear_series, listar_series, detalle_serie, actualizar_serie, BorrarSeriesView

urlpatterns = [
    path("crear-series/", crear_series, name="Crear series"),
    path("listar-series/", listar_series, name="Listado series"),
    path("detalle-serie/<int:pk>", detalle_serie, name="Detalle serie"),
    path("actualizar-serie/<int:pk>", actualizar_serie, name="Actualizar serie"),
    path("borrar-serie/<int:pk>", BorrarSeriesView.as_view(), name="Borrar serie")
    
]