"""Работа __new__:

'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент.
Он будет находиться под индексом 0 как единственный элемент кортежа.
second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы.
Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.

Передача данных из __new__ в __init__:
После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
В параметр first распакуется из args единственный аргумент 'data'.
В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
В параметр third распакуется значение под ключом с тем же названием из словаря kwargs."""

class Example:

  def __new__(cls, *args, **kwargs):

    print(args)

    print(kwargs)

    return object.__new__(cls)



  def __init__(self, first, second, third):

      print(first)
      print(second)
      print(third)



ex = Example('data', second=25, third=3.14)