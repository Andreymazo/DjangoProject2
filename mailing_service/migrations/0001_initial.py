# Generated by Django 4.1.5 on 2023-01-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mssg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, verbose_name='Тема')),
                ('text', models.CharField(max_length=100, verbose_name='Текст')),
            ],
        ),
    ]
