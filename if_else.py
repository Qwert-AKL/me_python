# # # # # # """Условный оператор if-else"""
# # # # # # num1 = int(input())
# # # # # # num2 = int(input())

# # # # # # if num1 < num2:
# # # # # #     print(num1, "меньше чем", num2)
# # # # # # if num1 > num2:
# # # # # #     print(num1, "больше чем", num2)

# # # # # # if num1 == num2:  # используем двойное равенство
# # # # # #     print(num1, "равно", num2)
# # # # # # if num1 != num2:
# # # # # #     print(num1, "не равно", num2)


# # # # # # Цепочки сравнений
# # # # # # age = int(input())
# # # # # # if 3 <= age <= 6:
# # # # # #     print('Вы ребёнок')

# # # # # # проверяющий равенство трех переменных
# # # # # # a = input()
# # # # # # b = input()
# # # # # # c = input()
# # # # # # if a == b == c:
# # # # # #     print("числа равны")
# # # # # # else:
# # # # # #     print("числа не равны")

# # # # # ################
# # # # # # num = int(input())

# # # # # # last_digit = num % 10    # последняя цифра числа
# # # # # # first_digit = num // 10  # первая цифра числа

# # # # # # if last_digit == first_digit:
# # # # # #     print('ДА')
# # # # # # else:
# # # # # #     print('НЕТ')


# # # # # ###
# # # # # # num1, num2, num3 = int(input()), int(input()), int(input())

# # # # # # counter = 0  # переменная счётчик
# # # # # # if num1 % 2 == 0:
# # # # # #     counter = counter + 1  # увеличиваем счётчик на 1
# # # # # # if num2 % 2 == 0:
# # # # # #     counter = counter + 1  # увеличиваем счётчик на 1
# # # # # # if num3 % 2 == 0:
# # # # # #     counter = counter + 1  # увеличиваем счётчик на 1

# # # # # # print(counter)

# # # # # # Проверка пароля v1
# # # # # # a, b = input(), input()

# # # # # # if a == b:
# # # # # #     print("Пароль принят")
# # # # # # else:
# # # # # #     print("Пароль не принят")

# # # # # # Проверка пароля v2
# # # # # # s, p = input(), input()
# # # # # # print("Пароль ", (s != p) * "не ", "принят", sep="")

# # # # # # # Проверка пароля v3
# # # # # # print("Пароль принят" if input()==input() else "Пароль не принят")


# # # # # # Четное или нечетное? v1
# # # # # # s = int(input())
# # # # # # if s % 2 == 0:
# # # # # #     print("Четное")
# # # # # # else:
# # # # # #     print("Нечетное")

# # # # # # Четное или нечетное? v2 (через кортеж)
# # # # # # print(('Четное','Нечетное')[ int(input()) % 2 ])


# # # # # # # Соотношение v.1
# # # # # # s = str(input())
# # # # # # s_new1 = int(s[0]) + int(s[3])
# # # # # # s_new2 = int(s[1]) - int(s[2])
# # # # # # if s_new1 == s_new2:
# # # # # #     print("ДА")
# # # # # # else:
# # # # # #     print("НЕТ")

# # # # # # # Соотношение v.2 через цикл
# # # # # # a, b, c, d = [int(i) for i in input()]
# # # # # # print('ДА' if a + d == b - c else 'НЕТ')


# # # # # # Роскомнадзор 18 v1
# # # # # # current_date = int(2025)
# # # # # # # input_date = input()
# # # # # # year_ = int(input())
# # # # # # # month = input()
# # # # # # # num = input()
# # # # # # nadzor = current_date - year_
# # # # # # if nadzor >= 18:
# # # # # #     print("Доступ разрешен")
# # # # # # else:
# # # # # #     print("Доступ запрещен")

# # # # # # # Роскомнадзор 18 v2
# # # # # # print(f'Доступ {["разрешен", "запрещен"][int(input()) < 18]}')

# # # # # # # Роскомнадзор 18 v3
# # # # # # year_ = int(input())
# # # # # # if year_ >= 18:
# # # # # #     print("Доступ разрешен")
# # # # # # else:
# # # # # #     print("Доступ запрещен")

# # # # # # Проверка на Арифметическую прогрессию
# # # # # a = int(input())
# # # # # b = int(input())
# # # # # c = int(input())
# # # # # if a - b == -a and c - b == a or a - b == b and c - b == -b or a - b == b - c:
# # # # #     print("YES")
# # # # # else:
# # # # #     print("NO")

# # # # # # Проверка на Арифметическую прогрессию
# # # # # a, b, c = int(input()), int(input()), int(input())
# # # # # if b - a == c - b:
# # # # #     print("YES")
# # # # # else:
# # # # #     print("NO")

# # # # # # Проверка на Арифметическую прогрессию (деление по модулю)
# # # # # a, b, c = int(input()), int(input()), int(input())
# # # # # if c % b == a % b:
# # # # #     print("YES")
# # # # # else:
# # # # #     print("NO")

