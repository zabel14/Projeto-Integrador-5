from django.db import models

# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=255)

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=255)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

class Consulta(models.Model):
    data_consulta = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    celular_cliente = models.CharField(max_length=255)
    email_cliente = models.CharField(max_length=255)

