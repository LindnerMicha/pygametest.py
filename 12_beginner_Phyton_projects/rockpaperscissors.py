import random
hand = ["Rock", "Paper", "Scissor"]

def runtime(par):
    # r > s, s > p , p > r
    win_user = 0
    win_pc = 0
    draw = 0
    par_c = par

    try:
        while par > 0:
            user_in = int(input("Welches Symbol möchtest du Spielen ?\n[1] Rock \n[2] Paper \n[3] Scissor\n"))

            player_user = hand[user_in - 1]
            hand_pc = int(random.randint(0, 2))
            player_pc = hand[hand_pc]
            print("Der PC hat gespielt: " + str(player_pc))

            if player_user == player_pc:
                print("Unentschieden\n")
                par = par -1
                draw = draw +1

            if is_win(user_in, hand_pc):
                print("Du has Gewonnen\n")
                par = par -1
                win_user = win_user +1
            else:
                print("Du hast Verloren\n")
                par = par -1
                win_pc = win_pc +1

        message = (f"""Der Spielstand nach {par_c} Partien lautet:
                       Siege User    {win_user}
                       Siege PC      {win_pc}
                       Unentschieden {draw}""")

        print("Das Spiel ist vorbei !")
        print(message)
    except:
        print("Du hast einen ungültigen Wert eingegeben, das Spiel ist vorbei !")

def is_win(user_in, hand_pc):               # return true if -> 0 > 2, 2 > 1 , 1 > 0
    if (user_in == 0 and hand_pc == 2) or (user_in == 2 and hand_pc == 1) or (user_in == 1 and hand_pc == 0):
        return True



par = int(input("Wie viele Partien möchtest du Spielen ? "))
runtime(par)