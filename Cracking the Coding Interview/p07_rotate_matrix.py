def rotate_matrix(m):
    new_m = []
    for j in range(len(m)):
        for i in range(len(m[0]) - 1, -1, -1):
            new_m.append([j][i])
    return new_m
    # for i in matrix:
    #     for j in i:
    #         print(i[j], end=', ')
    #     print('')
    # return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


print(rotate_matrix(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
))
