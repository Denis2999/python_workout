def digital_root(n):
    sum_x = 0
    while sum_x < 10:
        x = [int(a) for a in str(n)]
        sum_x = sum(x)
        print(sum_x)

    # return sum_x


print(digital_root(493193))
