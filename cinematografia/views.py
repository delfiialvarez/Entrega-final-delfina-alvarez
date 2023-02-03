from django.shortcuts import render

def index(request):
    return render(request, "index.html", context={})

def acerca_de(request):
    return render(request, "acerca_de.html", context={})