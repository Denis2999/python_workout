def get_even_number(list_of_numbers):
    list_of_even_numbers = []
    for i in list_of_numbers:
        if i == 237:
            break
        elif i % 2 == 0:
            list_of_even_numbers.append(i)
    return list_of_even_numbers


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]

print(get_even_number(numbers))
