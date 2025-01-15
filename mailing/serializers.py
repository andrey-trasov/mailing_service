from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mailing.models import Mail, Mailing


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
        Валидирует поле mails.
        - проверяет что список не пустой
        - проверяет что каждый элемент списка является словарем с ключом 'mail'
        - проверяет что значение каждого ключа 'mail' является валидным email
        """
        if not value:
            raise ValidationError("Список получателей не может быть пустым.")



        return value

    def create(self, validated_data):
        mails_data = validated_data.pop('recepient')
        mailing = Mailing.objects.create(**validated_data)
        for mail_data in mails_data:
            Mail.objects.create(mailing_id=mailing, **mail_data)
        return mailing


