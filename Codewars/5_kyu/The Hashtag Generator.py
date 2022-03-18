def generate_hashtag(s):
    if 0 < len(s) < 140:
        s = s.title().split()
        return "#" + "".join(s)
    return False


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
