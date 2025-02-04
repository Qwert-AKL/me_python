# def print_params(a, b, c=[]):
#     c.append(a + b)
#     print(c)
#
#
# print_params(3, 5)
# print_params(3, 5)
# print_params(3, 5)
#
#
# def print_params2(a, b, c=None):
#     if c is None:
#         c = []
#         c.append(a + b)
#     print(c)
#
#
# print_params2(3, 5)
# print_params2(3, 5)
# print_params2(2, 5)
#
#
# def print_params2(*params):# *args - упаковка/распаковка позиционных параментов, которые содержит 1 элемент (списков , картежей, множества)
#                           # **kwargs - запаковка распаковка Именнованный параметр - СЛОВАРь(элементы хранятся парами)
#     print(params)   # выдаёт картеж
#     print(*params)  # распаковывает картеж
# print_params2(1,2,3,4,5,6,7)
#
#
# def print_params3(a,b,c):
#                               # *args - упаковка/распаковка позиционных параментов, которые содержит 1 элемент (списков , картежей, множества)
#                               # **kwargs - запаковка распаковка Именнованный параметр - СЛОВАРь(элементы хранятся парами)
#     print(a,b,c)
# list_=[1,2,3]
# print_params3(list_,2,3)
# print_params3(*list_)


# def print_params4(a, b, c):
# # *args - упаковка/распаковка позиционных параментов, которые содержит 1 элемент (списков , картежей, множества)
# # **kwargs - запаковка распаковка Именнованный параметр - СЛОВАРь(элементы хранятся парами)
#     print(a, b, c)
#
# dict_={'a':1,'b':2,'c':3}       # словарь с ключами. Имена Ключей должны соотвествовать именам параметров функции
# print_params4(**dict_)

# def print_params4(**kwargs):
#     print(kwargs)
# dict_={'a':1,'b':2,'c':3}
# print_params4(**dict_)

def print_params4(**kwargs):
    for key in kwargs:
        print(key)
    for key, value in kwargs.items():
        print(key,value)
dict_={'a':1,'b':2,'c':3}
print_params4(**dict_)