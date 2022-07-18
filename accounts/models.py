from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ класс пользователя сайта """

    class Meta(AbstractUser.Meta):
        pass
