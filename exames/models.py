from django.db import models
from paciente.models import Paciente

class Exame(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_exame = models.CharField(max_length=100)
    data_exame = models.DateField() 
