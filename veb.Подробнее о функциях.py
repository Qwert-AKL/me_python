import random
import names
def num_gem():
    return '+7'+''.join([str(random.randint(0,9)) for i in range(10)])


book = [[(names.get_full_name().num_gem()] for i in range(1000)]
print(book[:10])




# n=8*10**9
# c=0
# while n>1:
#     c+=1
#     print('Кол-во операция:',c,'Числа:',n)
#     n=n//2


