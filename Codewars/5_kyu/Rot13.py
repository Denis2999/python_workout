def rot13(text):
    stdout = ""
    for i in text:
        num_letter = ord(i)
        print(num_letter)

        capital = (num_letter & 32)
        print(capital)

        num_letter &= ~capital
        print(num_letter)


rot13("a")
