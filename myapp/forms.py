# myapp/forms.py
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'bi', 'data_nascimento', 'endereco', 'telefone', 'alergias', 'historico_medico']
