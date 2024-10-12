# kreator postaci

punkty = 30
bohater = {"sila": 0, "zdrowie": 0, "madrosc": 0, "zrecznosc": 0}

print(
"""
    Witaj w grze kreator postaci!

    Twój bohater posiada cztery atrybuty:
    1. Siła
    2. Zdrowie
    3. Mądrość
    4. Zręczność

    W puli masz 30 punktów które możesz dowolnie spożytkować na atrybuty.
    Do dzieła! """)

wybor = None
while wybor != "3":
    print(
    """ 
        1. Dodaj punkty do atrybutu
        2. Zwróć punkty z atrybutu
        3. Zakończ
    """)
              
    wybor = input("Podaj numer opcji z menu: ")
    if wybor == "1":
        print("""
                1. Siła
                2. Zdrowie
                3. Mądrość
                4. Zręczność
                """)
        atrybut = input("Podaj numer atrybutu do którego chcesz dodać punkty?\n")
        while atrybut not in ("1", "2", "3", "4"):
            print("Nie ma takiego atrybutu")
            atrybut = input("Podaj numer atrybutu do którego chcesz dodać punkty?\n")
            
        dodane = int(input("Ile punktów chcesz dodać do tego atrybutu?\n"))
        while dodane > punkty:
            print("Nie masz tylu punktów w puli.")
            dodane = int(input("Ile punktów chcesz dodać do tego atrybutu?\n"))
                         
        if atrybut == "1":
            bohater["sila"] += dodane
            atrybut = "Siła"
        elif atrybut == "2":
            bohater["zdrowie"] += dodane
            atrybut = "Zdrowie"
        elif atrybut == "3":
            bohater["madrosc"] += dodane
            atrybut = "Mądrość"
        elif atrybut == "4":
            bohater["zrecznosc"] += dodane
            atrybut = "Zręczność"
        else:
            print("Nie ma takiego atrybutu")
    
        punkty -= dodane
        print("Do atrybutu", atrybut, "dodałeś", dodane, "pkt.")
        print("W puli zostało", punkty, "pkt.")
        print("Bohater posiada:", bohater)
        if punkty <= 0:
            print("Wykorzystałeś wszystkie punkty z puli.")
        
    if wybor == "2":
        atrybut = input("Podaj numer atrybutu z którego chcesz zwrócić punkty do puli?\n")
        while atrybut not in ("1", "2", "3", "4"):
            print("Nie ma takiego atrybutu")
            atrybut = input("Podaj numer atrybutu z którego chcesz zwrócić punkty do puli?\n")
        
        zabrane = int(input("Ile punktów chcesz zwrócić do puli?\n"))
    
        if atrybut == "1":
            while zabrane > bohater["sila"]:
                print("Ten atrybut nie posiada tylu punktów.")
                zabrane = int(input("Ile punktów chcesz zwrócić do puli?\n"))
            else:
                bohater["sila"] -= zabrane
                atrybut = "Siła"
        elif atrybut == "2":
            while zabrane > bohater["zdrowie"]:
                print("Ten atrybut nie posiada tylu punktów.")
                zabrane = int(input("Ile punktów chcesz zwrócić do puli?\n"))
            else:
                bohater["zdrowie"] -= zabrane
                atrybut = "Zdrowie"
        elif atrybut == "3":
            while zabrane > bohater["madrosc"]:
                print("Ten atrybut nie posiada tylu punktów.")
                zabrane = int(input("Ile punktów chcesz zwrócić do puli?\n"))
            else:
                bohater["madrosc"] -= zabrane
                atrybut = "Mądrość"
        elif atrybut == "4":
            while zabrane > bohater["zrecznosc"]:
                print("Ten atrybut nie posiada tylu punktów.")
                zabrane = int(input("Ile punktów chcesz zwrócić do puli?\n"))
            else:
                bohater["zrecznosc"] -= zabrane
                atrybut = "Zręczność"
        else:
            print("Nie ma takiego atrybutu")
    
        punkty += zabrane
        print("Do puli zwrociłeś", zabrane, "pkt.")
        print("W puli znajduje się obecnie", punkty, "pkt.")
        print("Bohater posiada:", bohater)
        if punkty >= 30:
            print("Zwróciłeś wszystkie punkty do puli.")

    if wybor == "3":
        print("Zakończyłeś kreowanie swojego Bohatera.")
        
input("\nAby zakończyć program, naciśnij klawisz Enter.")
