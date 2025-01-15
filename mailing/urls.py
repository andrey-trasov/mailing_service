# from django.urls import path, include
# from rest_framework import routers
#
# from mailing.views import MailingViewSet
#
# router = routers.DefaultRouter()
# router.register(r'mailings', MailingViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from mailing.apps import MailingConfig
from mailing.views import MailingCreateApiView
from django.urls import path

app_name = MailingConfig.name


urlpatterns = [
    path("mailing_create/", MailingCreateApiView.as_view(), name="mailing_create"),
]