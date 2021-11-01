def digital_root(n):
    # while n >= 10:
    #     x = [int(a) for a in str(n)]
    #     n = sum(x)
    #
    # return n
    # print(digital_root(sum(map(int, str(n)))))
    return n % 9 or n and 9


print(digital_root(901))
