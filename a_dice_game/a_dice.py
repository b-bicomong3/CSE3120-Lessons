# a_dice.py inside a_dice_game directory
"""
Title: Dice class
Author: Beatrix Bicomong
Date-created: 27-09-2022
"""

from random import randint


class Die:
    """
    create a die to roll for random numbers
    """

    # input
    def __init__(self, SIDES=6):
        """
        construct a die
        :param SIDES: int
        """
        self.DIE_MAX = SIDES
        self.DIE_NUM = None

    # processing
    def rollDie(self):
        """
        update die with new number
        :return: None
        """
        self.DIE_NUM = randint(1, self.DIE_MAX)

    def getEven(self):
        """
        test if the data number is even
        :return: bool
        """
        if self.DIE_NUM % 2 == 0:
            return True
        else:
            return False

    # output
    def displayDie(self):
        """
        print the number
        :return: None
        """
        print(self.DIE_NUM)


if __name__ == "__main__":
    # Simple dice game
    ### VARIABLES ###
    SCORE = 0

    DIE_1 = Die()
    DIE_2 = Die()

    print("""
    Welcome to Dice Roll
    Get points by correctly choosing both odd, both even or odd and even!
    Lose points if you are wrong.
    """)
    while True:

        # --- INPUTS --- #
        print("""
        1. Guess will be odd
        2. Guess will be even
        3. Guess will be odd and even
        """)

        CHOICE = int(input("> "))

        # --- PROCESSING --- #
        DIE_1.rollDie()
        DIE_2.rollDie()

        if DIE_1.getEven() and DIE_2.getEven():
            RESULT = 2
        elif not DIE_1.getEven() and not DIE_2.getEven():
            RESULT = 1
        else:
            RESULT = 3

        if CHOICE == RESULT:
            SCORE += 10
        elif SCORE == 0:
            pass
        else:
            SCORE -= 5

        # --- OUTPUTS -- #
        DIE_1.displayDie()
        DIE_2.displayDie()

        if CHOICE == RESULT:
            print("right on!")
        else:
            print("better luck next time")
        print(f"Score: {SCORE}")


    """
    DIE_1 = Die()
    DIE_2 = Die()

    DIE_1.rollDie()  # calling on  a method using a dot function
    DIE_2.rollDie()

    DIE_1.displayDie()
    DIE_2.displayDie()

    
    if DIE_1.getEven():
        print("Die 1 is Even")
    else:
        print("Die 1 is Odd")
    """
