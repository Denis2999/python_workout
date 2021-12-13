def duplicate_count(text):
    a = len([1 for i in set(text.lower()) if text.lower().count(i) > 1])
    # for i in set(text.lower()):
    #     if text.lower().count(i) > 1:
    #         a += 1
    return a


print(duplicate_count("abcdeaBabcdeaBabcdeaBabcdeaBabcdeaB"))
