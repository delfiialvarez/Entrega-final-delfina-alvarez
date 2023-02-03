from django.urls import path
from peliculas.views import crear_peliculas, listar_peliculas, detalle_pelicula, actualizar_pelicula, BorrarPeliculasView

urlpatterns = [
    path("crear-peliculas/", crear_peliculas, name= "Crear peliculas"),
    path("listado-peliculas/", listar_peliculas, name= "Lista de peliculas"),
    path("detalle-pelicula/<int:pk>", detalle_pelicula, name="Detalle pelicula"),
    path("actualizar-pelicula/<int:pk>", actualizar_pelicula, name="Actualizar pelicula"),
    path("borrar-pelicula/<int:pk>", BorrarPeliculasView.as_view(), name="Borrar pelicula"),
    
]