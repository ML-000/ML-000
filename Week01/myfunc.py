import numpy as np

# Code -> reformat code
def print_hi(name):
    name = 'Hi, ' + name
    print(name)


def my_func(x):
    y = x
    return y


def myfuncv2(x):
    y = x
    # Refactor -> Extract -> Method
    y = new_method(y)
    return y


def new_method(y):
    y += 1
    y *= 2
    return y


if __name__ == '__main__':
    print_hi('PyCharm')
