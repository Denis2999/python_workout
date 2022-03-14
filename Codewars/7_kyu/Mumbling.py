def accum(text):
    stdout_list = []
    counter = 0
    for i in text:
        stdout_list.append(i.upper() + i.lower() * counter + "-")
        counter += 1
    stdout = "".join(stdout_list)
    return stdout[0:-1]


print(accum("abcd"))
print(accum("NyffsGeyylB"))
