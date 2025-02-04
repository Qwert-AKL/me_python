# a = [1, 1, 1]
# b = ''
# d = [1, 1, 1]
# c = d
# c[0] = 2
# print(c)
# print(d)
# print(id(a))
# print(id(d))
# print(id(c))
# print(c is d)
#
# # print(help(c))
#======================================#
# def helper():
#     """
#     Эта функция-помощник
#     """
#     pass
#
# print(helper.__doc__)


#======================================#
# локальные функции
def print_messages():
    # определение локальных функций
    def say_hello(): print("Привет, Вуася")

    def say_goodbye(): print("прощай")

    # вызов локальных функций
    say_hello()
    say_goodbye()


# Вызов функции print_messages
print_messages()
#======================================#

def main():
    say_hello()
    say_goodbye()


def say_hello():
    print("Hello")


def say_goodbye():
    print("Good Bye")


# Вызов функции main
main()


def print_person(name, *, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")


print_person("Bob", age=41, company="Microsoft")