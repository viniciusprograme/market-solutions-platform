from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AgendamentoForm
from .models import Agendamento

@login_required
def criar_agendamento(request): # View para criação de agendamento
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save() # Salva no banco usando o Model
            return redirect("listar_agendamentos") # Redireciona para a página listar_agendamentos
    else:
        form = AgendamentoForm()
    return render(request, "agenda/criar_agendamento.html", {"form": form}) # Renderiza a página de criação de agendamentos

@login_required
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, "agenda/listar_agendamentos.html", {"agendamentos": agendamentos}) # Renderiza a página que lista os agendamentos


# Create your views here.
