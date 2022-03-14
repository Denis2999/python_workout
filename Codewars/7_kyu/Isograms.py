def is_isogram(string):
    set_string = set(string.lower())
    list_string = list(string.lower())
    for i in set_string:
        list_string.remove(i)
    return len(list_string) == 0



print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("noOse"))
print(is_isogram("isIsogram"))
