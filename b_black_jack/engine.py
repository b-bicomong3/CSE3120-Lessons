from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.__DEALER = Player("Dealer")
        self.__PLAYER = None
        self.__DECK = Deck()

    def setup(self):
        PLAYER_NAME = input("Player Name: ")
        self.__PLAYER = Player(PLAYER_NAME)
        self.__DECK.shuffle()

    def run(self):
        while not self.__DEALER.isWinner() and not self.__PLAYER.isWinner():
            for i in range(2):
                self.__DEALER.takeCard(self.__DECK.drawCard())
                self.__PLAYER.takeCard(self.__DECK.drawCard())
            # Player Turn
            while not self.__PLAYER.isHold():
                print(f"{self.__PLAYER.getName()}'s Hand: {self.__PLAYER.getHand()}")
                #### input
                DRAW_CARD = input("Draw Card? (y/N) ")
                #### processing
                if DRAW_CARD.upper() == "Y":
                    self.__PLAYER.takeCard(self.__DECK.drawCard())
                else:
                    self.__PLAYER.holdHand()
                # Calculate Score
                HAND = self.__PLAYER.getHand()
                SCORE = self.__calcScore(HAND)
                if SCORE > 21:
                    self.__PLAYER.isHold()
            self.__PLAYER.setHandValue(SCORE)
            # Dealer Turn
            # Dealer must keep drawing until the dealer hand is greater than 15
            while not self.__DEALER.isHold():
                # Calculate Score
                HAND = self.__DEALER.getHand()
                SCORE = self.__calcScore(HAND)
                if SCORE >= 16:
                    self.__DEALER.holdHand()
                else:
                    self.__DEALER.takeCard(self.__DECK.drawCard())
            self.__DEALER.setHandValue(SCORE)
            # Calculate winner
            if self.__PLAYER.getHandValue() < 22 and self.__DEALER.getHandValue() > 21:
                WINNER = 1
                self.__PLAYER.addScore()
            elif self.__PLAYER.getHandValue() > self.__DEALER.getHandValue() and self.__PLAYER.getHandValue() < 22:
                WINNER = 1
                self.__PLAYER.addScore()
            else:
                WINNER = 0
                self.__DEALER.addScore()
            #### outputs
            print(f"{self.__DEALER.getName()}'s Hand: {self.__DEALER.getHand()}")
            if WINNER == 1:
                print(f"{self.__PLAYER.getName()} wins this round!")
            elif self.__PLAYER.getHandValue() <= 22:
                print(f"BUST! {self.__DEALER.getName()} wins this round!")
            else:
                print(f"{self.__DEALER.getName()} wins this round!")
            # RESET ASSETS
            self.__PLAYER.resetHand()
            self.__DEALER.resetHand()
            self.__DECK = Deck()
            self.__DECK.shuffle()
        #### Output Winner
        if self.__DEALER.isWinner():
            print(f"{self.__DEALER.getName()} Wins!")
        else:
            print(f"{self.__PLAYER.getName()} Wins!")

    def __calcScore(self, HAND):
        SCORE = 0
        ACE = 0
        for card in HAND:
            if card.getCardValue() == 1:
                SCORE += 11
                ACE += 1
            elif card.getCardValue() > 9:
                SCORE += 10
            else:
                SCORE += card.getCardValue()
        while SCORE > 21:
            if ACE > 0:
                SCORE -= 10
                ACE -= 1
            else:
                break
        return SCORE


if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()
