#1. Вызов функции с разными параметрами
def print_params(a=1,b='строка', c=True):
    print(a,b,c)
print_params(1,'строка', True)
print_params(1,'строка')
print_params(1)
print_params()
print_params(None,'строка')
print('|','~'*15,'|')
print_params(b=25)
print_params(c=[1,2,3])
print('|','~'*15,'|')
#2.
value_list = [4, 'pi-pi', True]
value_dict_ = {'a': 56, 'b': 'буквы', 'c': False}

print_params(*value_list)
print_params(**value_dict_)
print('|','~'*15,'|')

#3.
values_list_2=[54.32,'СТРОКА']
print_params(*values_list_2,42)

def append_to_list(item,list_my=None):
    if list_my is None:
        list_my=[]
        list_my.append(item)
    print(list_my)
append_to_list('Просто текст',)