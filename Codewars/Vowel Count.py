def get_count(sentence):
    output = sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
    return output


print(get_count("Sample tests"))
