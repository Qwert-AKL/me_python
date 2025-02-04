import math
from math import inf

def true_divide(first,second):
    try:
        div_true_divide = first / second
        print(f'При делении первого числа: {first} на второе: {second}\nОтвет: {div_true_divide}')
    except ZeroDivisionError:
        div_true_divide=inf
        print(f'При делении первого числа: {first} на второе: {second} \nОтвет: {div_true_divide}')
        return math.inf


# true_divide(1,26)
# true_divide(1,0)