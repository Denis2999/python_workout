from functools import reduce


def some_def(some_list):
    for i in range(len(some_list) - 1):
        if some_list[i + 1] - some_list[i] != 1:
            return reduce(lambda a, b: a * b, some_list)
    return some_list[-1] + 1


print(some_def([1, 2, 3, 4, 5, 7]))
