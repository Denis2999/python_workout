s = input()
a = input()
b = input()


def bebe_with_baba(s, a, b):
    counter = 0
    for i in range(1000):
        if a in s:
            s = s.replace(a, b)
            counter += 1
            if counter == 1000:
                return "Impossible"
        else:
            return counter


print(bebe_with_baba(s, a, b))  # 2
# print(bebe_with_baba("abab", "ab", "ba"))  # 2
# print(bebe_with_baba("ababa", "a", "b"))  # 1
# print(bebe_with_baba("abab", "b", "a"))  # 1
# print(bebe_with_baba("abab", "c", "c"))  # 0
# print(bebe_with_baba("ababac", "c", "c"))  # Impossible
