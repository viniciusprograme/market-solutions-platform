from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form): # Classe dedicada a Login (Usuário e senha)
    username = forms.CharField(label = "Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

class RegistroForm(UserCreationForm): # Classe para cadastro de usuários no sistema
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
