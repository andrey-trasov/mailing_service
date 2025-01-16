from mailing.models import Mail, Telegram


def creating_recipients(recepients, mailing):
    """
    Создает список получателей из переданного словаря.
    """
    for recepient in recepients:
        if "@" in recepient:
            name_recepient = {'recepient': recepient}
            Mail.objects.create(mailing_id=mailing, **name_recepient)

        else:
            name_recepient = {'recepient': recepient}
            Telegram.objects.create(mailing_id=mailing, **name_recepient)



