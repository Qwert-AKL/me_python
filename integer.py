# """Тема урока: работа с целыми числами часть 1"""

# # a = 3
# # b = 2

# # print(a + b)
# # print(a - b)
# # # print(a * b)
# # # print(a / b)
# # s = 0
# # k = 30
# # d = k - 5
# # k = 2 * d
# # s = k - 100

# # # print(s)

# # first_number = int(input())
# # print(first_number)
# # second_number = first_number + 1
# # print(second_number)
# # three_number = second_number + 1
# # print(three_number)

# # first_number = int(input())
# # second_number = int(input())
# # three_number = int(input())
# # z = first_number + second_number + three_number
# # print(z)

# # Площадь куба
# # a = int(input())
# # s = 6 * a**2
# # v = a**3
# # print(f"Объем = {v}\nПлощадь полной поверхности = {s}")


# # # Значение функции
# # a = int(input())
# # b = int(input())
# # sum_1 = a + b
# # z = 3 *(sum_1**3) + 275 * b**2 - 127 * a - 41
# # print(z)

# # Следующее и предыдущее
# # a = int(input())
# # aplus = a + 1
# # aminus = a - 1
# # print(f"Следующее за числом {a} число: {aplus}\nДля числа {a} предыдущее число: {aminus}")

# # Стоимость покупки
# # monitor_ = int(input())
# # system_box_ = int(input())
# # Keyboard_ = int(input())
# # mouse_ = int(input())
# # pk = (monitor_ + mouse_ + system_box_ + Keyboard_) * 3
# # print(pk)

# # Арифметические операции
# # a = int(input())
# # b = int(input())
# # c1 = a + b
# # c2 = a - b
# # c3 = a * b
# # print(f'{a} + {b} = {c1}\n{a} - {b} = {c2}\n{a} * {b} = {c3}')

# # Арифметическая прогрессия
# # a = int(input())
# # d = int(input())
# # n = int(input())
# # an = a + d*(n - 1)
# # print(an)

# # Разделяй и властвуй
# # x = int(input())
# # print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep="---")

# """Тема урока: работа с целыми числами часть 1"""
# # ** - Возведение в степень
# # % - Остаток от деления
# # // - Целочисленное деление

# # Приоритет: (), **, -(унитарный минус), *,/,//,%,  +-

# # print(2 ** 0)
# # print(2 ** 1)
# # print(2 ** 2)
# # print(2 ** 3)
# # print(2 ** (-1))
# # print(2**(-2))
# # print((-3)**3)

# # print(2 ** 2 ** 3)
# # print(5 % 9)
# # print(5 // 9)
# # print(2%5)
# # print(-123//10)
# # print(18%12)
# # print(-10**2)
# # print(-10**3)
# # print((-10)**2)
# # # print((-10)**3)
# # a = 15 // (16 % 7)
# # b = 34 % a * 5 - 29 % 5 * 2
# # print(a + b)
# # a = 82 // 3**2 % 7
# # print(a)

# # # Геометрическая прогрессия
# # b1 = int(input())
# # q = int(input())
# # n = int(input())
# # bn=b1*q**(n-1)
# # print(bn)

# # # Расстояние в метрах
# # a = int(input())
# # a = a // 100
# # print(a)

# # Мандарины
# # n = int(input())
# # k = int(input())
# # man_1 = k // n
# # man_2 = k % n
# # print(man_1)
# # print(man_2)

# # # Сама неотвратимость
# # n = int(input())
# # survivor = n // 2 + n % 2
# # print(survivor)

# # Пересчёт временного интервала
# # minut = int(input())
# # timer_1 = minut // 60
# # timer_2 = minut % 60
# # print(f'{minut} мин - это {timer_1} час {timer_2} минут.')

# # Номер купе
# # n = int(input())
# # n = (n+3)//4
# # print(n)

# # Обработка цифр числа
# # последняя цифра числа определяется всегда как остаток
# # от деления числа на 10 (% 10). Чтобы отщепить последнюю цифру
# # от числа, необходимо разделить его нацело на 10 (// 10).

# #  Расчленёнка для цифры из двух чисел
# # num = 17
# # a = num % 10
# # b = num // 10
# # print(a)
# # print(b)

