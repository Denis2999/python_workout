def alphabet_position(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    stdout = [alphabet.index(i) + 1 for i in text.lower() if i in alphabet]
    return " ".join(str(i) for i in stdout)


print(alphabet_position("The sunset sets at twelve o' clock."))
