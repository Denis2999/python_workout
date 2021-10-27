def unique_list(list_of_numbers):
    return len(list_of_numbers) == len(set(list_of_numbers))


list_of_numbers_1 = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]

list_of_numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(unique_list(list_of_numbers_2))
