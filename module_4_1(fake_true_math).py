import fake_math,true_math
from fake_math import fake_divide
from true_math import true_divide
print(f'Ответ {fake_math.fake_divide.__name__ }')
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
print('')
print(f'Ответ {true_math.true_divide.__name__ }')
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
