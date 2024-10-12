# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwyklego pliku tekstowego

import sys, pickle, shelve

def open_file(file_name, mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony. \n", e)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    scores = next_line(the_file)
    
    return category, question, answers, correct, explanation, scores

def lista_naj(wynik):
    wyniki += [wynik]
    print(wyniki)
    return wyniki

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")
    name = input("Podaj imię gracza: ")
    return name

def main():
    trivia_file = open_file("kwiz2.txt", "r")
    title = next_line(trivia_file)
    name = welcome(title)
    score = 0
    wyniki = []
    # pobierz pierwszy blok
    category, question, answers, correct, explanation, scores = next_block(trivia_file)
    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedź
        answer = input("Jaka jest Twoja odpowiedź?: ")

        # sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(scores)
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")
    
        # pobierz kolejny blok
        category, question, answers, correct, explanation, scores = next_block(trivia_file)
    
    
    trivia_file.close()

    print("To było ostatnie pytanie")
    print("Twój końcowy wynik wynosi", score, "\n")

    wynik = [name, score]
    print(wynik)
    wyniki += wynik
            
    f = open("wyniki.dat", "ab")
    pickle.dump(wyniki, f)
    f.close()
    f = open("wyniki.dat", "rb")
    print("\nLista wyników:\n")
    wyniki = pickle.load(f)
    print(wyniki)
    f.close()
    
main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
