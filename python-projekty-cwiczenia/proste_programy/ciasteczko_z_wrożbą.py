# Ciasteczko z wróżbą
# Wyświetla losowo jedną z pięciu przepowiedni

import random

print("\n\tWitaj! Twoja przepowiednia na dzisiaj to:\n")

przepo = random.randint(1, 4)

if przepo == 1:
    print("Ju gona daj")
elif przepo == 2:
    print("Będzie kurwa pienknie")
elif przepo == 3:
    print("Wygrasz życie")
elif przepo == 4:
    print("Czeka Cię psychiatryk w hooj")
else:
    print("Brak przepowiedni bo jestes nołlajf")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
