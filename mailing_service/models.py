from django.contrib.auth.models import AbstractUser
from django.db import models

class Client(models.Model):

    email = models.CharField(unique=True, max_length=100, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    otchestvo = models.CharField(max_length=150, verbose_name='Отчество')
    comment = models.TextField(max_length=300)

# class User(AbstractUser):


# class ScheldMailing:
#     start_of_mailing = models.DateTimeField(auto_now=True)
#     period_of_seq =
#     status =

class Mssg(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема')
    text = models.CharField(max_length=100, verbose_name='Текст')


