from django.urls import path
from django.contrib.auth.views import LogoutView

from usuarios.views import login_view, register_view, update_user, update_user_profile, user_detail
urlpatterns = [
   path("acceso/", login_view, name="acceso"),
   path("registro/", register_view, name="registro"),
   path("actualizar-usuario/", update_user, name="actualizar usuario"),
   path("actualizar-perfil/", update_user_profile, name="actualizar perfil"),
   path("salir/", LogoutView.as_view(template_name = "usuarios/salir.html")),
   path("detalle-usuario/<int:pk>", user_detail, name="Detalle usuario"),
]