# #  Расчленёнка для цифры из трёх чисел
# # num = 754
# # a = num % 10
# # b = (num % 100) // 10
# # c = num // 100
# # print(a)
# # print(b)
# # print(c)

# # Алгоритм получения цифр n-значного числа

# # найти каждую цифру n-значного числа num:
# # num = 5337626
# # # #Последняя цифра
# # # numlast = (num % 10**1) // 10**0
# # # #Предпоследняя цифра
# # # numlast=(num%10**2)//10**1
# # # #Предпредпоследняя цифра:
# # # numlast=(num%10**3)//10**2
# # # Вторая цифра
# # n=7 # количество символов в цифре
# # numlast = (num % 10 ** (n - 1)) // 10 ** (n - 2)
# # # первая цифра
# # # numlast = (num % 10 ** n ) // 10 ** (n - 1)
# # print(numlast)

# # Определение число десятков  и единиц в двух значном числе
# # num = int(input())
# # last_item = num % 10
# # first_item = num // 10
# # print(f'число десятко {first_item} , число единиц {last_item}')

# # Число, образованное
# # при перестановке цифр двузначного числа.
# # num = int(input())
# # last_item = num % 10
# # first_item = num // 10
# # print(f'Сумма цифр: {last_item*10+first_item}')

# # Сумма цифр трёхзначного числа и произведение положительного числа
# # num = int(input())
# # num1 = num % 10
# # num2 = (num % 100) // 10
# # num3 = (num % 1000) // 100
# # print("Сумма цифр =", num1 + num2 + num3)
# # print("Произведение цифр =", num1 * num2 * num3)

# # Перестановка цифр вариант 1
# # num = int(input())
# # num1 = num % 10
# # num2 = (num % 100) // 10
# # num3 = (num % 1000) // 100
# # print("123=", num3, num2, num1, sep="")
# # print("132=", num3, num1, num2, sep="")
# # print("213=", num2, num3, num1, sep="")
# # print("231=", num2, num1, num3, sep="")
# # print("312=", num1, num3, num2, sep="")
# # print("321=", num1, num2, num3, sep="")

# # Перестановка цифр вариант 2
# # n = list(input())

# # for x in range( len(n)):
# # 	for y in range( len(n)):
# # 		for z in range( len(n)):
# # 			if x != y and x != z and z != y:
# # print(n[x] + n[y] + n[z])


# # Четырёхзначное число

# # num = int(input())
# # # Цифра в позиции единиц
# # num4 = (num % 10**1) // 10**0
# # # Цифра в позиции десятков
# # num3 = (num % 10**2) // 10**1
# # # Цифра в позиции сотен:
# # num2 = (num % 10**3) // 10**2
# # # Цифра в позиции тысяч
# # num1 = (num % 10**4) // 10**3
# # print("Цифра в позиции тысяч равна", num1)
# # print("Цифра в позиции сотен равна", num2)
# # print("Цифра в позиции десятков равна", num3)
# # print("Цифра в позиции единиц равна", num4)


# # % - Остаток от деления
# # // - Целочисленное деление
# n = int(input())
# num = n // 10000
# print("1=", num)
# num = n % 10000 // 1000
# print("2=", num)
# num = n % 1000 // 100
# print("3=", num)
# num = n % 100 // 10
# print('4=',num)
# num = n % 10
# print('5=',num)


# Принтит кубик из звёздочек
# print("*" * 17)
# print("*               *")
# print("*               *")
# print("*" * 17)

# Квадрат суммы  и сумма квадратов
# a = int(input())
# b = int(input())
# c = (a+b)**2
# print(f'Квадрат суммы {a} и {b} равен {c}')
# c = a**2+b**2
# print(f'Сумма квадратов {a} и {b} равна {c}')
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# c = a**b+c**d
# print(c)

# объединение строк
# n = int(input())
# n1 = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
# print(n1)

# # объединение строк
# n = str(input())
# print(f"{int(n) + int(str(n + n)) + int(str(n+n+n))}")


# оканчивается ли год с данным номером на два нуля.
# Последняя цифра
num = int(input())
numlast1 = (num % 10**2) // 10**1
numlast2 = (num % 10**1) // 10**0

if numlast1 == 0 and numlast2 == 0:
    print("YES")
else:
    print("NO")
# # # #Предпоследняя цифра
# # # numlast=(num%10**2)//10**1
