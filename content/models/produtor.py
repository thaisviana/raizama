from django.db import models
from django.conf import settings
from django.utils import timezone

class Produtor(models.Model):
    tipo = models.ManyToManyField(
        'Tipo', related_name='produtor_tipo', blank=True)
    nome = models.CharField(max_length=40, blank=True, null=True)
    razao_social = models.CharField(max_length=40)
    cnpj = models.CharField(max_length=40,blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)


    def cadastrar(self):
        self.data_criacao = timezone.now
        self.save()

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(null=True)

    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome