# Inwentarz bohatera 3.0
# Demonstruje listy

# utwórz listę zawierającą pewne elementy i wyświetl jej zawartość
# za pomocą pętli for
inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]
print("Elemnety Twojego inwentarza:")
for item in inventory:
    print(item)

# wyświetl długość listy
print("Twój dobytek zawiera", len(inventory), "elementy(-ów).")

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

#sprawdź czy element należy do listy, zapomocą operatora in
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

# wyświetl jeden element wskazany przez indeks
index = int(input("\nWprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje sie", inventory[index])

# wyświetl wycinek
start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontunuować grę, naciśnij klawisz Enter.")

# dokonaj konkatenacji dwócj list
chest = ["złoto", "klejnoty"]
print("Znajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartośc skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inventarz to:")
print(inventory)

input("\nAby kontunuowac grę, nacisnij klawisz Enter.")

# przypisz poprzez nowy indeks
print("Wyniemasz swój miecz na kuszę.")
inventory[0] = "kusza"
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# przypisz poprzez wycinek
print("Zużywasz swoje złoto i klejnoty na zakup kuli do wróżenia.")
inventory[4:6] = ["kula do wróżenia"]
print("Twój aktulany inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, nacisnij klawisz Enter.")

# usuń lement
print("W wielkiej bitwie Twoja tarcza zostaje zniszczona.")
del inventory[2]
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuowac grę, naciśnij klawisz Enter.")

# usuń wycinek
print("Twoja tarcza i kusza zostały skradzione przez złodzei.")
del inventory[:2]
print("Twój aktulany inwentarz to:")
print(inventory)

input("\nAby zakończyć program, naciśnij klawisz Enter.")
