class Human:
    def __init__(self,name):     # метод __init__  - инициализация класса
        self.name=name        # определение характеристику.

den = Human('Денис')  # den- объект класс Human или Экземпляр класса
max = Human('Макс')
print(type(den))
print(den.name,max.name)