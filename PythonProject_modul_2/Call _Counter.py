calls = 0


def count_calls():
    '''Счётчик вызова функций.'''

    global calls  # делаем возможным использование глобальной переменной
    calls += 1  # типо счётчик +1
print(count_calls.__doc__)                            #выводим значение сколько там насчитала вызовов функции.

def string_info(string):  # Функция string_info принимает аргумент - строку и возвращает кортеж из: #
                            # длины этой строки, строку в верхнем регистре, строку в нижнем регистре
                             # задание чтоб враг не догадался (реализовать логику работы по описанию.)
                                  # А просто написать не судьба. функция string_info и аргумент у неё (string)
    count_calls()  # тут просто вызываем функцию бла- бла: count_calls() и типо там должен сработать
                    # счётчик
    return len(string), string.upper(), string.lower()  # возврат длины строки, строки верхнего и нижнего регистра


print(string_info('Capybara'))          # выводим словечко, производится возврат: длины слова, выводит в верхнем и в нижнем регистре
print(string_info('ArmagedDon'))        # выводим словечко, производится возврат: длины слова, выводит в верхнем и в нижнем регистре


def is_contains(string, list_to_search):  # с двумя параметрами, то ли с двумя аргументами в задаче. А просто
                                            # фунция записывается is_contains с параметрами ,бла-бла (string,list_to_search)

    count_calls()                           # тут просто вызываем функцию бла- бла: count_calls() и типо там должен сработать
                                            # счётчик
    return string.upper() in [s.upper() for s in list_to_search]  # тут пробегается по списку и все буквы перегоняет в верхний регистр


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # ищем слово Urban в списке заданных и выдаст True
print(is_contains('Urban', ['recycling', 'cyclic']))  # ищем слово Urban в списке заданных и выдаст False, так нет в списке
print('Кол-во вызовов функций: ', calls)
