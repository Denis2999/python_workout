def get_list(input_text):
    new_list = [int(i) for i in input_text.split(', ')]
    return new_list


def get_tuple(input_text):
    new_tuple = tuple(int(i) for i in input_text.split(', '))
    return new_tuple


print(get_list('12, 234, 34, 3, 86, 93, 3'))
print(get_tuple('12, 234, 34, 3, 86, 93, 3'))
