def first_non_repeating_letter(string):
    string_lower = list(string.lower())
    string = list(string)
    for i in string_lower:
        if string_lower.count(i) == 1:
            return string[string_lower.index(i)]
    return ""


print(first_non_repeating_letter('Basic Tests'))
print(first_non_repeating_letter('sTreSS'))  # T
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))  # ,

