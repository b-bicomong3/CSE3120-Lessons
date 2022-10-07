from engine import Game


class Main:
    def __init__(self):
        self.__GAME = Game()
        self.__GAME.setup()
        self.__GAME.run()


if __name__ == "__main__":
    Main()
