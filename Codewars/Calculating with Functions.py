def zero(operation=None):
    if not operation:
        return 0
    elif "+" == operation[0]:
        return 0 + operation[1]
    elif "-" == operation[0]:
        return 0 - operation[1]
    elif "*" == operation[0]:
        return 0 * operation[1]
    elif "//" == operation[0]:
        return 0 // operation[1]
    return 0


def one(operation=None):
    if not operation:
        return 1
    elif "+" == operation[0]:
        return 1 + operation[1]
    elif "-" == operation[0]:
        return 1 - operation[1]
    elif "*" == operation[0]:
        return 1 * operation[1]
    elif "//" == operation[0]:
        return 1 // operation[1]
    return 1


def two(operation=None):
    if not operation:
        return 2
    elif "+" == operation[0]:
        return 2 + operation[1]
    elif "-" == operation[0]:
        return 2 - operation[1]
    elif "*" == operation[0]:
        return 2 * operation[1]
    elif "//" == operation[0]:
        return 2 // operation[1]


def three(operation=None):
    if not operation:
        return 3
    elif "+" == operation[0]:
        return 3 + operation[1]
    elif "-" == operation[0]:
        return 3 - operation[1]
    elif "*" == operation[0]:
        return 3 * operation[1]
    elif "//" == operation[0]:
        return 3 // operation[1]


def four(operation=None):
    if not operation:
        return 4
    elif "+" == operation[0]:
        return 4 + operation[1]
    elif "-" == operation[0]:
        return 4 - operation[1]
    elif "*" == operation[0]:
        return 4 * operation[1]
    elif "//" == operation[0]:
        return 4 // operation[1]


def five(operation=None):
    if not operation:
        return 5
    elif "+" == operation[0]:
        return 5 + operation[1]
    elif "-" in operation[0]:
        return 5 - operation[1]
    elif "*" in operation[0]:
        return 5 * operation[1]
    elif "//" in operation[0]:
        return 5 // operation[1]


def six(operation=None):
    if not operation:
        return 6
    elif "+" == operation[0]:
        return 6 + operation[1]
    elif "-" == operation[0]:
        return 6 - operation[1]
    elif "*" == operation[0]:
        return 6 * operation[1]
    elif "//" == operation[0]:
        return 6 // operation[1]


def seven(operation=None):
    if not operation:
        return 7
    elif "+" == operation[0]:
        return 7 + operation[1]
    elif "-" == operation[0]:
        return 7 - operation[1]
    elif "*" == operation[0]:
        return 7 * operation[1]
    elif "//" == operation[0]:
        return 7 // operation[1]


def eight(operation=None):
    if not operation:
        return 8
    elif "+" == operation[0]:
        return 8 + operation[1]
    elif "-" == operation[0]:
        return 8 - operation[1]
    elif "*" == operation[0]:
        return 8 * operation[1]
    elif "//" == operation[0]:
        return 8 // operation[1]


def nine(operation=None):
    if not operation:
        return 9
    elif "+" == operation[0]:
        return 9 + operation[1]
    elif "-" == operation[0]:
        return 9 - operation[1]
    elif "*" == operation[0]:
        return 9 * operation[1]
    elif "//" == operation[0]:
        return 9 // operation[1]


def plus(number):
    return "+", number


def minus(number):
    return "-", number


def times(number):
    return "*", number


def divided_by(number):
    if number == 0:
        raise ValueError("Can not divided by zero")
    return "//", number


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
