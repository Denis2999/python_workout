def int_reverse(some_int):
    if some_int >= 0:
        return str(some_int)[::-1]
    else:
        some_int = -some_int
        some_int = int(str(some_int)[::-1])
        return -some_int


print(int_reverse(-123))
