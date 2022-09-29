# main.py
"""
Title: Main
Author: Beatrix Bicomong
Date-created: 29-09-22
"""

from c_game_engine import Game


class Main:
    """
    tells python what files to run
    """

    def __init__(self):
        self.GAME = Game()
        self.GAME.setup()
        self.GAME.run()


if __name__ == "__main__":
    Main()
