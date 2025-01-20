import requests

from django.core.mail import send_mail
from pytz import timezone
from celery import shared_task

from mailing.models import Mailing, Mail, Logs, Telegram
from django.utils import timezone

from myproject.settings import EMAIL_HOST_USER, TELEGRAM_TOKEN


def creating_logs(message, recepient, server_response):
    """
    Запиль логов о отправке сообщений
    """
    Logs.objects.create(
        message=message,
        sending_time=timezone.now(),
        recepient=recepient,
        server_response=server_response,
    )


def sending_messages_by_mail(mailing):
    """
    Отправка собщений по почте
    """
    recepients = Mail.objects.filter(mailing_id=mailing)
    for recepient in recepients:
        answer = send_mail(
            subject="У вас новой сообщениие!",  # тема письма
            message=f"{mailing.message}",  # сообщение
            from_email=EMAIL_HOST_USER,  # с какого мейла отправляем
            recipient_list=[
                f"{recepient.recepient}"
            ],  # список имейлов на которые отправляем
        )

        creating_logs(mailing.message, recepient.recepient, answer)


def sending_messages_by_telegram(mailing):
    """
    Отправка собщений в Telegram
    """
    recepients = Telegram.objects.filter(mailing_id=mailing)
    for recepient in recepients:

        params = {
            "text": f"{mailing.message}",
            "chat_id": f"{recepient.recepient}",
        }

        answer = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=params
        )

        creating_logs(mailing.message, recepient.recepient, answer)


@shared_task
def sending_messages():
    """
    проверяем сообшений для отправки
    """
    time = timezone.now()
    mailings = Mailing.objects.filter(sending_time__lt=time)
    for mailing in mailings:

        sending_messages_by_mail(mailing)  # отправка сообщений по почте
        sending_messages_by_telegram(mailing)  # отправка сообщений через телеграм

        mailing.delete()  # Удаление оправленных сообщений
