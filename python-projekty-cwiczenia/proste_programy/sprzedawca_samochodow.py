# Program "Sprzedawca samochodów"

cena = input("Cena podstawowa nowego samochodu ")
cena = int(cena)
podatek = cena * 0.21
print("podatek", podatek)
opłata_rejestracyjna = cena * 0.06
print("opłata rejestracyjna", opłata_rejestracyjna)
prowizja_dealera = int(1000)
print("prowizja dealera", prowizja_dealera)
dostarczenie = int(300)
print("dostarczenie", dostarczenie)
print("Cena całkowita nowego samochodu wynosi", cena + podatek +
      opłata_rejestracyjna + prowizja_dealera + dostarczenie, "zł")


