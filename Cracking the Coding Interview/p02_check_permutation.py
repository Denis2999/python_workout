string_1 = "godh"
string_2 = "dog-"
test_cases = (
    ("dog", "god", True),
    ("abcd", "bacd", True),
    ("3563476", "7334566", True),
    ("wef34f", "wffe34", True),
    ("dogx", "godz", False),
    ("abcd", "d2cba", False),
    ("2354", "1234", False),
    ("dcw4f", "dcw5f", False),
    ("DOG", "dog", False),
    ("dog ", "dog", False),
    ("aaab", "bbba", False),
)


def is_it_permutation(some_string_1, some_string_2):
    if len(some_string_1) != len(some_string_2):
        return False
    if list(some_string_1) == list(some_string_2):
        return True
    return False


print(is_it_permutation(string_1, string_2))
