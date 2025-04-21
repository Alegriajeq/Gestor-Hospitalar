from django import forms
from .models import Exame

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = '__all__'
