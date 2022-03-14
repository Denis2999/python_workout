def get_middle(sentence):
    while len(sentence) > 2:
        sentence = sentence[1:-1]
    return sentence


# print(get_middle("test"))
# print(get_middle("testing"))
print(get_middle("fafncliuafcinpoa;bsfnc"))
print(get_middle("fafncliuafcinpoa;bsfncd"))

#
# sentence = "abfliaba" 
# print(sentence[1:-1])
