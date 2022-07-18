from django.contrib import admin

from .models import ShortLink


class ShortLinkAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс ShortLink"""
    list_display = ('slug', 'date_created', 'user', 'full_link')
    list_filter = ('user',)

admin.site.register(ShortLink, ShortLinkAdmin)
