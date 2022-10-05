# player.py in b_black_jack

"""
Title: Player class
Author: Beatrix Bicomong
Date-created: 04-10-2022
"""
from deck import Deck


class player:
    """
    The player for the game Black Jack
    """

    def __init__(self):
        """
        Create player object
        """
        self.DECK = []
        for i in range(2):
            self.DECK.append(Deck())
        self.HELD = []
        self.SCORE = 0

    # MODIFIERS

    def addScore(self, POINTS):
        """
        Adds player score
        :param POINTS: int
        :return: None
        """
        self.SCORE += POINTS

    def holdCard(self):
        """
        User selects card
        :return: None
        """
        print("Select a card to hold")
        for i in range(len(self.DECK)):
            print(f"{i + 1}. {self.DECK[i]}")
        CARD = int(input("> ")) - 1
        self.HELD.append(self.DECK.pop)


    # ACCESSORS

if __name__ == "__main__":
    DECK = Deck()
    DECK.shuffle()

    PLAYER = player()
    PLAYER.holdCard()
