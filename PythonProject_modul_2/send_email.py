def are_you_sure():
    while True:
        user_input = input(f'\nОтправить сообщение? по адресу: {sender} \n(yes/no): ')
        if user_input.lower() in ["yes", "y"]:
            print(f'Сообщение:\n{message}\nОТПРАВЛЕНО\n'
                  f'Отправитель: {recipient}\n'
                  f'Получатель: {sender}\n')
            break
        elif user_input.lower() in ["no", "n"]:
            print("Сообщение НЕ ОТПРАВЛЕНО")
            break
        else:
            print("Не путай буквы. Вводить yes/no.")

import re

a = None
b = None
c = None

print('Шаблоны для проверки')
print('university.help@gmail.com     urban.teacher@mail.ru   urban.fan@mail.ru    vasyok1337@gmail.com')
recipient = ''
sender = ''
message_text = None


def ckeck_email(message=None, recipient=None, sender='university.help@gmail.com'):
    global a, b, c


print('\nВвведите получателя:\n')
recipient = str(input())
email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
if re.match(email, recipient):
    print(f'Корректный email получателя {recipient}\n')
    a = True
    print('Ввведите отправителя:\n')
    sender = str(input())
    if a == True and re.match(email, sender):
        if sender != recipient:
            b = True
            print(f'Корректный email отправителя {sender}\n')
            message = str(input('Введите сообщение для отправки: '))
            c = True
        elif a == True and re.match(email, sender) and sender == 'university.help@gmail.com':
                b = True
                print(f'Корректный стандартный email отправителя {sender}\n')
                message = str(input('Введите сообщение для отправки: '))
                c = True
        else:
            b = False
            if sender != recipient:
                print(f'Некорректный email получателя {sender}\n')
            else:
                if sender == recipient:
                    print("Нельзя отправить письмо самому себе!\n")
if a and b and c == True:
    are_you_sure()

else:
    a = False
    print(f'Некорректный email получателя {sender}\n')

ckeck_email('Текст', " ", " ")

# def send_email(message, *recipient, sender = 'university.help@gmail.com'):
#     global a, b, c
#     if a and b==True and sender=='university.help@gmail.com':
#         print(f'Письмо успешно отправлено с адреса {sender}  на адрес {recipient}')
#
#
#
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.fan@mail.ru')
# #
# # print('\n')
# # print('проверочные значения')
# # print(a, 'получатель')
# # print(b, 'отправитель')
# # print(c, 'Нельзя отправить письмо самому себе')
