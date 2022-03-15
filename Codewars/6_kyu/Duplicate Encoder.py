def duplicate_encode(word):
    dict_word = {}
    for i in word.lower():
        if i in dict_word:
            dict_word[i] += 1
        else:
            dict_word[i] = 1

    # stdout = ""
    # for i in word.lower():
    #     if dict_word[i] > 1:
    #         stdout += ")"
    #     else:
    #         stdout += "("

    return "".join(("(" if dict_word[i] == 1 else ")") for i in dict_word)


# from collections import Counter
#
# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)   # Best practice
#     print(counter)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
