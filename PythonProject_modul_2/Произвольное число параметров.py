# #
# # def summator(text,*values,type='sum'):
# #     s=0
# #     for i in values:
# #         s+=i
# #     return f'{text} {s} {type}'
# #
# # print(summator("Сумма чисел: ", 2,4,5,6,7,8,9,100))
# # передача именнованных параметров
#
# def info(value, *types, name_='Kex',**values):
#     print('Тип', type(values))
#     print("Аргумент", values)
#     for key,value in values.items():
#         print(key,value)
#     print(type)
# info('Пример использования параметров всех типов',3,4,5,name="Lexus", course="Python")
#
#
#
def my_sum(n, *args, txt='Сумма чисел'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n  # **n степень
    print(txt + ':', s)


my_sum(1, 1,2,3,4,5)
my_sum(2, 1,2,3,4,5) #Сумма кубов