import datetime
import smtplib

from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from main.models import Mailing, MailingLog


def write_to_log(something):
    with open('/home/emik/PycharmProjects/Cursovaya_6/test.txt', 'a') as file:
        file.write(f'{something}\n')


def update_mailing_status(mailing, current_datetime_round):
    try:
        write_to_log('попытка отправки')
        send_mail(
            subject=mailing.message.name,
            message=mailing.message.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.clients.all()],
            fail_silently=False
        )
        MailingLog.objects.create(mailing_time=current_datetime_round, status=True, response=None, mailing=mailing)
        write_to_log('отправлено успешно')
    except smtplib.SMTPException as e:
        MailingLog.objects.create(mailing_time=current_datetime_round, status=False, response=e, mailing=mailing)
        write_to_log('возникла ошибка')

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
    current_datetime = timezone.now()
    current_datetime_round = current_datetime.replace(second=0, microsecond=0)
    write_to_log(current_datetime)
    new_mailings = Mailing.objects.filter(first_mall__lte=current_datetime, status='created')
    write_to_log(new_mailings)
    for mailing in new_mailings:
        mailing.status = 'active'
        update_mailing_status(mailing, current_datetime_round)

    mailings = Mailing.objects.filter(next_mail__lte=current_datetime, status='active')
    write_to_log(mailings)
    for mailing in mailings:
        update_mailing_status(mailing, current_datetime_round)
