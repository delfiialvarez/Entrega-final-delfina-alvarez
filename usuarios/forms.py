from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from usuarios.models import UserProfile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["phone", "birth_date", "profile_picture"]
   