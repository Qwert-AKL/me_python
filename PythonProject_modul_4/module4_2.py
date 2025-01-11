def test_function():
    print(f'Это print из функиции {test_function.__name__.upper()}')
    def inner_function():
        print(f'Это print из функиции {inner_function.__name__.upper()}')
        text_ = f'Я в области видимости функции {test_function.__name__.upper()}'
        return print(text_)
    inner_function()
# inner_function('text_') # Не фурычит.вне зоны действия inner_function
test_function()

