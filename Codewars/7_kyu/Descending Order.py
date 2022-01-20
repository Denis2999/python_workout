def descending_order(num):
    list_of_nums = [int(i) for i in list(str(num))]
    sorted_list_of_nums = sorted(list_of_nums)[::-1]
    list_to_return = [str(i) for i in sorted_list_of_nums]

    return int("".join(list_to_return))


print(descending_order(145263))
