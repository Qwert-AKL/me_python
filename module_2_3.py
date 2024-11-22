# # # проба №7 (42, 69, 322, 13, 99)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
    elif my_list[a] < 0:
        continue
    else:
        break
    a += 1

# # # проба №6 (вывод только положительных кроме 9,8,7,5)
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# a = 0
# while a < len(my_list):
#     if my_list[a] > 0 and my_list[a] != 9 and my_list[a] != 8 and my_list[a] != 7 and my_list[
#         a] != 5:  # пока не решил как эту строчку сократить.
#         print(my_list[a])
#     a += 1

# #проба №5 (удаление/обрезка списка)
#
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# del my_list[6:len(my_list)]
# a = 0
# while a < len(my_list):
#     if my_list[a] > 0:
#         print(my_list[a])
#     a += 1


# # проба №4 (вывод только положительных и <=13)
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# a = 0
# while a < len(my_list):
#     if my_list[a] > 0 and my_list[a] >= 13:
#         print(my_list[a])
#     a += 1


# проба №1 (ручное управление по индексу)
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = my_list[4]
# print(index)
# if index == 0:
#     print('Чило не отрицательное и не положительное', index)
# elif index > 0:
#     print('Чило положительное', index)
# else:
#     print("Число отрицательное", index)

# #проба №2 (проверка на 0, на отриц. на положительные и выводит всё)
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# a = 0
# while a < len(my_list):
#     if my_list[a] == 0:
#         print(my_list[a],'Чило не отрицательное и не положительное')
#     elif my_list[a]> 0:
#         print(my_list[a],'Чило положительное')
#     else:
#         print(my_list[a],'Число отрицательное')
#     a +=1

# # проба №3 (Без проверки на 0 и отрицание, только выводит положительные из списка)
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# a = 0
# while a < len(my_list):
#     if my_list[a] > 0:
#         print(my_list[a], 'Чило положительное')
#     # elif my_list[a]== 0:
#     #     print(my_list[a],'Чило не отрицательное и не положительное')
#     # else:
#     #     print(my_list[a],'Число отрицательное')
#     a += 1
