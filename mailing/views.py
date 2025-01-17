from django.utils import timezone
from rest_framework.generics import CreateAPIView

from mailing.models import Mailing
from mailing.serializers import MailingSerializer
from myproject.settings import TIME_ZONE


class MailingCreateApiView(CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
       serializer.save(sending_time=timezone.now())

