def anagrams(word, words):
    word = list(word)
    stdout = [i for i in words if sorted(word) == sorted(i)]
    return stdout


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy', 'lacer']))
