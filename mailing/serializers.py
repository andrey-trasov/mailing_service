from rest_framework import serializers

from mailing.functions import creating_recipients
from mailing.models import Mail, Mailing
from mailing.validators import list_recepient, checking_for_correctness


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ("recepient",)


class MailingSerializer(serializers.ModelSerializer):
    recepient = MailSerializer(many=True, write_only=True)

    class Meta:
        model = Mailing
        fields = ("id", "message", "delay", "recepient")

    def validate_recepient(self, value):
        """
        Валидирует поле recepient.
        - Проверяет что в получателе telegram всегда только числа
        - Проверяет что почта оформлена по общей маске почтового адреса
        """
        recepient = list_recepient(value[0]["recepient"])
        checking_for_correctness(recepient)

        return value

    def create(self, validated_data):
        mails_data = validated_data.pop("recepient")
        mailing = Mailing.objects.create(**validated_data)
        recepients = list_recepient(mails_data[0]["recepient"])
        creating_recipients(recepients, mailing)
        return mailing
