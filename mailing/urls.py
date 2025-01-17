from mailing.apps import MailingConfig
from mailing.views import MailingCreateApiView
from django.urls import path

app_name = MailingConfig.name


urlpatterns = [
    path("notify/", MailingCreateApiView.as_view(), name="mailing_create"),
]