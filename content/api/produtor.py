from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.conf import settings
from ..models import Produtor, Tipo


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class ProdutorSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(many=True)
    class Meta:
        model = Produtor
        fields = '__all__'


class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    #permission_classes = (AllowAny,)

