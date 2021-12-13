def persistence(n):
    b = 0
    while n >= 10:
        b += 1
        x = [int(i) for i in str(n)]
        a = 1
        for i in x:
            a *= i
        n = a
    return b


print(persistence(39))
