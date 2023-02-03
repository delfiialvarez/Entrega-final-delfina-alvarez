from django import forms

class SeriesForm(forms.Form):
    ESTADO_CHOICES = (
        ("En proceso", "En proceso"),
        ("Terminada", "Terminada"),
    )
    nombre = forms.CharField(max_length=150)
    cantidad_de_temporadas = forms.IntegerField()
    director = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=50)
    estado = forms.ChoiceField(choices=ESTADO_CHOICES)
    donde_ver = forms.CharField(max_length=100)
    sinopsis = forms.CharField(max_length=1000)
    portada = forms.ImageField()
    año_de_lanzamiento = forms.IntegerField()
    estado_personal = forms.BooleanField(required=False)