
# ОЧЕРЕДНАЯ ДИЧЬ, как не надо делать написана ниже(файл data_structure_2)
# сумарынй ответ не ясен с учётом первой части data_structure_1, получается ответ 100, но откуда берётся ещё 1 символ??
list1 = []
list2 = []
my_list_2=[]
sum_list1=0
sum_str_1=0
sum_ee=0
sum_last=0
nums_=0
nums=0
ee_last=0
# ОЧЕРЕДНАЯ ДИЧЬ, как не надо делать написана ниже(файл data_structure_2)
c=((), [{(2, 'Urban', ('Urban2', 35))}])
print(c,type(c))
for k in c:
    if isinstance(k, tuple):
        print('просто скобки',k)
        for s in c:
            if isinstance(s,list ):
                # print(s,type(s))
                list1.append(*s)
                # print('список',list1, type(list1))
                for j in list1:
                    # print(j,type(j))
                    if isinstance(j,set):
                        my_set = j
                        my_list = [item for item in my_set]
                        # print(my_list,type(my_list))
                        for q in my_list:
                            if isinstance(q, tuple):
                                for qq in my_list:
                                    if isinstance(qq,tuple):
                                        new_list_qq=list(qq)
                                        # print(new_list_qq,type(new_list_qq))
                                        for rr in new_list_qq:
                                            if isinstance(rr,int):
                                                sum_list1+=rr
                                                print('Cумма чисел в списке:',sum_list1)
                                            if isinstance(rr,str):
                                                sum_str_1=int(str(len(rr)))
                                                print('Длина строки:',sum_str_1,type(sum_str_1))
                                                print('=========================')
                                            if isinstance(rr,tuple):
                                                new_list_rr = list(rr)
                                                print(new_list_rr, type(new_list_rr))
                                                for ee in new_list_rr:
                                                    if isinstance(ee, str):
                                                        sum_ee = sum(map(str.isalpha, ee))
                                                        print(sum_ee)
                                                        import re
                                                        nums = re.findall(r'\d+', ee)
                                                        nums = [int(i) for i in nums]
                                                        nums_=int(str(*nums))
                                                        print(nums,type(nums))
                                                    if isinstance(ee, int):
                                                        ee_last=ee
                                                        print(ee)
                                            sum_last = int(sum_ee) + nums_ + int(ee_last) +int(sum_str_1)+int(sum_list1)
                                            print("ОТВЕТ",sum_last)

# a= {'a': 4, 'b': 5}
# print(a,type(a))
# print(len(a))
# a_new=sum(list(a.values()))
# print(len(a))
#
# print(a_new,type(a_new))


#
# b= (6, {'cube': 7, 'drum': 8})
# print(b,type(b))
# for k in b:
#     if isinstance(k, int):
#         print(k)
#     if isinstance(k,dict ):
#         print(k,type(k))
#         dict_1 = sum(list(k.values()))
#         dict_2 = len(k.keys())
#         # # print(dict_2,type(dict_2))
#         print('Сумма значений словаря:', dict_1)
#         print('Сумма ключей словаря:', dict_2)
#         sum_dict = dict_1 + dict_2
#         print('Сумма ключей словаря:', sum_dict)