# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email') # Campos que se mostrarán en el formulario
