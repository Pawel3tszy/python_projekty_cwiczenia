# Zwierzak z konstruktorem
# Demonstruje konstruktory

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self):
        print("Urodził się nowy zwierzak!")

    def talk(self):
        print("\nCześć! Jestem egzemplarzem klasy Critter.")

# część główna
Critter()
Critter()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
