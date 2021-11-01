def duplicate_count(text):
    text = text.lower()
    a = 0
    for i in set(text):
        print(i)
        if text.count(i) > 1:
            a +=1
    return a


print(duplicate_count("abcdeaBabcdeaBabcdeaBabcdeaBabcdeaB"))
