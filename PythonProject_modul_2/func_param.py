def printMax(a,b):
    if a>b:
        print(a,'максимально')
    elif a==b:
        print(a,'равно',b)
    else:
        print(b,'максимально')

a=input('Введите первое число: ')
b=input('Введите второе число: ')
printMax(a,b)