import operator

dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 'a': 10, 'b': 15, 'c': 4}

result = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
print(result)

result = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))
print(result)
