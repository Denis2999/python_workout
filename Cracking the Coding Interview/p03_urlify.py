some_string = "Mr John Smith   "


def replace_all_spaces(string):
    string = string.strip()
    list_string = list(string)
    new_string = ""
    for i in list_string:
        if i == " ":
            i = "%20"
        new_string += i
    return new_string


print(replace_all_spaces(some_string))

timer = 2345


def int_to_time(integer):
    if not 2359 >= integer >= 0:
        return False

    new_string = str(integer)
    for i in range(len(new_string), 2):
        print(i)


print(int_to_time(timer))
