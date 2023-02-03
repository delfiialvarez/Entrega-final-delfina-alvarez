from django.shortcuts import render
from django.views.generic import DeleteView

from peliculas.models import Peliculas
from peliculas.forms import PeliculasForm 


def crear_peliculas(request):
    if request.method == "GET":
        context = {
            "form": PeliculasForm
        }
        return render(request, "peliculas/crear_peliculas.html", context=context)
    elif request.method == "POST":
        form = PeliculasForm(request.POST, request.FILES)
        if form.is_valid():
            Peliculas.objects.create(
                nombre = form.cleaned_data["nombre"],
                director = form.cleaned_data["director"],
                año_de_lanzamiento = form.cleaned_data["año_de_lanzamiento"],
                estado = form.cleaned_data["estado"],
                portada = form.cleaned_data["portada"],
                sinopsis = form.cleaned_data["sinopsis"],
                recaudacion = form.cleaned_data["recaudacion"],
                donde_ver = form.cleaned_data["donde_ver"],
                genero = form.cleaned_data["genero"],
                duracion = form.cleaned_data["duracion"],
            )
            context = {
                "mensaje" : "Película agregada exitosamente"
            }
            return render(request, "peliculas/crear_peliculas.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": PeliculasForm()
            }
            return render(request, "peliculas/crear_peliculas.html", context=context)

def listar_peliculas(request):
    if "search" in request.GET:
        peliculas = Peliculas.objects.filter(nombre__icontains = request.GET["search"])
    else:
        peliculas = Peliculas.objects.all()
    context = {
        "peliculas": peliculas,
    }
    return render(request, "peliculas/listado_peliculas.html", context=context)

def detalle_pelicula(request,pk):
    pelicula = Peliculas.objects.get(id=pk)
    context= {
        "pelicula": pelicula
    }
    return render(request, "peliculas/detalle_pelicula.html", context=context)

def actualizar_pelicula(request,pk):
    pelicula = Peliculas.objects.get(id=pk)

    if request.method == "GET":
        context = {
            "form": PeliculasForm(
                initial= {
                   "nombre": pelicula.nombre,
                   "director": pelicula.director,
                   "año_de_lanzamiento": pelicula.año_de_lanzamiento,
                   "estado": pelicula.estado,
                   "portada": pelicula.portada,
                   "sinopsis": pelicula.sinopsis,
                   "recaudacion": pelicula.recaudacion,
                   "donde_ver": pelicula.donde_ver,
                   "genero": pelicula.genero,
                   "duracion": pelicula.duracion,
                }
            )
        }
        return render(request, "peliculas/actualizar_pelicula.html", context= context)
    elif request.method == "POST":
        form = PeliculasForm(request.POST, request.FILES)
        if form.is_valid():
            pelicula.nombre = form.cleaned_data["nombre"]
            pelicula.director = form.cleaned_data["director"]
            pelicula.año_de_lanzamiento = form.cleaned_data["año_de_lanzamiento"]
            pelicula.estado = form.cleaned_data["estado"]
            pelicula.portada = form.cleaned_data["portada"]
            pelicula.sinopsis = form.cleaned_data["sinopsis"]
            pelicula.recaudacion = form.cleaned_data["recaudacion"]
            pelicula.donde_ver = form.cleaned_data["donde_ver"]
            pelicula.genero = form.cleaned_data["donde_ver"]
            pelicula.duracion = form.cleaned_data["duracion"]
            pelicula.save()

            context = {
                "mensaje" : "Película actualizada"
            }
            return render(request, "peliculas/actualizar_pelicula.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": PeliculasForm()
            }
            return render(request, "peliculas/actualizar_pelicula.html", context= context)

class BorrarPeliculasView(DeleteView):
    model = Peliculas
    template_name = "peliculas/borrar_peliculas.html"
    success_url = "/peliculas/listado-peliculas/"

