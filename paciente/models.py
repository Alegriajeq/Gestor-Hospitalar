from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    bi = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    alergias = models.TextField(blank=True, null=True)
    historico = models.TextField(null=False, blank=False)



  

    def __str__(self):
        return self.nome

