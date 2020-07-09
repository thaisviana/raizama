from django.db import models
from django.conf import settings
from django.utils import timezone

class Produto (models.Model):

    CATEGORIA_CHOICE = [('AL','Alimento'),
                        ('CO','Cosmético'),
                        ('HI','Higiene'),
                        ('MO','Móveis'),
                        ('VE','Vestuaário')]
    categoria = models.ManyToManyField('Categoria',related_name='produto_categoria',blank=True)
    subcategoria = models.CharField (max_length= 40,blank=True)
    produto = models.CharField (max_length= 40,blank=True,null = True)
    data_criacao = models.DateTimeField(auto_now=True)

    def cadastrar(self):
        self.data_criacao = timezone.now
        self.save()

    def __str__(self):
        return self.produto

class Categoria (models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(null=True)

    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome


