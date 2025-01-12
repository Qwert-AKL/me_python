# ПУЗЫРЬКОВАЯ СОРТИРОВКА
nums = [5, 6, 7, 83, 2, 3, 1]
# nums=list(input())
# print('вывод не сортированного списка:', nums)


def bubble_sort(ls):
    # чтобы код сработал хотя бы один раз, задаем значение True
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                # меняем значение переменной swapped для следующего повтора
                swapped = True


bubble_sort(nums)
# print(f'Вывод отсортированного списка по функции {bubble_sort.__name__} ', nums)

# СОРТИРОВКА ВЫБОРКОЙ
nums = [3, 2, 7, 500, 2, 2, 1]


def selection_sort(ls):
    # i - количество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальный первый элемент
        lowest = i
        # цикл для перебора неотсортированных элементов
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
                ls[i], ls[lowest] = ls[lowest], ls[i]


selection_sort(nums)
# print(f'Вывод отсортированного списка по функции {selection_sort.__name__}: ', nums)

# СОРТИРОВКА ВСТАВКОЙ
nums = [3, 1, 7, 300, 2, 4, 1]


def insertion_sort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i - 1
        while (j >= 0 and temp < ls[j]):
            ls[j + 1] = ls[j]
            j = j - 1
        ls[j + 1] = temp


insertion_sort(nums)
# print(f'Вывод отсортированного списка по функции {insertion_sort.__name__}: ', nums)
