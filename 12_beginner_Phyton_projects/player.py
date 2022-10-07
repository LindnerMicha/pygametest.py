import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_sqare = False
        val = None
        while not valid_sqare:
            square = input(self.letter + "\´s turn. Imput move (0-9): ")
            # herausfinden ob die eingabe verwertbar ist
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqare = True # if these are sucscessful
            except ValueError:
                print("Invalid square. Try again")
        return val