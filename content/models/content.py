from django.db import models
from adminsortable.models import SortableMixin


class Content(SortableMixin):
    title = models.CharField('título', max_length=255)
    url = models.URLField('url do video')
    description = models.TextField('descrição')
    is_active = models.BooleanField('ativo', default=True)
    order = models.PositiveIntegerField('ordem', default=0, editable=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        ordering = ['order']
