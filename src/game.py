#  Copyright (c) 2019. Created by Tomasz Piechocki

from World.squareWorld import SquareWorld


class Game:
    """
    Game controller
    """
    def __init__(self, window):
        self.setGame()

        self.window = window
        self.window.resize(1280, 720)
        self.window.setWindowTitle("Tomasz Piechocki, 175690")
        self.window.setStyleSheet("* { background-color: lightgray; }")

        self.__world = SquareWorld(self, self.x, self.y)
        self.__player = None


    def setGame(self):
        self.x = 20
        self.y = 20

    def newGame(self):
        Game(self.window)
