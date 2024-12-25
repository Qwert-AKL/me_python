# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список


# Максимум в списке
def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


# print(find_max([34,545,2,0,2334,24,5,234,4,43]))

# Подсчёт четных чисел в списке
def count_even(list_):
    conter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            conter += 1
    return conter

print(count_even([34, 545, 2, 0, 2334, 24, 5, 234, 4, 43]))

# Уникальный список

def unique(list_):
    new_list=[]
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(unique([34, 545, 2, 0, 2334,3,2,2,3,1,2,3,4,5,63]))
