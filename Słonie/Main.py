try:
    liczba_sloni = int(input())
    if 2 > liczba_sloni or liczba_sloni > 1000000:
        raise ValueError("liczba słoni jest poza dziedziną")
except ValueError:
    print("To nie jest liczba")

masa_sloni = input().split(" ")
masa_sloni = [int(i) for i in masa_sloni]
for i in masa_sloni:
    if i < 100 or i > 6500:
        raise ValueError("Masa słoni jest poza dziedziną")

aktualne_ustawienie = input().split(" ")
aktualne_ustawienie = [int(i) for i in aktualne_ustawienie]
for i in aktualne_ustawienie:
    if i < 1 or i > liczba_sloni:
        raise ValueError("numer słoni jest poza dziedziną")

proponowane_ustawienie = input().split(" ")
proponowane_ustawienie = [int(i) for i in proponowane_ustawienie]
for i in proponowane_ustawienie:
    if i < 1 or i > liczba_sloni:
        raise ValueError("numer słoni jest poza dziedziną")


def zamiana_pozycji():
    koszt_wysilku = 0
    for i in range(liczba_sloni):
        if aktualne_ustawienie[i] != proponowane_ustawienie[i]:
            x = aktualne_ustawienie.index(proponowane_ustawienie[i])
            aktualne_ustawienie[i], aktualne_ustawienie[x] = aktualne_ustawienie[x], aktualne_ustawienie[i]
            koszt_wysilku += masa_sloni[x] + masa_sloni[i]
    return koszt_wysilku


print(zamiana_pozycji())
