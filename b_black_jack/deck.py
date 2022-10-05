# deck.py in b_black_jack

"""
Title: Deck class
Author: Beatrix Bicomong
Date-created: 04-10-2022
"""

from card import Card
from random import shuffle


class Deck:
    """
    Create a deck of 52 playing cards
    """

    def __init__(self):
        self.__DECK = []
        for i in range(4):
            for j in range(13):
                self.__DECK.append(Card(i, j))

    # MODIFIER
    def shuffle(self):
        """
        Shuffles the deck
        :return:
        """
        shuffle(self.__DECK)

    def drawCard(self):
        """
        Draws the top card
        :return: obj(Card)
        """
        if len(self.__DECK) > 0:
            return self.__DECK.pop(0)

    # ACCESSOR
    def getDeck(self):
        return self.__DECK


if __name__ == "__main__":
    DECK = Deck()
    for i in range(5):
        print(DECK.getDeck()[i])
    DECK.shuffle()
    for i in range(5):
        print(DECK.getDeck()[i])
    HAND = []
    for i in range(5):
        HAND.append(DECK.drawCard())
    print(HAND)
