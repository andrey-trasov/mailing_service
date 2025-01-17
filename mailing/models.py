from django.db import models

class Mailing(models.Model):
    message = models.TextField(verbose_name="сообщение", max_length=1024)

    Delay = [
        (0, 0),    # - отправлять без задержки, при получении запроса
        (1, 1),    # - отправить с задержкой в 1 час
        (2, 2),    # - отправить с задержкой в 1 день
    ]

    delay = models.IntegerField(verbose_name="задержка отправки", choices=Delay)
    sending_time = models.DateTimeField(verbose_name="время отправки сообщения", null=True, blank=True)

    class Meta:
        verbose_name = "Почтовое сообщение"
        verbose_name_plural = "Почтовые сообщения"

    def __str__(self):
        return f"Почтовое сообщение: {self.message[:20]}..."


class Telegram(models.Model):
    recepient = models.CharField(verbose_name="id", max_length=11)
    mailing_id = models.ForeignKey(Mailing, verbose_name='рассылка', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Телеграм-пользователь"
        verbose_name_plural = "Телеграм-пользователи"

    def __str__(self):
        return f"Телеграм-пользователь: {self.recepient}"


class Mail(models.Model):
    recepient = models.CharField(verbose_name="почта", max_length=150)
    mailing_id = models.ForeignKey(Mailing, verbose_name='рассылка', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Почта пользователя"
        verbose_name_plural = "Почты пользователей"

    def __str__(self):
        return f"Почта пользователя: {self.recepient}"

class Logs(models.Model):
    message = models.TextField(verbose_name="сообщение", max_length=1024, null=True, blank=True)
    sending_time = models.DateTimeField(verbose_name="время отправки сообщения", null=True, blank=True)
    recepient = models.TextField(verbose_name="получатель", max_length=1024, null=True, blank=True)
    server_response = models.TextField(verbose_name="ответ сервера", max_length=1024, null=True, blank=True)

    class Meta:
        verbose_name = "Лог отправки"
        verbose_name_plural = "Логи отправки"

    def __str__(self):
        return f"Лог отправки: {self.message[:20]}..."


