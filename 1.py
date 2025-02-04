# for i in 1,2,3,4:
#     print('i:=',i)

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

#
# for i in range(1, 101, 1):  # Start начало последовательности , СТОп конец последовательности, ШАГ
#     for j in range(1, 11):
#         print(f'{i}x{j}= {i * j}')

# # первый вариант
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i, dict_[i])

# Второй вариант через метод
dict_ = {"a": 1, "b": 2, "c": 3}
for i, k in dict_.items():
    print(i, k)
