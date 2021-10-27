dictionary_1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 'a': 10, 'b': 15, 'c': 4}
dictionary_2 = {"brand": "Ford", "model": "Mustang", "year": 1964}

for i in dictionary_2:
    dictionary_1[i] = dictionary_2[i]
print(dictionary_1)

result = {**dictionary_1, **dictionary_2}
print(result)
