# c_game_engine.py
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from b_player import Player


class Game:
    """
    provide the structure for the turns and win condition of the game
    """

    def __init__(self):
        self.PLAYER1 = Player()
        self.PLAYER2 = Player()

    def setup(self):
        """
        where data needs to be modified to start the game
        :return:
        """
        print("Welcome to Farkle")

    def run(self):
        """
        where majority of the game will happen. This section often loops
        :return:
        """
        while self.PLAYER1.SCORE < 10000 and self.PLAYER2.SCORE < 10000:
            # --- PLAYER 1 TURN --- #
            print("Player 1 Turn!")
            ROLLS = 0
            while ROLLS < 3 and len(self.PLAYER1.DICE) > 0:
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDie()
                ROLLS += 1
            TEMP_POINTS = int(input("Player 1 Points: "))
            self.PLAYER1.addScore(TEMP_POINTS)
            self.PLAYER1.resetDie()

            # --- PLAYER 2 TURN --- #
            print("Player 2 Turn")
            ROLLS = 0
            while ROLLS < 3 and len(self.PLAYER2.DICE) > 0:
                self.PLAYER2.rollDice()
                self.PLAYER2.holdDie()
                ROLLS += 1
            TEMP_POINTS = int(input("Player 2 Points: "))
            self.PLAYER2.addScore(TEMP_POINTS)
            self.PLAYER2.resetDie()
        if self.PLAYER1.SCORE > self.PLAYER2.SCORE:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins")
        exit()


if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()
