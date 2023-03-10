# Generated by Django 4.1.5 on 2023-02-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('otchestvo', models.CharField(max_length=150, verbose_name='Отчество')),
                ('comment', models.TextField(max_length=300)),
            ],
        ),
    ]
