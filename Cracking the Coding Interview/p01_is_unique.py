"""Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?"""

some_string = "abc+defghij_311111111111111111111111"


def is_some_string_too_long(text):
    if len(text) > 128:
        return True


first_string = list(some_string)
second_string = set(some_string)


# print(len(first_string) == len(second_string))
# print(set(some_string))
# print(list(some_string))


def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True


print(is_unique_chars_using_dictionary("asdfgczvb"))
