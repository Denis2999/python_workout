def filter_list(int_list):
    stdout = [i for i in int_list if type(i) == int]
    return stdout


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
