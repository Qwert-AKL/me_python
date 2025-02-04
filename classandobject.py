class Human:
    head=True

    def __init__(self, name, age):  # метод __init__  - инициализация класса
        self.name = name  # определение характеристику.
        self.age = age
        self.say_info()  # вызов внутри

    def say_info(self):
        print(f'Привет, меня зовут {self.name},мне {self.age} годика')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения,мне теперь {self.age} годика')

    # print(type(den))
    # print(den.name,den.age,den.surname)
    # print(max.name,max.age)
    # den.say_info()
    # max.say_info()

    def __len__(self):
        return self.age

    def __lt__(self, other):  # операторы сравнение методом <
        return self.age < other.age

    def __gt__(self, other):  # операторы сравнение методом >
        return self.age > other.age

    def __eq__(self, other):  # операторы сравнение методом ==
        return self.name == other.name or self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __str__(self):
        return f'{self.name}'

    def __del__(self):
        print(f'{self.name} ушёл')


den = Human('Денис', 22)  # den- объект класс Human или Экземпляр класса
max = Human('Макс', 22)
# # den.surname = "Чубака"
# # del den
# # print(den < max)  # вывод сравнения зависит от следующего вызова функции
# # print(den > max)
# max.birthday()
# # print(den < max)  # вывод сравнения перезагрузка оператора сравнения <
# # print(den > max)  # вывод сравнения перезагрузка оператора сравнения >
# # print(den == max)  # вывод сравнения перезагрузка оператора сравнения ==
# # print('<bool>',den == max)  # вывод сравнения перезагрузка оператора сравнения bool
#
# # print(len(den))
# # del den
# print('вывод методом __str__', den)
a=6
print(Human.head)
