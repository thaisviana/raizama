from rest_framework import serializers, viewsets
from django.conf import settings
from ..models import Produtor, Tipo
from django.db import models


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('nome','descricao')

class ProdutorSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = Produtor
        fields = ('tipo','nome','razao_social','cnpj','descricao')

    def create(self, validated_data):
        tipos_data = validated_data.pop('tipo', None)
        tipos_list = []
        if tipos_data:
            for tipoData in tipos_data:
                tipo, created = Tipo.objects.get_or_create(nome=tipoData['nome'])
                tipos_list.append(tipo)
        produtor =  Produtor.objects.create(**validated_data)
        if tipos_list:
            produtor.tipo.set(tipos_list)
        produtor.save()
        return produtor
    
    def update(self, instance, validated_data):
        tipos_data = validated_data.pop('tipo')
        tipos_list = []
        for tipoData in tipos_data:
            tipo, created = Tipo.objects.get_or_create(nome=tipoData['nome'])
            tipos_list.append(tipo)
        instance.descricao = validated_data['descricao']
        instace.nome = validated_data['nome']
        instance.razao_social = validated_data['razao_social']
        instance.cnpj = validated_data['cnpj']
        if tipos_list:
            instance.tipo.set(tipos_list)
        instance.save()
        return instance


class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    #permission_classes = (AllowAny,)

