import random

def guess(x):
    ran_num = random.randint(1, x)
    print("Debug: Gehaimzahl = " + str(ran_num))
    guess = 0
    while guess != ran_num:
        guess = int(input(f"\nVersuche nun die Gehime Zahl zwischen 1 und {x} zu erraten: "))
        if guess < ran_num:
            print("Die Geheim Zahl ist größer als dein Tipp")
        elif guess > ran_num:
            print("Die Geheim Zahl ist kleiner als dein Tipp")
    print("\nGratulation, du hast die Zahl richtig erraten !!")


x = input("Gib den maximalen Zahlenbereich an: ")
guess(int(x))