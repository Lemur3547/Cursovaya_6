# Generated by Django 5.0.6 on 2024-06-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_mall', models.DateTimeField(verbose_name='Дата и время первой отправки рассылки')),
                ('regularity', models.DurationField(verbose_name='Периодичность')),
                ('status', models.CharField(max_length=10, verbose_name='Статус рассылки')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Темя письма')),
                ('text', models.TextField(verbose_name='Письмо')),
            ],
        ),
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_mall', models.DateTimeField(verbose_name='Дата и время последней попытки')),
                ('status', models.BooleanField(verbose_name='статус попытки')),
                ('response', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ответ почтового сервера')),
            ],
        ),
    ]
