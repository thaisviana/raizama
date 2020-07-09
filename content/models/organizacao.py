from django.db import models
from django.conf import settings
from django.utils import timezone

class Organizacao(models.Model):
    PEQUENO = 'PQ'
    MEDIO = 'MD'
    GRANDE = 'GD'
    GIGANTE = 'GG'
    TIPO_DE_PORTE_CHOICES = [
        (PEQUENO, 'Pequeno'),
        (MEDIO, 'Médio'),
        (GRANDE, 'Grande'),
        (GIGANTE, 'Gigante')
    ]
    tipo = models.ManyToManyField(
        'Tipo', related_name='organizacao_tipo', blank=True)
    subtipo = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=40, blank=True, null=True)
    razao_social = models.CharField(max_length=40)
    cnpj = models.CharField(max_length=40,blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tipo_de_porte = models.CharField(
        max_length=2,
        choices=TIPO_DE_PORTE_CHOICES,
        default=PEQUENO,
    )
    fins_lucrativos = models.BooleanField(default=True)
    transparencia_financeira = models.BooleanField(default=True)
    vinculo_com_grandes_corporacoes = models.BooleanField(default=True)
    vinculo_com_organizacoes_sociais = models.BooleanField(default=True)
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