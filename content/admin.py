from django.contrib import admin
from .models import Content, Organizacao, Tipo
from adminsortable.admin import SortableAdmin


class ContentAdmin(SortableAdmin):
    list_display = ('title', 'url', 'is_active', 'order')


admin.site.register(Content, ContentAdmin)
admin.site.register(Organizacao)
admin.site.register(Tipo)
