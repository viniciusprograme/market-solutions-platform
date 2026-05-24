from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FrequenciaForm
from .models import Frequencia

# Página para registrar frequência
@login_required
def registrar_frequencia(request):
    if request.method == "POST":
        form = FrequenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_frequencias")
    
    else:
        form = FrequenciaForm()
    return render(request, "frequencia/registrar.html", {"form": form})

# Página para listar todas as frequências
@login_required
def listar_frequencias(request):
    frequencias = Frequencia.objects.all().order_by("-data")
    return render(request, "frequencia/listar.html", {"frequencias": frequencias})

