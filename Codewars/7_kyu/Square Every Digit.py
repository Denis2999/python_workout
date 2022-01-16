def square_digits(num):
    num = list(str(num))
    for key, value in enumerate(num):
        num[key] = int(value) ** 2
        num[key] = str(num[key])
    return int("".join(num))


print(square_digits(9119))


# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)