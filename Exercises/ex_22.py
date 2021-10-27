import collections
import string

SOME_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing lorem lorem lorem lorem elit. Cras semper nisl sed scelerisque porta. Sed consequat eget quam ut molestie. Donec id condimentum erat."


def most_common_word(text):
    text = ''.join(x for x in text if x not in set(string.punctuation))
    text = text.split(' ')
    return collections.Counter(text).most_common()[0]


def the_longest_word(text):
    text = ''.join(x for x in text if x not in set(string.punctuation))
    text = text.split(' ')
    return max(text, key=len)


print(most_common_word(SOME_TEXT))
print(the_longest_word(SOME_TEXT))
