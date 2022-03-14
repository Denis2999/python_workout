def order(sentence):
    for i in sentence.split():
        if [1 - 9] in i:
            print(i)


print(order("4of Fo1r pe6ople g3ood th5e the2"))
