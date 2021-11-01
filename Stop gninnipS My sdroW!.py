def spin_words(sentence):
    list_sentence = []

    # for i in list(sentence.split(" ")):
    #     if len(i) >= 5:
    #         list_sentence.append(i[::-1])
    #     else:
    #         list_sentence.append(i)
    # return ' '.join(list_sentence)

    return " ".join([i[::-1] if len(i) >= 5 else i for i in sentence.split(" ")])


print(spin_words("Hey fellow warriors"))
