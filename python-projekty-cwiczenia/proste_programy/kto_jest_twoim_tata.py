# program kto jest twoim tata
# pokazuje działanie i modyfikacje słowników

# wprowadzasz syna przedstawia ojca
# dodajesz syn ojciec
# wymieniasz syn ojciec
# usuwasz syn ojciec
# koniec

pary = {"Paweł Wojtkowiak": "Piotr Wojtkowiak", "Adam Bindek": "Grzegorz Bindek",
        "Krystian Guzierowicz": "Sławomir Guzierowicz"}

wybor = None
while wybor != "5":
    
    print("""
    1. Wyszukaj ojca
    2. Dodaj parę syn-ojciec
    3. Wymień parę syn-ojciec
    4. Usuń parę syn-ojciec
    5. Zakończ
    """)

    wybor = input("Wybierz opcje z menu: ")
    
    if wybor == "1":
        syn = input("Podaj imię i nazwisko syna: ")
        if syn in pary:
            print("Imię i nazwisko ojca:",pary[syn])
        else:
            print("Nie ma takiej osoby w bazie danych.")
            syn = input("Podaj imię i nazwisko syna: ")
    elif wybor == "2":
        print(pary)
        syn = input("Dodaj imie i nazwisko syna: ")
        ojciec = input("Dodaj imię i nazwisko ojca: ")
        pary[syn] = ojciec
        print(pary)
    elif wybor == "3":
        print(pary)
        syn = input("Która parę chcesz wymienić?: ")
        if syn in pary:
            ojciec = input("Podaj dane nowego taty: ")
        else:
            print("Nie ma takiej osoby w bazie danych.")
            syn = input("Która parę chcesz wymienić?: ")
        pary[syn] = ojciec
        print(pary)
    elif wybor == "4":
        print(pary)
        syn = input("Którą parę chcesz usunąć? ")
        if syn in pary:
            del pary[syn]
        else:
            print("Nie ma takiej osoby w bazie danych.")
            syn = input("Która parę chcesz usunąć? :")
        print(pary)
    elif wybor == "5":
        print("Wyjście z programu.")

print("\nAby zakończyć program, naciśnij klawisz Enter.")        
