from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustom(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []#'avatar', 'telephone_number', 'country'
    phone = models.CharField(max_length=25, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='CustomUser/', verbose_name='аватарка')


