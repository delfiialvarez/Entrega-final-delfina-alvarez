from django.shortcuts import render
from django.views.generic import DeleteView

from series.models import Series
from series.forms import SeriesForm

def crear_series(request):
    if request.method == "GET":
        context = {
            "form": SeriesForm
        }
        return render(request, "series/crear_series.html", context=context)
    elif request.method == "POST":
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            Series.objects.create(
                nombre = form.cleaned_data["nombre"],
                cantidad_de_temporadas = form.cleaned_data["cantidad_de_temporadas"],
                director = form.cleaned_data["director"],
                genero = form.cleaned_data["genero"],
                estado = form.cleaned_data["estado"],
                donde_ver = form.cleaned_data["donde_ver"],
                sinopsis = form.cleaned_data["sinopsis"],
                portada = form.cleaned_data["portada"],
                año_de_lanzamiento = form.cleaned_data["año_de_lanzamiento"],
                estado_personal = form.cleaned_data["estado_personal"],
            )
            context = {
                "mensaje" : "Serie agregada exitosamente"
            }
            return render(request, "series/crear_series.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": SeriesForm()
            }
            return render(request, "series/crear_series.html", context=context)

def listar_series(request):
    if "search" in request.GET:
        series = Series.objects.filter(nombre__icontains = request.GET["search"])
    else:
        series = Series.objects.all()
    context = {
        "series": series,
    }
    return render(request, "series/listado_series.html", context=context)

def detalle_serie(request,pk):
    serie = Series.objects.get(id=pk)
    context= {
        "serie": serie
    }
    return render(request, "series/detalle_serie.html", context=context)

def actualizar_serie(request,pk):
    serie = Series.objects.get(id=pk)

    if request.method == "GET":
        context = {
            "form": SeriesForm(
                initial= {
                   "nombre": serie.nombre,
                   "director": serie.director,
                   "año_de_lanzamiento": serie.año_de_lanzamiento,
                   "estado": serie.estado,
                   "portada": serie.portada,
                   "sinopsis": serie.sinopsis,
                   "cantidad_de_temporadas": serie.cantidad_de_temporadas,
                   "donde_ver": serie.donde_ver,
                   "genero": serie.genero,
                   "estado_personal": serie.estado_personal,
                }
            )
        }
        return render(request, "series/actualizar_serie.html", context=context)
    elif request.method == "POST":
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            serie.nombre = form.cleaned_data["nombre"]
            serie.director = form.cleaned_data["director"]
            serie.año_de_lanzamiento = form.cleaned_data["año_de_lanzamiento"]
            serie.estado = form.cleaned_data["estado"]
            serie.portada = form.cleaned_data["portada"]
            serie.sinopsis = form.cleaned_data["sinopsis"]
            serie.cantidad_de_temporadas = form.cleaned_data["cantidad_de_temporadas"]
            serie.donde_ver = form.cleaned_data["donde_ver"]
            serie.genero = form.cleaned_data["donde_ver"]
            serie.estado_personal = form.cleaned_data["estado_personal"]
            serie.save()

            context = {
                "mensaje" : "serie actualizada"
            }
            return render(request, "series/actualizar_serie.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": SeriesForm()
            }
            return render(request, "series/actualizar_serie.html", context= context)

class BorrarSeriesView(DeleteView):
    model = Series
    template_name = "series/borrar_series.html"
    success_url = "/series/listar-series/"


