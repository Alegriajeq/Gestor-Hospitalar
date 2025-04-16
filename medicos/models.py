# medicos/models.py

from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