# # # # # # Проверка на Арифметическую прогрессию
# # # # # print("YES" if int(input()) - 2 * int(input()) == -int(input()) else "NO")

# # # # # Вывод наименшего числа v1
# # # # a, b = int(input()), int(input())
# # # # if a > b:
# # # #     print(b)
# # # # else:
# # # #     print(a)
# # # # # Вывод наименшего числа v2
# # # # print(min(int(input()), int(input())))


# # # # Наименьшее из четырёх чисел v1
# # # # a, b, c, d = int(input()), int(input()), int(input()), int(input())
# # # # if a < b < c < d:
# # # #     print(a)
# # # # if b < a < c < d:
# # # #     print(b)
# # # # if c < a < b < d:
# # # #     print(c)
# # # # if d < a < b < c:
# # # #     print(d)

# # # # # Наименьшее из четырёх чисел v2
# # # # print(min(int(input()), int(input()), int(input()), int(input())))


# # # # Возрастная группа v.1
# # # age = int(input())
# # # if age >= 60:
# # #     print("старость")
# # # if 25 <= age <= 59:
# # #     print("зрелость")
# # # if 14 <= age <= 24:
# # #     print("молодость")
# # # if 0 <= age <= 13:
# # #     print("детство")

# # # # Возрастная группа v.2
# # # n = int(input())
# # # print(
# # #     "старость"
# # #     if n > 59
# # #     else "зрелость" if n > 24 else "молодость" if n > 13 else "детство"
# # #


# # # Сумма положительныйх чисел +
# # # a, b, c = int(input()), int(input()), int(input())
# # # if a > 0 and b > 0:
# # #     sum = a + b
# # #     if c > 0:
# # #         sum = sum + c
# # #         print(sum)
# # #     else:
# # #         sum = sum
# # #         print(sum)
# # # if a < 0 and b > 0:
# # #     sum = b
# # #     if c > 0:
# # #         sum = sum + c
# # #         print(sum)
# # #     else:
# # #         sum = sum
# # #         print(sum)
# # # if a > 0 and b < 0:
# # #     sum = a
# # #     if c > 0:
# # #         sum = sum + c
# # #         print(sum)
# # #     else:
# # #         sum = sum
# # #         print(sum)
# # # if a < 0 and b < 0:
# # #     sum = 0
# # #     if c > 0:
# # #         sum = sum + c
# # #         print(sum)
# # #     else:
# # #         sum = sum
# # #         print(sum)
# # # if a < 0 and b < 0 and c < 0:
# # #     print("0")

# # # traffic_light_signal = input('Введите сигнал светофора: ')

# # # if traffic_light_signal == 'красный':
# # #     print('Стой!')
# # # elif traffic_light_signal == 'желтый':
# # #     print('Приготовься...')
# # # elif traffic_light_signal == 'зеленый':
# # #     print('Иди!')

# # # Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих.
# # #  Программа должна вывести одно из чисел:
# # # 3 (если все совпадают), #2 (если два совпадает) или  #0 (если все числа различны).

# # # a, b, c = int(input()), int(input()), int(input())

# # # if a == b == c:
# # #     print(3)
# # # elif a == b or b == c or a == c:
# # #     print(2)
# # # else:
# # #     print(0)

# # # Гонка спидстеров
# # # n, k = int(input()), int(input())
# # # if n>k:
# # #     print('NO')
# # # elif n<k:
# # #     print('YES')
# # # else:
# # #     print("Don't know")


# # # Вид треугольника
# # # a, b, c = int(input()), int(input()), int(input())
# # # if a == b == c:
# # #     print("Равносторонний")
# # # elif a == b and c<a and c<b:
# # #     print("Равнобедренный")
# # # elif b == c and a<b and a<c:
# # #     print("Равнобедренный")
# # # elif a == c and b<a and b<c:
# # #     print("Равнобедренный")
# # # elif a != b and b != c and c != a:
# # #     print("Разносторонний")

# # # Серединное число
# # # a, b, c = int(input()), int(input()), int(input())
# # # if b > a < c:
# # #     if b < c:
# # #         print(b)
# # #     elif b > c:
# # #         print(c)
# # # elif a > b < c:
# # #     if a < c:
# # #         print(a)
# # #     elif a > c:
# # #         print(c)
# # # elif a > c < b:
# # #     if a < b:
# # #         print(a)
# # #     elif a > b:
# # #         print(b)

# # # #Количество дней  v.1
# # # a = int(input())
# # # if a in [1,3,5,7,8,10,12]:
# # #     print('31')
# # # elif a in [4,6,9,11]:
# # #     print('30')
# # # elif a in [2]:
# # #     print('28')

# # # #Количество дней  v.2
# # # m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # # print(m[int(input())-1])

# # # # Церемония взвешивания v1
# # # a = int(input())
# # # if a in range(1, 60):
# # #     print("Легкий вес")
# # # elif a in range(60, 64):
# # #     print("Первый полусредний вес")
# # # elif a in range(64, 70):
# # #     print("Полусредний вес")

