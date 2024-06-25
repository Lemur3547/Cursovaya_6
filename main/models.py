from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.CharField(max_length=255, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Темя письма')
    text = models.TextField(verbose_name='Письмо')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    first_mall = models.DateTimeField(verbose_name='Дата и время первой отправки рассылки')
    regularity = models.DurationField(verbose_name='Периодичность')
    status = models.CharField(max_length=10, verbose_name='Статус рассылки')
    clients = models.ManyToManyField(to=Client, verbose_name='Список клиентов')
    message = models.ForeignKey(to=Message, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'Рассылка №{self.pk}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLog(models.Model):
    last_mall = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.BooleanField(verbose_name='статус попытки')
    response = models.CharField(max_length=255, verbose_name='Ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(to=Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return f'Отчет к рассылке {self.mailing}'

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
