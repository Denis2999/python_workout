import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt") as p:
    for i in p:
        try:
            secret = simplecrypt.decrypt(i, encrypted).decode("utf8")
        except simplecrypt.DecryptionException:
            pass

        print(secret)