from rest_framework import serializers, viewsets
from django.conf import settings
from ..models import Produto, Categoria
from django.db import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nome','descricao')

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = Produto
        fields = ('categoria','subcategoria','produto')

    def create(self, validated_data):
        categorias_data = validated_data.pop('produto', None)
        categoria_list = []
        if categorias_data:
            for produtoData in categorias_data:
                categoria, created = Produto.objects.get_or_create(cateogoria=produtoData['categoria'])
                categoria_list.append(categoria)
        info_de_produto = Produto.objects.create(**validated_data)
        if categoria_list:
            info_de_produto.categoria.set(categoria_list)
        info_de_produto.save()
        return info_de_produto


    def update(self, instance, validated_data):
        categoria_data = validated_data.pop('categoria')
        categoria_list = []
        for tipoData in categoria_data:
            categoria, created = Categoria.objects.get_or_create(nome=tipoData['nome'])
            categoria_list.append(categoria)
        instance.categoria = validated_data['categoria']
        instance.subcategoria = validated_data['subcategoria']
        instance.produto = validated_data['produto']
        if categoria_list:
            instance.tipo.set(categoria_list)
        instance.save()
        return instance

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    #permission_classes = (AllowAny,)
