
from django.db import models
from paciente.models import Paciente  # Certifique-se de que o nome 'paciente' esteja correto.
 # Adiciona a importação do modelo Paciente

class Exame(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_exame = models.CharField(max_length=100)
    data_agendamento = models.DateTimeField()
    resultado = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.tipo_exame} - {self.paciente.nome}'
