from django import forms

class PeliculasForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    director = forms.CharField(max_length=100)
    año_de_lanzamiento = forms.IntegerField()
    estado = forms.BooleanField(required=False)
    portada = forms.ImageField()
    sinopsis = forms.CharField(max_length=1000)
    recaudacion = forms.FloatField()
    donde_ver = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=100)
    duracion = forms.CharField(max_length=20)