def dir_reduction(directions):
    north = 0
    south = 0
    west = 0
    east = 0
    for i in directions:
        if i == "NORTH":
            north += 1
        elif i == "SOUTH":
            south += 1
        elif i == "WEST":
            west += 1
        elif i == "EAST":
            east += 1

    width = west - east
    hight = north - south

    width_list = []
    for i in range(abs(width)):
        if width > 0:
            width_list.append("WEST")
        else:
            width_list.append("EAST")

    hight_list = []
    for i in range(abs(hight)):
        if width > 0:
            hight_list.append("NORTH")
        else:
            hight_list.append("SOUTH")

    return hight_list + width_list


print(dir_reduction(
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH",
     "WEST"]))
