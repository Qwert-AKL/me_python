def printMax(x, y):
    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами.'''
    x = int(x)
    y = int(y)
    if x > y:

        print(x, 'х наибольшее')
    elif x == y:

        print(x, 'равен', y)
    else:

        print(y, 'y наибольшее')


printMax(5, 100)
print(printMax.__doc__)
