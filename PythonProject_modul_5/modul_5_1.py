"""Домашняя работа по уроку "Атрибуты и методы объекта"""
"""Задача "Developer - не только разработчик"""
# Версия 2

class House:

    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors
        self.info()


    def info(self):
        if self.name == 'ЖК "Горский"':
            print('-------------------------------------------------------')
            print(f'Добро пожаловать в {self.name}\n'
                  f'в жилищном комплексе {self.number_of_floors} этажей.')
            print('-------------------------------------------------------')
        elif self.name == '"Домик в деревне"':
            print('-------------------------------------------------------')
            print(f'Добро пожаловать в {self.name}\n'
                  f'в жилищном комплексе {self.number_of_floors} этажей.')
            print('-------------------------------------------------------')


    def go_to(self, new_floor,start_):
        from random import randint
        self.start_ = randint(1, 20)

        if self.start_ < new_floor <= self.number_of_floors:
            print('Требуемый этаж', new_floor, 'Стартовый этаж', self.start_)
            for i in range(self.start_,new_floor+1,1):
                print(f'лифт поднялся на этаж №{i} c этажа №{self.start_}')
        elif new_floor<self.start_:
            print('Требуемый этаж',new_floor,'Стартовый этаж',self.start_)
            for i in range(self.start_,new_floor-1,-1):
                print(f'лифт опускается на этаж №{i}')
        elif new_floor>self.number_of_floors:
            print('Требуемый этаж', new_floor)
            print(f'Такого этажа нет. В доме {self.number_of_floors} этажей')
        elif 1>new_floor:
            print('В подвал лифт не идёт')

h1 = House('ЖК "Горский"', 18)
h1.go_to(17,0)

h2 = House('"Домик в деревне"', 10)
h2.go_to(20,0)


# Версия 1 (не удачная, частично работает подъём спуск с рандомного этажа есть ошибка)
# from random import randrange
# global number_of_floors_lift, numbers1
#
# # Генерирует изначального случайный этаж нахождения:
# numbers1 = randrange(0, 18, 1)
# numbers2 = randrange(0, 10,1)
#
#
# class House:
#
#     def __init__(self, name, number_of_floors, *number_of_floors_lift):
#         self.name = name
#         self.number_of_floors = number_of_floors
#         number_of_floors_lift = numbers1
#         self.number_of_floors_lift = number_of_floors_lift
#         self.info()
#
#     def info(self):
#         if self.name == 'ЖК "Горский"':
#             print('-------------------------------------------------------')
#             print(f'Добро пожаловать в {self.name}\n'
#                   f'в жилищном комплексе {self.number_of_floors} этажей.')
#             print('-------------------------------------------------------')
#             print(f'Вы находитесь на этаже №{self.number_of_floors_lift}')
#             print(f'Вас переместят с этажа №{self.number_of_floors_lift} на заданный этаж')
#         elif self.name == '"Домик в деревне"':
#             while True:
#                 if self.number_of_floors_lift <= numbers2:
#                     print('-------------------------------------------------------')
#                     print(f'Добро пожаловать в {self.name}, в домике {self.number_of_floors} этажа.')
#                     if numbers2<=self.number_of_floors:
#                         print(f'Вы находитесь на этаже № {numbers2}')
#                         print(f'Вас переместят с этажа №{self.number_of_floors_lift} на заданный этаж')
#                         break
#                     elif numbers2>self.number_of_floors:
#                         print(f'Зачем Вам лифт, вы и так летаете в районе уровня {numbers2} этажа')
#                         break
#                     else:
#                         print(f'{self.name} выбран не существующий этаж, перемещение лифта не возможно')
#                         break
#
#     def go_to(self, new_floor):
#             self.number_of_floors = new_floor
#             # print(f'Лифт начинает перемещаться на этаж {new_floor}')
#
#             if self.name == 'ЖК "Горский"' and new_floor > numbers1:
#                 for i in range(numbers1, new_floor + 1): print(f'Этаж №{i}')
#                 print(f'Вы прибыли на этаж №{new_floor}')
#             if self.name == 'ЖК "Горский"' and new_floor < numbers1:
#                 for i in range(numbers1, new_floor, -1): print(f'Этаж №{i}')
#                 print(f'Вы прибыли на этаж №{new_floor}')
#
#             # if self.name == '"Домик в деревне"':
#             #     print("Этаж", numbers2)
#             #     if new_floor < numbers2:
#             #         for i in range(numbers2, new_floor, -1): print(f'Этаж №{i}')
#             #         print(f'Вы прибыли на этаж №{new_floor}')
#             #     elif new_floor > numbers2:
#             #         print(f'Вы выбрали не существующий №{new_floor} этаж(а)')
#                 # user_input = ''
#                 # while True:
#                 #     user_input = input(f'в {self.name} всего два этажа. Достроить оперативно?(да/нет): ')
#                 #     if user_input.lower() == 'да':
#                 #         print('Этаж(и) построен(ы), лифт продолжает движение к заданному этажу')
#                 #         for i in range(numbers2, new_floor, +1): print(f'Этаж №{i}')
#                 #         print(f'Вы прибыли на этаж №{new_floor}')
#                 #         break
#                 #     elif user_input.lower() == 'нет':
#                 #         print(f'Вы отказались надстраивать новые этажи')
#                 #         break
#                 #     else:
#                 #         print('Введите да/нет')
#
#
# # number_of_floors_lift=randrange(1, len(number_of_floors), 1)
# # h1 = House('ЖК "Горский"', 18)
# # h1.go_to(8)
# # h1.go_to(int(input()))
# h2 = House('"Домик в деревне"', 10)
#
# # h2.go_to(int(input()))
# h2.go_to(10)
