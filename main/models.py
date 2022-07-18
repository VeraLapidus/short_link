from django.conf import settings
from django.db import models


class ShortLink(models.Model):
    """ модель для сокращенния ссылки """

    full_link = models.URLField(unique=True, verbose_name='Полная ссылка в формате http://...')
    slug = models.CharField(max_length=28, unique=True, blank=True, verbose_name='Сокращенная ссылка')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата и время сокращения ссылки')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.full_link

