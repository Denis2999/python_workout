def is_square(n):
    if n < 0:
        return False
    return n ** (1 / 2) % 1 == 0


print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))
print("###########################")
print(0 % 1 == 0)