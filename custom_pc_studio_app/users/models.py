from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    delivery_address = models.TextField(max_length=300, blank=True, null=True, verbose_name="Адрес доставки")

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username