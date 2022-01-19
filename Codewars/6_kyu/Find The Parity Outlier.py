def find_outlier(integers):
    even_numbers = [i for i in integers if i % 2 == 0]
    odd_numbers = [i for i in integers if i % 2 != 0]

    if len(even_numbers) < len(odd_numbers):
        return "{} (the only even number)".format(*even_numbers)
    else:
        return "{} (the only odd number)".format(*odd_numbers)


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
