# Po literce

# komputer wybiera losowo słowo
# komupter informuje ile liter znajduje się w słowie
# gracz otrzymuje pięć szans na pytania o litere
# komputer odpowiada tylko tak lub nie, potem gracz odpowiada

import random

SLOWA = ("gitara", "saksofon", "klawisze", "rower", "latanie", "wypad")
SZANSA = 5

losowe = random.choice(SLOWA)
dlugosc = len(losowe)

print("\nKomputer wylosował słowo, zgadnij jakie to słowo!\nMasz 5 szans \
na zadanie pytania o literę.")
print("Słowo składa się z", dlugosc, "liter.")

while SZANSA > 0:
    litera = input("Podaj literę która Twoim zdaniem występuje w słowie: ")
    SZANSA -= 1
    if litera in losowe:
        print("Tak ta litera występuje!")
    else:
        print("Niestety, ta litera nie występuje.")

slowo = input("Wykorzystałeś już 5 prób. Jakie to słowo? ")
if slowo == losowe:
    print("Brawo! Zgadłeś!")
else:
    print("No kurwa chyba nie!")
print("To słowo to:", losowe)
input("\nAby zakończyć program naciśnij klawisz Enter.")


