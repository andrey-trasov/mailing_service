# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from mailing.models import Mailing, Telegram, Mail
#
#
# class MailingTestCase(APITestCase):
#
#
#     def setUp(self):
#         """
#         создаем бд
#         """
#         self.mailing = Mailing.objects.create(message='Всем привет!', delay=0, sending_time='2025-01-20 18:00:57.598429+03')
#         self.telegram = Telegram.objects.create(recepient='12345678', mailing_id=self.mailing)
#         self.mail = Mail.objects.create(recepient='tests@gmail.com', mailing_id=self.mailing)
#
#
#     def test_create_mailing(self):
#         url = reverse('mailing:mailing_create')
#         data = {
#             "message": "string",
#             "delay": 0,
#             "recepient": [
#                 {
#                     "recepient": "['123456789', 'teat@gmail.com']"
#                 }
#             ]
#         }
#         response = self.client.post(url, data)
#
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
