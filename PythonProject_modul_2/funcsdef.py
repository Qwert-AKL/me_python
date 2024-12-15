def print_params(a, b, c=[]):
    c.append(a + b)
    print(c)


print_params(3, 5)
print_params(3, 5)
print_params(3, 5)


def print_params2(a, b, c=None):
    if c is None:
        c = []
        c.append(a + b)
    print(c)


print_params2(3, 5)
print_params2(3, 5)
print_params2(2, 5)
