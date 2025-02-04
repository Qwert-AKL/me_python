"""Домашняя работа по уроку "Специальные методы классов"""
"""Задача "Специальные методы классов"""


# Версия 1

class House:

    def __init__(self, name, number_of_floors,*value):
        self.name = name
        self.number_of_floors = number_of_floors
        self.value=value
        self.info()

    def info(self):
        if self.name == 'ЖК "Эльбрус"':
            print('-------------------------------------------------------')
            print(f'Добро пожаловать в {self.name}\n'
                  f'в жилищном комплексе <{self.number_of_floors}> этажей.')
            print('-------------------------------------------------------')
        elif self.name == 'ЖК "Акация"':
            print('-------------------------------------------------------')
            print(f'Добро пожаловать в {self.name}\n'
                  f'в жилищном комплексе <{self.number_of_floors}> этажей.')
            print('-------------------------------------------------------')

    def go_to(self, new_floor, start_):
        from random import randint
        self.start_ = randint(1, 20)

        if self.start_ < new_floor <= self.number_of_floors:
            print('Требуемый этаж', new_floor, 'Стартовый этаж', self.start_)
            for i in range(self.start_, new_floor + 1, 1):
                print(f'лифт поднялся на этаж №{i} c этажа №{self.start_}')
        elif new_floor < self.start_:
            print('Требуемый этаж', new_floor, 'Стартовый этаж', self.start_)
            for i in range(self.start_, new_floor - 1, -1):
                print(f'лифт опускается на этаж №{i}')
        elif new_floor > self.number_of_floors:
            print('Требуемый этаж', new_floor)
            print(f'Такого этажа нет. В доме <{self.number_of_floors}> этажей')
        elif 1 > new_floor:
            print('В подвал лифт не идёт')

    # def __len__(self):  # Возврат ко-во этажей через метод __len__
    #     return self.number_of_floors
    #
    def __str__(self): # Возврат ко-во этажей и названия через метод __str__
        return f'Название: <{self.name}>,кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):  # Сравнение количество этажей через метод __eq__
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # Сравнение < этажей через метод __lt__
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):  # Сравнение <= этажей через метод __le__
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self,value):
        if isinstance(value,int):
            self.number_of_floors+=value
            return self
    def __radd__(self,value):
        if isinstance(value, int):
            self.number_of_floors+=value
            return self
    def __iadd__(self,value):
        if isinstance(value, int):
            self.number_of_floors+=value
            return self


h1 = House('ЖК "Эльбрус"', 10)
h1.go_to(17, 0)

h2 = House('ЖК "Акация"', 10)
h2.go_to(7, 0)

# print(len(h1))  # Вывод количество этажей через метод __len__
# print(len(h2))  # Вывод количество этажей через метод __len__
# print('-----------------------------------')
# print(str(h1)) # Вывод количество этажей через метод __str__
# print(str(h2)) # Вывод количество этажей через метод __str__
# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=
print('-----------------------------------')
print('Сравнение методом __eq__ (==)', h1 == h2)
print('-----------------------------------')
print('Сравнение  этажей через метод __lt__ (<)', h1 < h2)
print('-----------------------------------')
print('Сравнение  этажей через метод __le__ (<=)', h1 <= h2)
print('-----------------------------------')
print('Сравнение  этажей через метод __gt__ (>)', h1 > h2)
print('-----------------------------------')
print('Сравнение  этажей через метод __ge__ (>=)', h1 >= h2)
print('-----------------------------------')
print('Сравнение  этажей через метод __ne__ (>=)', h1 != h2)
print('-----------------------------------')
h1=h1+1234    #__add__
print(h1)
h2 = 555 + h2 # __radd__
print(h2)
h1 += 111 # __iadd__
print(h1)


