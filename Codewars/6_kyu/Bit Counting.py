def count_bits(n=1234):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2

    return list(b).count("1")


print(count_bits())
