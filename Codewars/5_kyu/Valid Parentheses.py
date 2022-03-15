def valid_parentheses(some_inp):
    decision = 0
    for i in some_inp:
        if i == "(":
            decision += 1
        elif i == ")":
            decision -= 1

        if decision < 0:
            return False
    return decision == 0


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
