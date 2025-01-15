from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateApiView

app_name = MailingConfig.name


urlpatterns = [
    path("mailing_create/", MailingCreateApiView.as_view(), name="mailing_create"),
    ]