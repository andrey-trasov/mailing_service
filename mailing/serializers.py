from rest_framework import serializers
from .models import Mailing

class MailingSerializer(serializers.ModelSerializer):
    recipient = serializers.CharField(required=True)

    class Meta:
        model = Mailing
        fields = ['id', 'message', 'delay', 'recipient']

    def validate_recipient(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Recipient must be a string.")
        return value