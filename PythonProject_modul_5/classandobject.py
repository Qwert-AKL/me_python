class Human:
    def __init__(self, name, age):  # метод __init__  - инициализация класса
        self.name = name  # определение характеристику.
        self.age = age
        self.say_info()  # вызов внутри

    def say_info(self):
        print(f'Привет, меня зовут {self.name},мне {self.age} годика')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения {self.age} годика')


# print(type(den))
# print(den.name,den.age,den.surname)
# print(max.name,max.age)
# den.say_info()
# max.say_info()

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} ушёл')

den = Human('Денис', 23)  # den- объект класс Human или Экземпляр класса
max = Human('Макс', 3)
# den.surname = "Чубака"
# del den
max.birthday()
print(len(den))
# del den