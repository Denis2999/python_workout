import json


def test(parent, child):
    if parent == child or parent in base[child]:
        return True
    for i in base[child]:
        if test(parent, i):
            return True
    return False


templates = json.loads(input())
# templates = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []},
#              {"name": "D", "parents": ["C", "F"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": []}]

base = {}
for i in templates:
    base[i["name"]] = i["parents"]
# print(base)

answer_values = [i for i in base]
answer_numbers = [0 for i in base]

for i in base:
    for j in base:
        if test(i, j):
            ind = answer_values.index(i)
            answer_numbers[ind] += 1

zipped_answer = zip(answer_values, answer_numbers)

for i, j in sorted(list(zipped_answer)):
    print("{} : {}".format(i, j))
