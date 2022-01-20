def is_palindrom(some_str):
    punctuation = (" ", ",", ".", "?", "!")
    new_str = [i for i in some_str.lower() if i not in punctuation]
    return new_str == new_str[::-1]


print(is_palindrom("А роза упала ,на лапу Азора,,,."))
print(is_palindrom("абба"))
