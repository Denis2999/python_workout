aktualne_ustawienie = input().split(" ")
aktualne_ustawienie = [int(i) for i in aktualne_ustawienie]

proponowane_ustawienie = input().split(" ")
proponowane_ustawienie = [int(i) for i in proponowane_ustawienie]

bool_list = []
for i in range(len(aktualne_ustawienie)):
    if aktualne_ustawienie[i] == proponowane_ustawienie[i]:
        bool_list.append(True)
    else:
        bool_list.append(False)

print(bool_list)
