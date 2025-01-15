from rest_framework.generics import CreateAPIView

from mailing.models import Mailing
from mailing.serializers import MailingSerializer


class  MailingCreateApiView(CreateAPIView):
   queryset = Mailing.objects.all()
   serializer_class = MailingSerializer

   def perform_create(self, serializer):
      del serializer.validated_data["recipient"]
      # print(serializer.data["recipient"])
      serializer.save()
      # print(1)

