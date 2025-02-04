import re

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#  ^: начало строки.
#  [a-zA-Z0-9_.+-]+: любой набор букв, цифр, символов подчеркивания (_), точки (.), плюса (+), дефиса (-). Символ + означает "один или более символов".
#  @: символ "собака", который обязательно должен присутствовать в email.
#  [a-zA-Z0-9-]+: доменное имя, состоящее из букв, цифр или дефиса.
#  \.: символ точки. Поскольку точка — это специальный символ, её нужно экранировать с помощью \.
#  [a-zA-Z0-9-.]+: доменное расширение, содержащее буквы, цифры, точку или дефис.
#  $: конец строки

email = str(input(''))

if re.match(pattern, email):
    #re.match() в Python проверяет, соответствует ли начало строки заданному шаблону.
    # Если совпадение найдено, возвращается объект Match; если нет — None. 1


    print("Валидный email")
else:
    print("Невалидный email")

#
# import re
#
# a = None
# b = None
# c = None
#
# print('Шаблоны для проверки')
# print('university.help@gmail.com     urban.teacher@mail.ru   urban.fan@mail.ru    vasyok1337@gmail.com')
# recipient = ''
# sender = ''
#
#
# def ckeck_email(recipient, sender):
#     global a, b, c
#     print('\nВвведите получателя:\n')
#     recipient = str(input())
#     email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     if re.match(email, recipient):
#         print("Корректный email получателя", recipient)
#         a = True
#         print('Ввведите отправителя:\n')
#         sender = str(input())
#         if a == True and re.match(email, sender):
#             if sender != recipient:
#                 b = True
#                 print("Корректный email отправителя", sender)
#             else:
#                 b = False
#                 if sender != recipient:
#                     print("Некорректный email получателя", sender)
#                 else:
#                     if sender == recipient:
#                         print("Нельзя отправить письмо самому себе!")
#     else:
#         a = False
#         print("Некорректный email получателя", sender)