# Крестики - Нолики
def check_winner():  # условия выйгрыша
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':  # диагональ
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':  # диагональ
        return 'X'


    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':  # диагональ
        return '0'
    if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':  # диагональ
        return '0'
    return '*'

def draw_area():
    for i in area:
        print("      ", *i)
    print()

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print(""" Добро пожаловать в игру!
    КРЕСТИКИ & НОЛИКИ""")
print(' -_-_-_-_-_-_-_-_-_-_-_-_')  # Верхний колонтитул
draw_area()
for turn in range(1,10):                # i - переенную просто так поменяли
    print(f'Ходит {turn}')
    if turn % 2 ==0:
        turn_char='0'
        print('Ходит нолик')
    else:
        turn_char = 'X'
        print('Ходит крестик')

    row=int(input('Введите номер стройки 1,2,3:  '))-1       #-1 для адаптации пользовательского ввода и номера строки в списках т.е 1 меняем на 0 по списку
    colum=int(input('Введите номер столбца 1,2,3:   '))-1
    if area[row][colum] =="*":                                # []-ряд  []-столбец  area[0][0] = ' X'
        area[row][colum] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        continue

    draw_area()

    if check_winner()=='X':
        print('Победа крестика!!!! ')
        break
    if check_winner() == '0':
        print('Победа нолика!!!! ')
        break
    if check_winner() == '*' and turn==9:
        print('Ничья!!!! ')
        break




