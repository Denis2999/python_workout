def get_specific_sum(number):
    summ = number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number))
    return summ


print(get_specific_sum(10))
