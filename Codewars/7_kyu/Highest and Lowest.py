def high_and_low(numbers):
    new_numbers = [int(i) for i in numbers.split(" ")]
    return "{} {}".format(max(new_numbers), min(new_numbers))


print(high_and_low("818 975 -545 -855 -909 -426 446 47 946 63 -89 486 -337 629 -730"))
