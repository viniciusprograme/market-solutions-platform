from django.contrib import admin
from .models import Aluno, Disciplina, Frequencia

# Configuração para Aluno
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "contato") # colunas visíveis na lista
    search_fields = ("nome",) # campo de busca por nome

# Configuração para Disciplina
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

# Configuração para Frequencia
@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ("aluno", "disciplina", "data", "presente") # colunas visíveis
    list_filter = ("disciplina", "data", "presente") # filtros laterais
    search_fields = ("aluno__nome", "disciplina__nome") # busca por aluno ou disciplina