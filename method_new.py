# print(int.__mro__)
# print(object)
class User:
    __instance = None

    def __new__(cls, *args, **kwargs):  # Метод Нью
        print('Я в new')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        # self.kwargs=kwargs
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, values in kwargs.items():  # Проегает по ключам
            setattr(self, key, values)  # и присваивает значение


other = [1, 2, 3]
user = {'name': 'Den', 'age': 25, 'gender': 'male'}

user1 = User(*other, **user)
print(user1.args)
print(user1.name)
print(user1.gender)
# user2 = User()
# print(id(user1),id(user2))
# print(user1 is user2)
# print(User.__mro__)
