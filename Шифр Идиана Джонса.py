# Моя версия №1: не особо правильная
# import re
#
# while True:
#     num_1_cell = int(input('\nЗначение ячейки: '))
#     for i in range(-1, num_1_cell + 1):
#         for j in range(-1, num_1_cell + 1):
#             k = [i] + [j]
#             summa_index = sum(k)
#             if summa_index >= 0 and i > 0 and j > 0 and i != j and j != i and i < j and num_1_cell % summa_index == 0:
#                 num_2_cell = ''.join(str(k))
#                 s1 = re.sub("[^0-9]", "", num_2_cell)       #проверка на числа. так как список передаёт в строку вместе с символами ][и запятой.
#                 print(s1, end='')
# Моя версия №2: не особо правильная
# while True:
#     print("key generator")
#     num_1_cell = int(input('Введите значение первой ячейки: '))
#     num_2_cell = []
#     k = 0
#     for i in range(-1, num_1_cell + 1):
#         for j in range(-1, num_1_cell + 1):
#             k = [i] + [j]
#             summa_index = sum(k)
#             if summa_index >= 0 and i > 0 and j > 0 and i != j and j != i and i<j and num_1_cell % summa_index == 0:
#                 num_2_cell.append([i] + [j])
#     print('Пароль: ',*num_2_cell)

# Версия преподавателя
for k in range(3, 21):
    string = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                string += str(i) + str(j)
# Full Vision
# string += str(i) + '+' + str(j) + ' '
    print(k, '-', string)