from django.db import models
from paciente.models import Paciente
from medicos.models import Medico

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.medico.nome} em {self.data} às {self.hora}"
