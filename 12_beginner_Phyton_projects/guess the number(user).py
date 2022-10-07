import random

def guess(hidden_num, better):
#    guess = random.randint(1, (hidden_num*2))                                 #erzeugt sein guess
    guess = 0
    count = 0
    while guess != hidden_num:
        guess = random.randint(1, (hidden_num * 2)-better)
        count +=1
        print("Debug: Geratene Zahl = " + str(guess))

    print("\nDeine Geheimzahl war: " + str(hidden_num))
    print("Schade, der Computer hat nach " + str(count) + " versuchen deine Zahl erraten")


hidden_num = int(input("Gib die Geheimzahl ein: "))
better = int(input("Um wie viel soll sich der Computer verbessern ? "))
guess(hidden_num, better)