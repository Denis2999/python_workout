def is_valid_walk(walk):
    if len(walk) == 10:
        dict = {"n": "s", "s": "n", "e": "w", "w": "e"}
        res = []
        for i in walk:
            if res and dict[i] == res[-1]:
                res.pop()
            else:
                res.append(i)
        for j in range(res.count("n")):
            res.remove("n")
            res.remove("s")

        return res
    return False


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # False
print(is_valid_walk(['n', 'w', 'e', 'n', 'w', 's', 'e', 'w', 's', 'e']))  # True
print(is_valid_walk(['n', 'n', 'n', 'w', 's', 's', 's', 's', 'e', 'n']))  # True
