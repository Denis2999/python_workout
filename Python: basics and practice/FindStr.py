# some_text = "aaaaa"
# some_word = "a"
some_text, some_word = [input() for i in range(2)]


def find_str(text, word):
    register = 0
    for i in range(len(text)):
        if text[i:].startswith(word):
            register += 1
    return register


print(find_str(some_text, some_word))

# for i in range(len(some_text)):
#     print(some_text[i:])
