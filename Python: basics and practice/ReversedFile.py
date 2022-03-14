with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
    fw.writelines(fr.readlines()[::-1])


#
# with open("dataset_24465_4.txt") as p:
#     some_list = [i for i in p]
#     for i in some_list[::-1]:
#         print(i, end="")

    # for i in some_list[::-1]:
    #     test_f.write(i+"\n")
