def find_short(s):
    stdout = []
    for i in s.split():
        stdout.append(len(i))
    return min(stdout)


print(find_short("bitcoin take over the world maybe who knows perhaps"))
