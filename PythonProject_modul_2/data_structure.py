# Сумматор символов в списке
def data_structure_summa(*list_):
    summa=0
    for index in list_:
        if isinstance(index, str):
            summa += len(index)
            # print(index,type(index))
        elif isinstance(index, int):
            summa += index
            # print(index, type(index))
        elif isinstance(index, list):
            summa += data_structure_summa(*index)
            # print(index, type(index))
        elif isinstance(index, tuple):
            summa += data_structure_summa(*index)
            # print(index, type(index))
        elif isinstance(index, set):
            summa += data_structure_summa(*index)
            # print(index, type(index))
        elif isinstance(index, dict):
            summa += data_structure_summa(*tuple(index.items()))
            # print(index, type(index))
    return summa
# data_structure=input()
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result=data_structure_summa(data_structure)
print(f'Сумма символов списка:\n{data_structure} \nравна {result}')