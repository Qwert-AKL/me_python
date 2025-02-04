def total(a=10,*numbers,**phonebook):   #* - звездачка все аргументы собирает в кортеж
    print('a',a)                        #** -две звёздочи это все аргумены собираются в словарь
    for singel_items in numbers:            #проходит по всем элементам кортежа
        print('singel_items',singel_items)
    for first_part,second_part in phonebook.items():        #проходит по всем элементам словаря
        print(first_part,second_part)

print(total(10,1,2,5,Jack=1123,John=2231, Inge=1560))