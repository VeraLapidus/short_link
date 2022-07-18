from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс CustomUser"""
    list_display = ('username', 'date_joined', 'last_login')
    list_filter = ('date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)


