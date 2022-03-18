def dirReduc(arr):
    dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = []
    for i in arr:
        print("res", res)
        print("dict[i]", dict[i])
        # print("res-1", res[-1])
        print("######################################")
        if res and dict[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res


# print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))  # ["WEST"]
# print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))  # ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(['NORTH', 'NORTH', 'NORTH', 'WEST', 'SOUTH', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST', 'NORTH']))  # True