# # # # Церемония взвешивания v2
# # # weight = int(input())
# # # if weight < 60:
# # #     print("Легкий вес")
# # # elif 59 < weight < 64:
# # #     print("Первый полусредний вес")
# # # elif 63 < weight < 69:
# # #     print("Полусредний вес")

# # # Самописный калькулятор v.1
# # # a, b, c = int(input()), int(input()), str(input())
# # # if c == "+":
# # #     answer = a + b
# # #     print(answer)
# # # elif c == "-":
# # #     answer = a - b
# # #     print(answer)
# # # elif c == "*":
# # #     answer = a * b
# # #     print(answer)
# # # elif c == "/":
# # #     if b != 0:
# # #         answer = a / b
# # #         print(answer)
# # #     else:
# # #         print("На ноль делить нельзя!")
# # # else:
# # #     print("Неверная операция")


# # # Цветовой микшер v1
# # a, b = str(input()), str(input())
# # if a == "красный" or a == "синий" or a == "желтый":
# #     if b == "красный" or b == "синий" or b == "желтый":
# #         if a == b:
# #             print(a or b)
# #         elif (a == "красный" and b == "синий") or (b == "красный" and a == "синий"):
# #             print("фиолетовый")
# #         elif (a == "красный" and b == "желтый") or (b == "красный" and a == "желтый"):
# #             print("оранжевый")
# #         elif (a == "синий" and b == "желтый") or (b == "синий" and a == "желтый"):
# #             print("зеленый")
# #     else:
# #         print("ошибка цвета")
# #         pass
# # else:
# #     print("ошибка цвета")
# #     pass


# # # Цветовой микшер v2
# # c1, c2 = input(), input()
# # i = 0
# # if c1 == "красный":
# #     i = 1
# # elif c1 == "синий":
# #     i = 10
# # elif c1 == "желтый":
# #     i = 100

# # j = 0
# # if c2 == "красный":
# #     j = 1
# # elif c2 == "синий":
# #     j = 10
# # elif c2 == "желтый":
# #     j = 100

# # if i * j == 0:
# #     print("ошибка цвета")
# # else:
# #     if i == j:
# #         print(c1)
# #     elif i + j == 110:
# #         print("зеленый")
# #     elif i + j == 101:
# #         print("оранжевый")
# #     elif i + j == 11:
# #         print("фиолетовый")


# # Цвета колеса рулетки v.1
# pocket = int(input())
# if pocket in range(0, 37):
#     if pocket == 0:
#         print("зеленый")
#     elif pocket in range(1, 11):
#         if pocket % 2 == 0:
#             print("черный")
#         else:
#             print("красный")
#     elif pocket in range(11, 19):
#         if pocket % 2 == 0:
#             print("красный")
#         else:
#             print("черный")
#     elif pocket in range(19, 29):
#         if pocket % 2 == 0:
#             print("черный")
#         else:
#             print("красный")
#     elif pocket in range(29, 37):
#         if pocket % 2 == 0:
#             print("красный")
#         else:
#             print("черный")
# else:
#     print("ошибка ввода")

# # Цвета колеса рулетки v.2
#     n = int(input())
# print((['зеленый'] +
#        ['красный','черный'] * 5 +
#        ['черный','красный'] * 4 +
#        ['красный','черный'] * 5 +
#        ['черный','красный'] * 4) [n] if 0 <= n <= 36 else 'ошибка ввода')

# Пересечение отрезков v.1
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# else:
#     if a1 > a2:
#         a2 = a1
#     if b1 > b2:
#         b1 = b2
#     if a2 == b1:
#         print(a2)
#     else:
#         print(a2, b1)

# набо только девочек и возраст
# data1, data2 = int(input()), str(input())
# if data2=='f':
#     if 10<=data1<=15:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')


# Перевод чисел в арабские числа 1-10
# num=int(input())
# if num in range(1, 11):
#     if num==1:
#         num_arab="I"
#         print(num_arab) 
#     elif num==2:
#         num_arab="I"*num
#         print(num_arab)
#     elif num==3:
#         num_arab="I"*num
#         print(num_arab)    
#     elif num==4:
#         num_arab="I"+'V'
#         print(num_arab)
#     elif num==5:
#         num_arab='V'
#         print(num_arab)
#     elif num==6:
#         num_arab='V'+"I"
#         print(num_arab)
#     elif num==7:
#         num_arab='V'+"I"*2
#         print(num_arab)
#     elif num==8:
#         num_arab='V'+"I"*3
#         print(num_arab)
#     elif num==9:
#         num_arab="I"+'X'
#         print(num_arab)
#     elif num==10:
#         num_arab='X'
#         print(num_arab)           
# else:
#     print('ошибка') 


#проверка на чётность и не чётность
# num=int(input())
# if num%2==0:
#     if num in range(2, 5):
#         print('NO')
#     elif num in range(6, 21):
#         print('YES')
#     elif num>20:
#         print('NO')
# else:
#     print('YES')