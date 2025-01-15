from django.db import models

class Mailing(models.Model):
    message = models.TextField(verbose_name="название", max_length=1024)

    Delay = [
        (0, 0),    # - отправлять без задержки, при получении запроса
        (1, 1),    # - отправить с задержкой в 1 час
        (2, 2),    # - отправить с задержкой в 1 день
    ]

    delay = models.IntegerField(verbose_name="задержка отправки", choices=Delay)

    class Meta:
        verbose_name = "Почтовое сообщение"
        verbose_name_plural = "Почтовые сообщения"

    def __str__(self):
        return f"Почтовое сообщение: {self.message[:20]}..."


class Telegram(models.Model):
    user_id = models.CharField(verbose_name="id", max_length=11)
    mailing_id = models.ForeignKey(Mailing, verbose_name='рассылка', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Телеграм-пользователь"
        verbose_name_plural = "Телеграм-пользователи"

    def __str__(self):
        return f"Телеграм-пользователь: {self.user_id}"


class Mail(models.Model):
    mail = models.CharField(verbose_name="почта", max_length=150)
    mailing_id = models.ForeignKey(Mailing, verbose_name='рассылка', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Почта пользователя"
        verbose_name_plural = "Почты пользователей"

    def __str__(self):
        return f"Почта пользователя: {self.mail}"

# class Logs(models.Model):






