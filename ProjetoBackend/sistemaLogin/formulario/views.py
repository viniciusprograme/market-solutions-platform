from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistroForm
from django.contrib.auth.models import Group

def login_view(request): # Função/View login, pelo qual será responsável acessar a página /home/
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # Autenticação baseado no nome de usuário e senha
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Se válido, vai realizar o login e redirecionar para /home/
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect("home") # Serve para redirecionar para a página inicial
            else:
                # Se não, mostrará a mensagem de erro
                messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()
    # Vai renderizar o template de login com o formulário
    return render(request, "formulario/login.html", {"form": form})

def logout_view(request): # Função/View de logout
    logout(request) # Encerra a seção do usuário
    return redirect('login') # Redireciona para /login/

def registro_view(request): # Função/View responsável pelo registro de usuários
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid(): # Criação de usuário a partir de um formulário
            user = form.save()
            grupo = Group.objects.get(name="Visitantes") # Coloca o usuário no grupo padrão (Visitantes)
            user.groups.add(grupo)
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect("login") # No fim, redireciona para o Login
    else:
        form = RegistroForm()
    # Renderiza o template de registro com o formulário
    return render(request, "formulario/registro.html", {"form": form})    

# View da página inicial, disponível apenas para usuários logados
@login_required
def home_view(request):
    # Se o usuário é um admin
    if request.user.groups.filter(name="Administradores").exists():
        return render(request, "formulario/home_admin.html") # Renderiza página exclusiva para admins
    else:
        return render(request, "formulario/home.html") # Se não renderiza a página de Home