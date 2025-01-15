from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from mailing.models import Mailing
from mailing.serializers import MailingSerializer


# class MailingViewSet(viewsets.ModelViewSet):
#     queryset = Mailing.objects.all()
#     serializer_class = MailingSerializer

class MailingCreateApiView(CreateAPIView):
   queryset = Mailing.objects.all()
   serializer_class = MailingSerializer
