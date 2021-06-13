# High order functions
from functools import reduce


def use_reduce():
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda prev, curr: prev * curr, my_list)
    return all_multiplied


def use_map():
    my_list = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, my_list))
    return squares


def use_filter():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    return odd


def run():
    print(use_reduce())


if __name__ == '__main__':
    run()