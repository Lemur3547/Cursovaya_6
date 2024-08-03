import datetime
import smtplib

from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from main.models import Mailing, MailingLog


def update_mailing_status(mailing, current_datetime_round):
    """Попытка рассылки сообщения"""
    try:
        send_mail(
            subject=mailing.message.name,
            message=mailing.message.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.clients.all()],
            fail_silently=False
        )
        MailingLog.objects.create(mailing_time=current_datetime_round, status=True, response=None, mailing=mailing,
                                  user=mailing.user)
    except smtplib.SMTPException as e:
        MailingLog.objects.create(mailing_time=current_datetime_round, status=False, response=e, mailing=mailing,
                                  user=mailing.user)

    # Обновление времени отправки последней рассылки и назначение времени следующей
    mailing.last_mall = current_datetime_round
    if mailing.regularity == 'day':
        mailing.next_mail = current_datetime_round + datetime.timedelta(days=1)
    elif mailing.regularity == 'week':
        mailing.next_mail = current_datetime_round + datetime.timedelta(days=7)
    elif mailing.regularity == 'month':
        mailing.next_mail = current_datetime_round + datetime.timedelta(days=30)
    else:
        pass
    mailing.save()


def time_check():
    """Получение списка рассылок, которые нужно разослать"""
    current_datetime = timezone.now()
    current_datetime_round = current_datetime.replace(second=0, microsecond=0)
    new_mailings = Mailing.objects.filter(first_mall__lte=current_datetime, status='created', is_active=True)
    for mailing in new_mailings:
        mailing.status = 'active'
        update_mailing_status(mailing, current_datetime_round)

    mailings = Mailing.objects.filter(next_mail__lte=current_datetime, status='active', is_active=True)
    for mailing in mailings:
        update_mailing_status(mailing, current_datetime_round)
