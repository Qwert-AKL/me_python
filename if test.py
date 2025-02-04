######## ########

######## ########
# while True:
#     a=input('Введите первое число для сравнеия: ')
#     b=input('Введите второе число для сравнеия: ')
#     if a==b:
#         print(a,'=',b)
#     elif a<b or b<a:
#         if a<b:
#             print(a,'<',b)
#         elif a>b:
#             print(a,'>',b)
#         continue

######## ########

######## ########
sale1 = 0.05  # 5 %
sale2 = 0.12  # 12%
sale3 = 0.20  # 20%
sale4 = 0.30  # 30%
while True:
    prise = int(input('Введите цену товара/услуги: '))
    if prise >= 0 and prise <= 5000:
        new_prise = prise - (prise * sale1)
        print('Cтоимость составит с учётом скидки 5%',new_prise)
    elif prise > 5000 and prise <= 15000:
        new_prise = prise - (prise * sale2)
        print('Cтоимость составит с учётом скидки 12%', new_prise)
    elif prise > 15000 and prise <= 25000:
        new_prise = prise - (prise * sale3)
        print('Cтоимость составит с учётом скидки 20%', new_prise)
    elif prise > 25000 :
        new_prise = prise - (prise * sale4)
        print('Cтоимость составит с учётом скидки 20%', new_prise)
    continue