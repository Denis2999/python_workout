def xo(s):
    s = list(s.lower())
    if "x" in s or "o" in s:
        return s.count("x") == s.count("o")
    return True


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
