def to_jaden_case(string):
    stdout = [i.capitalize() for i in string.split()]
    return " ".join(stdout)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
