def zeros(n):
    factorial_counter = 0
    while n > 0:
        n //= 5
        print(n)
        factorial_counter += n
    return "########### ", factorial_counter

#
# print(zeros(6))  # 1
# print(zeros(12))  # 2
# print(zeros(30))  # 7
print(zeros(1000))  # 7
