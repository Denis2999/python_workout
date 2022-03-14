family_class = {}

iteration_item = int(input())
for i in range(iteration_item):
    child, *parent = input().replace(":", " ").split()
    family_class[child] = parent


def is_there_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = is_there_path(graph, node, end, path)
            if newpath: return newpath
    return None


iteration_item = int(input())
answers = []
for i in range(iteration_item):
    parent, child = input().split()
    if is_there_path(family_class, child, parent) is not None:
        answers.append("Yes")
    else:
        answers.append("No")
for i in answers:
    print(i)
