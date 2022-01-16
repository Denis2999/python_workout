def pig_it(text):
    pig_ret = ""
    for i in text.split(" "):
        text_list = list(i)
        if "?" in text_list:
            text_list.remove("?")
            text_list.append(text_list.pop(0))
            pig_ret += "".join(text_list) + "ay "
            return pig_ret + "?"

        elif "!" in text_list:
            text_list.remove("!")
            text_list.append(text_list.pop(0))
            pig_ret += "".join(text_list) + "ay "
            return pig_ret + "!"

        text_list.append(text_list.pop(0))
        pig_ret += "".join(text_list) + "ay "
    return pig_ret.rstrip()


print(pig_it('Pig latin is cool'))
# print(pig_it(''))
