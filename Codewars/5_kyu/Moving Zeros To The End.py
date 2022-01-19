def move_zeros(array):
    counter_zero = array.count(0)
    a_list = [i for i in array if i != 0]
    a_list += [0] * counter_zero
    return a_list


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
