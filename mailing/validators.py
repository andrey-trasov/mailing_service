import ast

from rest_framework.exceptions import ValidationError

def validity_error():
    raise ValidationError(
        f"Не правильный тип данных"
        f"Введите либо 1 получателя: 'string@gmail.com'"
        f"Либо несколько в списке: '['string@gmail.com', 'string@gmail.com']'"
    )


def list_recepient(recepient):
    """
    Возвращает список с получателями
    """
    # print(recepient)
    if recepient[0] == "[" and recepient[-1] == "]":  # проверка, передан список или 1 значение
        try:
            return ast.literal_eval(recepient)
        except:
            validity_error()

    elif not "[" in recepient and not "]" in recepient:
        try:
            return [recepient]
        except:
            validity_error()
    else:
        validity_error()

def checking_for_correctness(recepients):
    """
    Проверяет корректность получателей
    """
    for recepient in recepients:
        # print(recepient)
        if not "@" in recepient:
            if not recepient.isdigit():
                raise ValidationError(f"Получатель {recepient} не является почтой или id в telegram")



# {
#   "message": "string",
#   "delay": 0,
#   "recepient": [
#     {
#       "recepient": "['string@gmail.com', 'string@gmail.com', 'string@gmail.com', '123456789']"
#     }
#   ]
# }