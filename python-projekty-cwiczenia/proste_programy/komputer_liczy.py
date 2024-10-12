#Komputer liczy

#pętla gdzie komputer liczy

#gracz podaje początek
#gracz podaje koniec
#gracz podaje co ile

#wyswietlenie liczenia

#koniec programu
print(
    """
    Siemandero, jołjoł, witam w moim programie do liczenia:D,
    polega on na tym, że podajesz zakres liczb w jakim chcesz żeby komputer
    policzyl za Ciebie oraz wielkość odstępu miedzy kolejnymi liczbami.
    """
    )

poczatek = int(input("\nPodaj początek liczenia: "))
koniec = int(input("\nPodaj koniec liczenia: "))
coile = int(input("Podaj wielkosc odstępu między kolejnymi liczbami: "))
            
for i in range(poczatek, koniec, coile):
    print(i, end=" ")

input("\n\nAby zakończyć program niciśnij klawisz Enter.")
