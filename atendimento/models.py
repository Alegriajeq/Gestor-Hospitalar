from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    bi = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    alergias = models.TextField(blank=True, null=True)
    historico_medico = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
