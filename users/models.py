from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):
    """Модель пользователя"""
    username = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/', **NULLABLE)

    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.username:
            return self.username
        else:
            return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_block_users', 'Может блокировать пользователей',)
        ]

