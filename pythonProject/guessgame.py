secret_word = "baum"
guess = ""
count = 3

while guess != secret_word:
    count = count - 1
    guess = input("Enter guess: ")
    if guess != secret_word:
        if count == 0:
            break

        print("Falsch")
        print("Noch " + str(count) + " versuche")


if guess == secret_word:
    print("Du hast richtig geraten! Du hast gewonnen!")
elif count == 0:
    print("Deine züge sind vorbei")