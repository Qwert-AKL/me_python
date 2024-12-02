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

import re

while True:
    num_1_cell = int(input('\n Значение ячейки: '))
      for i in range(-1, num_1_cell + 1):
        for j in range(-1, num_1_cell + 1):
            k = [i] + [j]
            summa_index = sum(k)
            if summa_index >= 0 and i > 0 and j > 0 and i != j and j != i and i < j and num_1_cell % summa_index == 0:
                num_2_cell = ''.join(str(k))
                s1 = re.sub("[^0-9]", "", num_2_cell)       #проверка на числа. так как список передаёт в строку вместе с символами ][и запятой.
                print(s1, end='')