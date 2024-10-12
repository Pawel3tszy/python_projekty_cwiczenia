# Zwierzak z klasą
# Demonstruje atrybuty klasy i metody statyczne

class Critter(object):
    """Wirtualny pupil"""
    total = 0

    @staticmethod
    def status():
        stat = print("\nOgólna liczba zwierzaków wynosi", Critter.total)
        return stat

    def __init__(self, name):
        print("Urodził się zwierzak!")
        self.name = name
        Critter.total += 1

# część główna
print("Uzyskanie dostępu do atrybutuklasy Critter.total:", end=" ")
print(Critter.status())

Critter.status()

print("\nTworzenie zwierzaków.")
crit1 = Critter("zwierzak 1")
crit2 = Critter("zwierzak 2")
crit3 = Critter("zwierzak 3")

Critter.status()

print("\nUzyskanie dostepu do atrybutu klasy poprzez obiekt:", end=" ")
print(crit1.total)
print(crit2.status())
crit1.total
crit1.status()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
