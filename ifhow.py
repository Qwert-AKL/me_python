# name =input('Введите ваше имя: ')
# if name == 'Urban' :  # if условие == (два знака равно) "Urban" : после двоеточия 4 пробела или табуляция.
#     print("Здравствуйте администратор ")
# if name == 'Алексей':
#         print("Здравствуйте администратор ")
# else:
#     print("Привет", name)

number = int(input('Введите число: '))  # fizz, BUZZ, FIzzBuzz
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:  # % (оператор остаток от деления) Если остаток от деления равен 0, то
    print('FiZZ')
elif number % 5 == 0:
    print("Buzz")
else:
    print('Число не делится на 3 или 5 без остатка')
# or (или)-не строгий оператор т.есть , and (и)-строгий оператор
