from django import forms
from .models import Frequencia

# Formulário para registrar frequência
class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ["aluno", "disciplina", "data", "presente"]
        widgets = {
            # Campo de data com formato brasileiro
            "data": forms.DateInput(
                format="%d/%m/%Y",
                attrs={"type": "date", "class": "form-control"}),
            "horario": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
        }

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Aceita datas no formato dd/mm/yyyy
    self.fields["data"].input_formats = ["%d/%m/%Y"]