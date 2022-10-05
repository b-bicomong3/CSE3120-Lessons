# b_player.py in a_dice_game folder
"""
Title: The player class
Author: Beatrix Bicomong
Date-created 28-09-22
"""
from a_dice import Die


class Player:
    """
    the player for the game Farkle
    """

    def __init__(self):
        """
        create a player object
        """
        self.DICE = []
        for i in range(6):
            self.DICE.append(Die())
        self.HELD = []
        self.SCORE = 0

    # --- METHOD --- #
    ### INPUTS
    def addScore(self, POINTS):
        """
        adds points to the player score
        :param POINTS: int
        :return: None
        """
        self.SCORE += POINTS
    ### PROCESSING
    def rollDice(self):
        """
        rolls sll dice is DICE
        :return: None
        """
        for die in self.DICE:
            die.rollDie()

    def holdDie(self):
        """
        user selects a die to save
        :return: None
        """
        print("Select a die to hold")
        for i in range(len(self.DICE)):
            print(f"{i + 1}. {self.DICE[i].DIE_NUM}")
        DIE = int(input("> ")) - 1
        self.HELD.append(self.DICE.pop(DIE))
        print("Dice remaining:")
        for die in self.DICE:
            die.displayDie()
        print("Dice held:")
        for die in self.HELD:
            die.displayDie()

        # ask to not roll
        BANK = input("Would you like to bank? (y/N)")
        if BANK.upper() == "Y":
            return self.getScore()
        else:
            # ask to hold more dice
            AGAIN = input("Hold More? (y/N) ")
            if AGAIN.upper() == "Y":
                return self.holdDie()

    def resetDie(self):
        """
        move all dice from HELD to DICE
        :return: None
        """
        self.DICE += self.HELD
        self.HELD = []

    ### OUTPUT
    def getDice(self):
        """
        display all dice in DICE
        :return:
        """
        for die in self.DICE:
            die.displayDie()

    def getScore(self):
        """
        displays the score
        :return:
        """
        print(self.SCORE)

if __name__ == "__main__":
    NAME = Player()
    NAME.rollDice()
    NAME.holdDie()
    POINTS = int(input("Points Scored: "))
    NAME.addScore(POINTS)
    NAME.resetDie()
    NAME.getScore()
