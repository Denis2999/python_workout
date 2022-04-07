def increment_string(strng):
    number = []
    for i in strng[::-1]:
        if i.isdigit():
            number.append(i)
        else:
            break

    # if len(number) == 0:
    #     return strng + "1"

    if len(number) != 0:
        some_num = str(int("".join(number[::-1])) + 1)
    else:
        return strng + "1"
    return strng[:-len(number)] + some_num.zfill(len(number))


print(increment_string("foo"))  # => "foo1"
print(increment_string("foobar001"))  # => "foobar002"
print(increment_string("foobar1"))  # => "foobar2"
print(increment_string("foobar00"))  # => "foobar01"
print(increment_string("foobar99"))  # => "foobar100"
print(increment_string("foobar099"))  # => "foobar100"
print(increment_string(""))  # => "1"
print(increment_string("M*&ej @2n28061330vU75386z^&]A5Pg43130000000005877277"))  # => "1"
# number = "001"
# print(number.zfill(len(number)))
