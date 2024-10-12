# Zwierzak z atrybutem
# Demonstruje tworzenie atrybutów obiektu i uzyskiwanie do nich dostępu

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.dupa = name

    def __str__(self):
        nazwa = self.dupa
        return nazwa

    def talk(self):
        print("Cześć! Jestem", self.dupa, "\n")

# czeęść główna
crit1 = Critter("Reksio")
crit1.talk()

crit2 = Critter("Pucek")
crit2.talk()

print("Wyświetlenie obiektu crit1:")
print(crit1)

print("Bezpośrednie wyświetlenie wartości atrybutu crit1.name:")
print(crit1.dupa)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
