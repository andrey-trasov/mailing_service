from django.contrib import admin

from mailing.models import Mailing, Telegram, Mail, Logs


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "message")


@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ("id", "recepient")


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ("id", "recepient")


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ("id", "recepient", "message")
