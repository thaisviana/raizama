import uuid
import os

from django.utils.deconstruct import deconstructible


@deconstructible  # Necessary to allow django migrations
class UploadPath(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid1().hex, ext)
        return os.path.join(self.path, filename)