# program rzut monetą
# rzuca monetą sto razy a następnie podaje użytkownikowi liczbę orzełków i reszek

import random

rzut = 0
orzeł = 0
reszka = 0

while True:
    rzut += 1
    losowanie = random.randint(1,2)
    if rzut > 100:
        break
    elif losowanie == 1:
        orzeł += 1
    else:
        reszka += 1
print("Rzucałeś monetą sto razy.")        
print("Po stu rzutach wypadło", orzeł, "orłów, i", reszka, "reszek.")

input("\nAby zakończyć program, naciśnij klawisz Enter.")
