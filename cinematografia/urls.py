from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from cinematografia.settings import MEDIA_ROOT, MEDIA_URL

from cinematografia.views import index, acerca_de

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name= "index"),
    path("acerca-de/", acerca_de, name="acerca de"),

    path("peliculas/", include("peliculas.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("series/", include("series.urls")),
]+ static(MEDIA_URL, document_root = MEDIA_ROOT)
