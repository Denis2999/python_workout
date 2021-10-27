def is_palindrome(input_string):
    formated_string = input_string.lower().replace(' ', '')

    palindrome = [i for i in reversed(formated_string)]

    if formated_string == ''.join(palindrome):
        return True

    return False


print(is_palindrome("cat o0 Otac"))
