from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        max_length=9,
        choices=CHOICES,
        default='user'
    )
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True
    )
    password = models.TextField(
        'Пароль',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
