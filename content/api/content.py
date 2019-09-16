from rest_framework import serializers, viewsets
from ..models.content import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.filter(is_active=True)
    serializer_class = ContentSerializer
