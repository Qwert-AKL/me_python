# Версия 3
a=''
b=''
suffix = ('.com','.ru','.net')
bansufix = ('.uk')
default_sender='university.help@gmail.com'

def send_email(message,recipient,sender='university.help@gmail.com'):
    global a, b,c
    a=recipient
    b=sender
    c=message
    print('\n',c,'\n')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

def check_recipient(recipient):
    global suffix,a
    for i in recipient:
        if '@' in recipient:
            if recipient.endswith(suffix):
                print(f'email получателя корректный: {recipient}')
                break
        else:
            print(f'email получателя некорректный: {recipient}')
            break
check_recipient(a)

def check_sender(sender):
    global suffix,bansufix, default_sender, a
    for i in sender:
        if '@' in sender:
            if sender.endswith(suffix) != sender.endswith(bansufix):
                if b == a:
                    print(f'email отправителя некорректный:{sender}\n'
                          f'Нельзя отправить письмо самому себе')
                    break
                else:
                    if sender == default_sender:
                        print(f'email отправителя корректный: {sender}')
                        break
                    else:
                        if sender.endswith(bansufix):
                            print(f'Невозможно отправить письмо с адреса {sender}, данный {bansufix} домен запрещён')
                            break
                        else:
                            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса : {sender} на адрес {a}')
                            break
            else:
                print(f'email отправителя некорректный: {sender}')
                break

check_sender(b)





#
# # Версия 2
# # просто флаги
# flag_a_r=0
# flag_b_r=0
# flag_a_s=0
# flag_b_s=0
# a=''
# b=''
# c=''
#
# def send_email(message,recipient,sender='university.help@gmail.com'):
#     global a,b,c
#     a=recipient
#     b=sender
#     c=message
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# # send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# #send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# # send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
#
# #Проверка получателя
# def check_recipient(recipient):
#     global flag_a_r, flag_b_r, flag_a_s, flag_b_s
#     for i in recipient:
#         if i == '@':
#             flag_a_r += 1
#             for x in recipient:
#                 if x == '.com' or '.ru' or '.net':
#                     flag_b_r += 1
#             # print(flag_a_r, flag_b_r)
#             print(f'email отправителя корректный: {recipient}')
# check_recipient(a)
#
# # #Проверка отравителя
# def check_sender(sender):
#     global flag_a_r, flag_b_r, flag_a_s, flag_b_s
#     for i in sender:
#         if i == '@':
#             flag_a_s += 1
#             for x in sender:
#                 if x == '.com' or '.ru' or '.net':
#                     flag_b_s += 1
#             # print(flag_a_s, flag_b_s)
#             print(f'email отправителя корректный: {sender}')
# check_sender(b)
#
# #проверка на совпадения
# def check_R_S(recipient, sender):
#
#     global flag_a_r, flag_b_r, flag_a_s, flag_b_s
#     # print(flag_a_r, flag_b_r, flag_a_s, flag_b_s)
#     if sender == recipient:
#         print(f'Нельзя отправить письмо самому себе!\nc {recipient} на {sender}')
#         print(f'Но если очень сильно нужно, то можно')
#     if flag_b_r and flag_b_s==0:
#         print('Невозможно отправить письмо с адреса ')
#     if flag_b_r and flag_b_s!=0 and b=='university.help@gmail.com':
#         print(f'Письмо успешно отправлено с адреса {b} на адресат {a}')
#     if flag_b_r and flag_b_s!=0 and b!='university.help@gmail.com':
#         print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {b} на адресат {a}')
# check_R_S(a,b)





# ### Версия №1 с ручным управлением
# def are_you_sure():
#     while True:
#         user_input = input(f'\nОтправить сообщение? по адресу: {sender} \n(yes/no): ')
#         if user_input.lower() in ["yes", "y"]:
#             print(f'Сообщение:\n{message}\nОТПРАВЛЕНО\n'
#                   f'Отправитель: {recipient}\n'
#                   f'Получатель: {sender}\n')
#             break
#         elif user_input.lower() in ["no", "n"]:
#             print("Сообщение НЕ ОТПРАВЛЕНО")
#             break
#         else:
#             print("Не путай буквы. Вводить yes/no.")
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
# message_text = None
#
#
# def ckeck_email(message=None, recipient=None, sender='university.help@gmail.com'):
#     global a, b, c
#
#
# print('\nВвведите получателя:\n')
# recipient = str(input())
# email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
# if re.match(email, recipient):
#     print(f'Корректный email получателя {recipient}\n')
#     a = True
#     print('Ввведите отправителя:\n')
#     sender = str(input())
#     if a == True and re.match(email, sender):
#         if sender != recipient:
#             b = True
#             print(f'Корректный email отправителя {sender}\n')
#             message = str(input('Введите сообщение для отправки: '))
#             c = True
#         elif a == True and re.match(email, sender) and sender == 'university.help@gmail.com':
#                 b = True
#                 print(f'Корректный стандартный email отправителя {sender}\n')
#                 message = str(input('Введите сообщение для отправки: '))
#                 c = True
#         else:
#             b = False
#             if sender != recipient:
#                 print(f'Некорректный email получателя {sender}\n')
#             else:
#                 if sender == recipient:
#                     print("Нельзя отправить письмо самому себе!\n")
# if a and b and c == True:
#     are_you_sure()
#
# else:
#     a = False
#     print(f'Некорректный email получателя {sender}\n')
#
# ckeck_email('Текст', " ", " ")
#
#
# # # print('\n')
# # # print('проверочные значения')
# # # print(a, 'получатель')
# # # print(b, 'отправитель')
# # # print(c, 'Нельзя отправить письмо самому себе')
