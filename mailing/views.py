from django.utils import timezone

from rest_framework.generics import CreateAPIView

from mailing.models import Mailing
from mailing.serializers import MailingSerializer

class MailingCreateApiView(CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        mailing = serializer.save()
        if mailing.delay == 0:
            time = timezone.now()
        elif mailing.delay == 1:
            time = timezone.now() + timezone.timedelta(hours=1)
        else:
            time = timezone.now() + timezone.timedelta(days=1)
        mailing.sending_time = time
        mailing.save()

