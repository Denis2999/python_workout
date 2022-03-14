import os

py_list = []

tree = os.walk("main")
for current_dir, dirs, files in tree:
    for i in files:
        if i[-3:] == ".py":
            py_list.append(current_dir)
            break
    print("current dir is: ", current_dir)
    print("dirs is: ", dirs)
    print("files are: ", files)
    print("-----------------")

print("py_list is: ", sorted(py_list))

with open('input.txt', 'w') as fw:
    fw.writelines("\n".join(sorted(py_list)))