# player.py in b_black_jack

"""
Title: Player class
Author: Beatrix Bicomong
Date-created: 04-10-2022
"""


class Player:
    """
    The player for the game Black Jack
    """

    def __init__(self, NAME):
        """
        Create player object
        """
        self.__HAND_VALUE = 0
        self.__WINS = 0
        self.__HAND = []
        self.__HOLD = False
        self.__NAME = NAME

    # MODIFIERS

    def takeCard(self, CARD):
        """
        adds a card to the player's hand
        """
        self.__HAND.append(CARD)

    def setHandValue(self, VALUE):
        self.__HAND_VALUE = VALUE

    def holdHand(self):
        self.__HOLD = True

    def resetHand(self):
        self.__HOLD = False
        self.__HAND = []
        self.__HAND_VALUE = 0

    def addScore(self):
        self.__WINS += 1

    # ACCESSOR
    def getName(self):
        return self.__NAME

    def getHand(self):
        return self.__HAND

    def getHandValue(self):
        return self.__HAND_VALUE

    def isHold(self):
        return self.__HOLD

    def isWinner(self):
        if self.__WINS >= 3:
            return True
        else:
            return False

