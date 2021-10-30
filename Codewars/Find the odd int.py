def find_it(list_ints):
    for i in set(list_ints):
        if list_ints.count(i) % 2 != 0:
            return i


print(find_it([0, 1, 0, 1, 0]))
