

# постепенная распаковка списка с вложеными значения (часть 1 без части 2 (((), [{(2, 'Urban', ('Urban2', 35))}])]))
# ((), [{(2, 'Urban', ('Urban2', 35))}])] лежит в другом файле
list1 = []
list2 = []
sum_tuple_1 = 0
int_1 = 0
sum_dict = 0
sum_str_1=0
massSUM=0

def data_structure(*args):
    global sum_tuple_1, int_1, sum_dict

    data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                      ((), [{(2, 'Urban', ('Urban2', 35))}])]
    for i in data_structure[0:len(data_structure)]:
        # print(i, type(i))
        if isinstance(i, list):  # int,tuple,bool,str,dict,list
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
            print('Изначальный тип индекса списка: ', i, type(i))
            list1.append(i)
            print(list1, type(list1))
            sum_list = sum(*list1)
            print('Итоговая сумма списка:', sum_list)

        if isinstance(i, dict):
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
            print(i, type(i))
            dict_1 = sum(list(i.values()))
            dict_2 = len(i.keys())
            # print(dict_2,type(dict_2))
            # print('Сумма значений словаря:', dict_1)
            # print('Сумма ключей словаря:', dict_2)
            sum_dict = dict_1 + dict_2
            print('Итоговая сумма по словарю:', sum_dict)

        if isinstance(i, tuple):
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
            if isinstance(data_structure[2], tuple):
                dictionary = data_structure[2]
                print(dictionary, type(dictionary))
                for k in dictionary:
                    if isinstance(k, int):
                        int_1 = k
                    if isinstance(k, dict):
                        # print(k, type(k))
                        dict_3 = sum(list(k.values()))
                        dict_4 = len(k.keys())
                        # print(dict_2,type(dict_2))
                        sum_dict = dict_3 + dict_4
            # print('Сумма чисел в кортеже:', int_1)
            # print('Сумма значений словаря:', dict_3)
            # print('Сумма ключей словаря:', dict_4)
            sum_tuple_1 = int_1 + sum_dict
            print('Итоговая сумма по кортежу: ', sum_tuple_1)
        if isinstance(i, str):  # int,tuple,bool,str,dict,list
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
            print('Изначальный тип индекса списка: ', len(i), type(i))
            sum_str_1=len(i)
            print('Итоговая сумма списка:', sum_str_1)
    massSUM=sum_list+sum_dict+sum_tuple_1+sum_str_1
    print("ОТВЕТ: ",sum_list,sum_dict,sum_tuple_1,sum_str_1)
    print(massSUM)

data_structure()
