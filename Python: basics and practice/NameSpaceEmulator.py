namespaces = {
    "global": {
        "variables": [],
        "parent": None
    }
}


def cmd_create(namesp, parent):
    namespaces[namesp] = {
        "variables": [],
        "parent": parent
    }


def cmd_add(namesp, var):
    namespaces[namesp]["variables"].append(var)


def cmd_get(namesp, var):
    if namesp == None:
        print(None)
    elif var in namespaces[namesp]["variables"]:
        print(namesp)
    else:
        # print("Namespaces & parent is: ", namespaces[namesp]["parent"],"\n")
        cmd_get(namespaces[namesp]["parent"], var)


iterators = int(input())
for i in range(iterators-1):
    cmd, namesp, arg = input().split()
    if cmd == "create":
        cmd_create(namesp, arg)
    elif cmd == "add":
        cmd_add(namesp, arg)
    elif cmd == "get":
        cmd_get(namesp, arg)
print(namespaces)
