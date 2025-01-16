import ast

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mailing.functions import creating_recipients
from mailing.models import Mail, Mailing
from mailing.validators import list_recepient, checking_for_correctness


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('recepient',)


class MailingSerializer(serializers.ModelSerializer):
    recepient = MailSerializer(many=True, write_only=True)

    class Meta:
        model = Mailing
        fields = ('id', 'message', 'delay', 'recepient')
        # read_only_fields = ('id',)

    def validate_recepient(self, value):
        """
        Валидирует поле recepient.
        - Проверяет что в получателе telegram всегда только числа
        - Проверяет что почта оформлена по общей маске почтового адреса
        """
        # print(value)
        recepient = list_recepient(value[0]["recepient"])
        # print(recepient)
        checking_for_correctness(recepient)

        return value

    def create(self, validated_data):
        mails_data = validated_data.pop('recepient')
        # print(mails_data)
        mailing = Mailing.objects.create(**validated_data)

        recepients = list_recepient(mails_data[0]["recepient"])
        # print(recepients)

        creating_recipients(recepients, mailing)

        # for mail_data in mails_data:
        #     print(mail_data)


            # Mail.objects.create(mailing_id=mailing, **mail_data)
        return mailing


