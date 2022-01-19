def descending_order(num):
    list_of_nums = [int(i) for i in list(str(num))]
    descending_list = []
    for i in list_of_nums:
        max_elem = max(list_of_nums)
        descending_list.append(max_elem)
        list_of_nums.remove(max_elem)

    return descending_list, descending_list


print(descending_order(145263))
