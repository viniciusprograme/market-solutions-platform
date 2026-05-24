from django.db import models
from django.contrib.auth.models import User

# Disciplina cultural (ex.: Capoeira, Canto)
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Aluno matriculado nas disciplinas
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    contato = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

# Registro de frequência (presença/ausência)
class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} ({self.data})"


