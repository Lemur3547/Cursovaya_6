from django.contrib import admin

from main.models import Mailing, Client, Message, MailingLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Регистрация модели клиента в админке"""
    fields = ('name', 'surname', 'patronymic', 'email', 'comment')
    list_display = ('name', 'surname', 'patronymic', 'email', 'comment')
    list_filter = ('name', 'surname', 'patronymic',)
    search_fields = ('name', 'surname', 'patronymic', 'comment',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Регистрация модели письма в админке"""
    list_display = ('name', 'text',)
    list_filter = ('name', 'text',)
    search_fields = ('name', 'text',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    """Регистрация модели рассылки в админке"""
    list_display = ('id', 'name', 'first_mall', 'regularity', 'status')
    list_filter = ('first_mall', 'regularity', 'status',)
    search_fields = ('name',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    """Регистрация модели отчета о рассылке в админке"""
    list_display = ('id', 'mailing', 'mailing_time', 'status', 'response')
    list_filter = ('mailing', 'mailing_time', 'status', 'response')
    search_fields = ('mailing', 'status', 'response')
