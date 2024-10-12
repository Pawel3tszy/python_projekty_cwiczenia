# Jaka to liczba. Zgaduje komputer


import random

moja = random.randint(1,100)
komputer = 50
proba = 1

print("Dobra komputerku głupi tera Cie dojade, nie masz szans.")
print("Mam zadanie dla Ciebie, pomyślalem wlaśnie liczbę i musisz ją odgadnąć.")
print("No więc moja liczba to:", komputer)

while komputer != moja:
    if komputer < moja:
        print("Za mała")
        komputer = komputer + (komputer // 2)
    else:
        print("Za duża")
        komputer = komputer // 2

    print("Moja liczba to:", komputer)
    proba += 1

print("Brawo komputer, jednak zgadłeś. Moja liczba to:", moja)
print("Ty zjebie potrzebowaleś jednak do tego", proba, "prób.")
