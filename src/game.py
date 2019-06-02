#  Copyright (c) 2019. Created by Tomasz Piechocki

import random
import math

from PyQt5.QtWidgets import QInputDialog

from World.squareWorld import SquareWorld
from Organisms.Animals.sheep import Sheep
from Organisms.Animals.wolf import Wolf

class Game:
    """
    Game controller
    """
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.__world = None
        self.__player = None

        self.window = window
        self.window.setWindowTitle("Tomasz Piechocki, 175690")
        self.window.setStyleSheet("* { background-color: lightgray; }")

        self.setGame()

    def setGame(self):
        self.x = QInputDialog.getInt(None, "Input", "Podaj szerokość (10-40):", 20, 10, 40, 1)[0]
        self.y = QInputDialog.getInt(None, "Input", "Podaj wysokość (10-30):", 20, 10, 30, 1)[0]

        self.__world = SquareWorld(self, 10,10)
        #temp = self.__world.getRandomEmptyField()

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 200)
        limit = random.randint(2*rate, 4*rate)
        for i in range (0, 99):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Sheep(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 400)
        limit = random.randint(2 * rate, 3 * rate)
        for i in range(0, 1):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Wolf(temp.getX(), temp.getY(), self.__world))

        self.__world.displayWorld()

    def newTurn(self):
        self.__world.makeTurn()

    def newGame(self):
        Game(self.window)
