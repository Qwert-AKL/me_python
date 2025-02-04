# import this
#
# name = input("Введите имя:  ")
# if 5 > 1:
#     print("ок")
#     age = input()

while True:
    number = int(input('Введите число: '))
    if number % 2 == 0:
        print('Число чётное: ')
        # continue- пропускает последующие выполнение условий
    else:
        print('Чило нечетное: ')
        # break                          #break  - прерывает цикл
print('Я за циклом')
