# for i in 1,2,3,4:
#     print('i:=',i)
import random

# for i in 'Hello':
#     print('i:=',i)

# list_=['one','two','thee']
# for i in list_:
#     print('i:=',i)

# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
# print(list_)

# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     list_[i]='(^^,)'
#     print(list_[i])
#
# print(list_)

# list_ = ['one', 'two', 'three']
# list_2= [2,3,4,5,1]
# sum_=0
# for i in range(len(list_2)):
#     sum_+=list_2[i]
# print(sum_)

# # Таблица умножения
# for i in range(1, 11, 1):  # Start начало последовательности , СТОп конец последовательности, ШАГ
#     for j in range(1, 11):
#         print(f'{i}x{j}= {i * j}')

# # первый вариант
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i, dict_[i])

#     # Второй вариант через метод
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i, k in dict_.items():
#     print(i, k)
#обычная функция
# def say_hello():
#     print('Hello')
#
# say_hello()
# say_hello()
# say_hello()

# #Принемающая функция
# def say_hello(name):
#     print('Hello',name)
#
# say_hello('Anton')
# say_hello('MAX')
# say_hello('Lex')

# Возращающая фунция
# def lottery():
#     tikets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     win1 = random.choice(tikets)
#     win2 = random.choice(tikets)
#     return win1,win2
#
#
# win1 = lottery()
# win2 = lottery()
# print(win1,win2)


# import random
#
# def lottery(mon,thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(mon,thue)
#     return win1, win2
#
#
# win1, win2 = lottery('mon  ','thue  ')
# print(' ',win1,'  ',win2)

# import random
#
# def lottery(*args,**kwargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
#
# win1, win2 = lottery(1,2,3,4,5,6,7,8,9,10,11,12)
# print(' ',win1,'  ',win2)


def test(a=2,b=True):
    print(a,b)
test([1,2],'3')   #    *-РАСПАКОВКА СПИСКА, **- СЛОВАРЬ РАСПАКОВЫВАЕТСЯ