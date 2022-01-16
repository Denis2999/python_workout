def disemvowel(string_):
    vowels = ["a", "o", "i", "e", "u", "A", "O", "I", "E", "U"]
    new_list = [i for i in string_ if i not in vowels]
    return "".join(new_list)


print(disemvowel("This website is for losers LOL!"))


# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")
