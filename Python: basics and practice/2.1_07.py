import sys

sys.stdin = open("input.txt", "r")

parents = {}

n = int(input())
for i in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]
print("Parents are: ", parents)

q = int(input())
anton_list = [input() for i in range(q)]
# print("Anton list: ", anton_list)


def is_parent(child, parent):
    if parent == child:
        return True
    for i in parents[child]:
        if is_parent(i, parent):
            return True
    return False


output_list = []
for i in anton_list[::-1]:
    pop_elem = anton_list.pop()
    for j in anton_list:
        if is_parent(pop_elem, j):
            output_list.append(pop_elem)
            break
for i in output_list[::-1]:
    print(i)
