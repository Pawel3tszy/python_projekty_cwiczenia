# odwrotny komunikat

print("\nSiema! Sprawa jest prosta, wypisujesz komunikat.")
print("Komputer wypisuje go w odwrotnej kolejności.")


komunikat = input("\nTwój komunikat to: ")
print(komunikat)

n_kom = ""

while komunikat:
    n_kom += komunikat[-1]
    komunikat = komunikat[:-1]
#    print(n_kom)
#    print(komunikat)
    
print("To jest twój nowy komunikat: ", n_kom)

input("\nAby zakończyć program, pocałuj mnie w faje albo naciśnij klawisz Enter.\n")
