from file_me.module_4.sortfunc import *
print("Ввод данных через пробел: ")
data_1=list(map(int,input().split()))
data_2=list(map(int,input().split()))
data_3=list(map(int,input().split()))
# input()- всегда строка.
# input().split() - метод с вводом с разделителем
# map(int,input().split()) - метод map(int,..... присваивает каждому элементу списка int, но выдаст карту
# map(int,input().split()) - метод map(int,..... присваивает каждому элементу списка int, добавляем list
# print(f'Вывод данных:',data_1)
bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)
print(f'Пузырьковая сортировка функции {bubble_sort.__name__}',data_1)
print(f'Пузырьковая сортировка функции {selection_sort.__name__}',data_2)
print(f'Пузырьковая сортировка функции {insertion_sort.__name__}',data_3)