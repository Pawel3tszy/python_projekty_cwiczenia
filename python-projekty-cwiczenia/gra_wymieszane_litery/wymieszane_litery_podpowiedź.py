# Wymieszane litery
# Komputer wybiera losowo słowo, a później miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo
# Każdemu słowu towarzyszy podpowiedź
# Gracz dostaje więcej punktów jeśli odgadnie słowo bez korzystania z podpowiedzi

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

#podpowiedzi
PODPO = ("język programowania", "poprzestawiane litery", "przeciwieństwo trudnego",
         "przeciwieństwo prostego", "uzyskana na pytanie", "instrument?")

proba = 1

# wybierz losowo jedno słowo z sekwencji
index = random.randint(0, len(WORDS))

word = WORDS[index]
pod = PODPO[index]
    
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utwórz pomieszaną wersje słowa
jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
            Witaj w grze 'Wymieszane litery'!

    Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    podpo = input("Czy chcesz skorzystać z podpowiedzi? tak\\nie: ")
    if podpo == "tak":
        proba += 5
        print(pod)
    else:
        proba += 1
        print("To zgaduj dalej.")
    guess = input("Twoja odpowiedż: ")

if guess == correct:
    print("Zgadza się! Zgadłeś!\n")

print("Liczba prób to:", proba, \
      "\nJeśli skorzystałeś z podpowiedzi do wyniku dodano plus 5.")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
