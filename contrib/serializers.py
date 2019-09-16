from django.utils import six
from rest_framework.fields import CharField, ImageField


class LineBreakCharField(CharField):
    def to_representation(self, value):
        value = '<br/>'.join(value.splitlines())
        return six.text_type(value)


class ThumbnailerSerializerField(ImageField):
    def __init__(self, *args, **kwargs):
        self.format = kwargs.pop('format', '')
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            url = value.url
        except ValueError:
            return None
        url = value[self.format].url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url
