from rest_framework import serializers
from rest_framework.exceptions import ValidationError


# class RecepientValidator:
#     def __init__(self, field):
#        self.field = field
#
#
#     def __call__(self, value):
#         val = dict(value).get(self.field)
#         print(2)
#         print(val)
#         if isinstance(val, str):
#             print(12)



       # if val and "youtube.com" not in val:
       #     raise serializers.ValidationError('Некорректная ссылка. Ссылка должна содержать адрес youtube.com')

def validate_custom_method_field(value):
    print(9)
    print(value)
    if isinstance(value, str):
        raise ValidationError("Custom field must be a positive integer.")
        print(3)
    return value