# def create_phone_number(n):
#     first_part_num = [str(i) for i in n[:3]]
#     second_part_num = [str(i) for i in n[3:6]]
#     third_part_num = [str(i) for i in n[6:10]]
#     return "({}) {}-{}".format("".join(first_part_num), "".join(second_part_num), "".join(third_part_num))

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
