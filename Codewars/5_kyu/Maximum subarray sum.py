def max_sequence(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in arr:
        max_ending_here += i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        elif max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))
# should be 6: [4, -1, 2, 1]
