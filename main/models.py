from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.CharField(max_length=255, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Темя письма')
    text = models.TextField(verbose_name='Письмо')


class Mailing(models.Model):
    first_mall = models.DateTimeField(verbose_name='Дата и время первой отправки рассылки')
    regularity = models.DurationField(verbose_name='Периодичность')
    status = models.CharField(max_length=10, verbose_name='Статус рассылки')
    clients = models.ManyToManyField(to=Client, verbose_name='Список клиентов')
    message = models.ForeignKey(to=Message, on_delete=models.CASCADE, null=True)


class MailingLog(models.Model):
    last_mall = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.BooleanField(verbose_name='статус попытки')
    response = models.CharField(max_length=255, verbose_name='Ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(to=Mailing, on_delete=models.CASCADE)
