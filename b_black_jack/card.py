# cards.py in b_black_jack
"""
Title: Card class
Author: Beatrix Bicomong
Date-created: 04-10-2022
"""


class Card:
    """
    A single playing card
    """
    SUITS = {
        0: "Diamonds",
        1: "Clubs",
        2: "Hearts",
        3: "Spades"
    }

    VALUES = {
        0: "Ace",
        1: "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        8: "9",
        9: "10",
        10: "Jack",
        11: "Queen",
        12: "King"
    }

    def __init__(self, SUIT, VALUE):
        self.__SUIT = SUIT
        self.__VALUE = VALUE

    # MODIFIER

    # ACCESSOR
    def __str__(self):
        """
        Magic variable that defines what is printed in a string
        :return: str
        """
        return f"{Card.VALUES[self.__VALUE]} of {Card.SUITS[self.__SUIT]}"

    def __repr__(self):
        """
        Magic variable that defines how an object looks like in a list
        :return:
        """
        return f"<Card object - {self.__str__()}>"

    def getCardValue(self):
        return self.__VALUE

    def getCardSuit(self):
        return self.__SUIT


if __name__ == "__main__":
    CARD = Card(3, 6)  # 6 of spades
    print(CARD)
    print(CARD.getCardSuit())
    print(CARD.getCardValue())

    DECK = []
    for i in range(4):
        for j in range(13):
            DECK.append(Card(i, j))

    print(DECK)
