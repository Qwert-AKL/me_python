"""Домашняя работа по уроку "Атрибуты и методы объекта"""
"""Задача "Developer - не только разработчик"""
# import random
from random import randrange
global number_of_floors_lift,numbers1
numbers1 = randrange(1,18, 1)
numbers2 = randrange(1, 2, 1)
class House:

    def __init__(self,name,number_of_floors,*number_of_floors_lift):
        self.name=name
        self.number_of_floors =number_of_floors
        number_of_floors_lift = numbers1
        self.number_of_floors_lift = number_of_floors_lift
        self.info()

    def info(self):
        if self.name=='ЖК "Горский"':
            print(f'Добро пожаловать в {self.name}, в жилищном комплексе {self.number_of_floors} этажей.')
            print(f'Вы находитесь на этаже №{self.number_of_floors_lift}')
            print(f'Нажмите кнопку этажа, на который хотите переместится')
        elif self.name=='"Домик в деревне"':
              if self.number_of_floors_lift<=2:
                print(f'Добро пожаловать в {self.name}, в домике {self.number_of_floors} этажа.')
                print(f'Вы находитесь на этаже №{self.number_of_floors_lift}')
                print(f'Нажмите кнопку этажа, на который хотите переместится')
              else:
                print(f'{self.name} выбран не существующий этаж, перемещение лифта не возможно')


    def go_to(self,new_floor):
        self.number_of_floors = new_floor
        # print(f'Лифт начинает перемещаться на этаж {new_floor}')
        if self.name=='ЖК "Горский"' and new_floor>numbers1:
            for i in range(numbers1, new_floor+1):print(f'Этаж №{i}')
            print(f'Вы прибыли на этаж №{new_floor}')
        if self.name=='ЖК "Горский"' and new_floor<numbers1:
            for i in range(numbers1,new_floor,-1): print(f'Этаж №{i}')
            print(f'Вы прибыли на этаж №{new_floor}')
        if self.name=='"Домик в деревне"' and new_floor<=numbers2:
            for i in range(numbers2,new_floor,-1): print(f'Этаж №{i}')
            print(f'Вы прибыли на этаж №{new_floor}')
        if self.name=='"Домик в деревне"' and new_floor>numbers2:
            user_input = input(f'в {self.name} всего два этажа. Достроить оперативно?(да/нет): ')
            if user_input.lower() == 'да' or 'д' or 'yes':
                print('Этаж(и) построен(ы), лифт продолжает движение к заданному этажу')
                for i in range(numbers2, new_floor, +1): print(f'Этаж №{i}')
                print(f'Вы прибыли на этаж №{new_floor}')
            elif user_input.lower() == 'нет' or 'н' or 'no':
                print(f'Вы выбрали не существующий №{new_floor}этажа')
            else:
                print('В ведите да/нет')



# number_of_floors_lift=randrange(1, len(number_of_floors), 1)
h1 = House('ЖК "Горский"', 18)
h1.go_to(8)
# h1.go_to(int(input()))
h2 = House('"Домик в деревне"', 2)
# h2.go_to(int(input()))
h2.go_to(5)


