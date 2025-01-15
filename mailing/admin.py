from django.contrib import admin

from mailing.models import Mailing, Telegram, Mail


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
   list_filter = ("id", "message")

@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
   list_filter = ("id", "recepient")

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
   list_filter = ("id", "recepient")