def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums


def binary_search(list_1, item):
    low = 0
    high = len(list_1) - 1

    while low <= high:
        mid = low + high
        guess = list_1[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def scramble(s1, s2):
    s1 = insertion_sort(list(s1))

    for i in s2:
        item = binary_search(s1, i)
        if item is not None:
            s1.pop(s1.index(i))
        else:
            return False
    return True


print(scramble('rkqodlw', 'world'))  # == > True)
print(scramble('cedewaraaossoqqyt', 'codewars'))  # == > True)
print(scramble('katas', 'steak'))  # == > False)
