from django.contrib import admin
from .models import Content
from adminsortable.admin import SortableAdmin


class ContentAdmin(SortableAdmin):
    list_display = ('title', 'url', 'is_active', 'order')


admin.site.register(Content, ContentAdmin)
