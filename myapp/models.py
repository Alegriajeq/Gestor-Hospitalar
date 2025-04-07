# myapp/models.py para cadastro do paciente
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    bi = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    alergias = models.TextField(blank=True)
    historico_medico = models.TextField(blank=True)

    def __str__(self):
        return self.nome
