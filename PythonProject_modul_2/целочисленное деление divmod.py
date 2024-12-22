def foo(a):
   return divmod(a, -11)

# Тесты
print(foo(22))
print(foo(-77))
print(foo(1))
## Или так
print('Второй вариант решения')
def foo(a):
   return a // -11, a % -11

# Тесты
print(foo(22))
print(foo(-77))
print(foo(1))