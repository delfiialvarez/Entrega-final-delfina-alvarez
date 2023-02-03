from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from usuarios.models import UserProfile
from usuarios.forms import RegisterForm, UserUpdateForm, UserProfileForm

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "usuarios/acceso.html", context=context)
    elif request.method == "POST":
        form = AuthenticationForm(request=request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                context= {
                    "mensaje": f"Bienvenido {user}"
                }
                return render(request, "index.html", context=context)
        form = AuthenticationForm()
        context= {
            "form": form,
            "errors": "Usuario o contraseña incorrecto"
        }
        return render(request, "usuarios/acceso.html", context=context)

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        context= {
            "form": form
        }
        return render(request, "usuarios/registro.html", context=context)
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect("acceso")
        context= {
            "errors": form.errors,
            "form": RegisterForm()
        }
        return render(request, "usuarios/registro.html", context=context)

@login_required
def update_user(request):
    user = request.user
    if request.method == "GET":
        form = UserUpdateForm(initial ={
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
        context = {
            "form": form 
        }
        return render(request, "usuarios/actualizar_usuario.html", context=context)
    elif request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get("username")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect("index")
        context = {
            "errors": form.errors,
            "form": UserUpdateForm()
        }
        return render(request, "usuarios/actualizar_usuario.html", context=context)

def update_user_profile(request):
    user= request.user
    if request.method == "GET":
        form = UserProfileForm(initial= {
            "phone": request.user.profile.phone,
            "birth_date":  request.user.profile.birth_date,
            "profile_picture": request.user.profile.profile_picture,
        })
        context= {
            "form": form
        }
        return render(request, "usuarios/actualizar_perfil.html", context=context)
    elif request.method =="POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get("phone")
            user.profile.birth_date = form.cleaned_data.get("birth_date")
            user.profile.profile_picture = form.cleaned_data.get("profile_picture")
            user.save()
            return redirect("index")
        context= {
            "errors": form.errors,
            "form": UserProfileForm()
        }
        return render(request, "usuarios/registro.html", context=context)

def user_detail(request,pk):
    user = User.objects.get(id=pk)
    context= {
        "user": user
    }
    users = UserProfile.objects.get(id=pk)
    context= {
        "user_1": users
    }
    return render(request, "usuarios/detalle_usuario.html", context=context)