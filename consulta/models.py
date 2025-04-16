from django.db import models
from paciente.models import Paciente  # Certifique-se de usar o nome correto do app

from medicos.models import Medico

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateTimeField()
    status = models.CharField(max_length=50, default='Agendada')
