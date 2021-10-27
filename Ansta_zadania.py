import numpy


def index_generator(index_1, index_2):
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1

    try:
        index_1 = int(index_1.replace('-', ''))
        index_2 = int(index_2.replace('-', ''))
    except ValueError:
        print("ValueError. Enter proper values")
        raise

    index_list = []
    for i in range(index_1 + 1, index_2):
        i = list(str(i))
        i.insert(2, "-")
        index_list.append("".join(i))
    return index_list


def missed_element(list_of_elements, strength):
    missed_elements = list(set([i for i in range(1, strength + 1)]) - set(list_of_elements))
    return missed_elements


def list_05_generator(fst_number, lst_number):
    if fst_number > lst_number:
        fst_number, lst_number = lst_number, fst_number

    return numpy.arange(fst_number, lst_number + 0.5, 0.5).tolist()


print(index_generator("79-900", "80-155"))
print(missed_element([2, 3, 7, 4, 9], 10))
print(list_05_generator(2, 5.5))
