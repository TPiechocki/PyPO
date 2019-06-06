#  Copyright (c) 2019. Created by Tomasz Piechocki

import random
import math
import pickle
import sys

from PyQt5.QtWidgets import QInputDialog, QErrorMessage

from Organisms.Animals.cybersheep import CyberSheep
from World.squareWorld import SquareWorld
from Organisms.Animals.sheep import Sheep
from Organisms.Animals.wolf import Wolf
from Organisms.Animals.fox import Fox
from Organisms.Animals.tortoise import Tortoise
from Organisms.Animals.antelope import Antelope
from Organisms.Plants.grass import Grass
from Organisms.Plants.dandelion import Dandelion
from Organisms.Plants.belladonna import Belladonna
from Organisms.Plants.guarana import Guarana
from Organisms.Plants.hogweed import Hogweed
from Organisms.player import Player

class Game:
    """
    Game controller
    """
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.__world: SquareWorld = None
        self.__player = None
        self.window = None

        self.setGame(window)

    def setGame(self, window):
        if window:
            window.hide()
        self.x, ok = QInputDialog.getInt(None, "Input", "Podaj szerokość (10-40):", 20, 10, 40, 1)
        if not ok:
            if window.windowTitle() == "sig":
                quit()
            window.show()
            return
        self.y, ok = QInputDialog.getInt(None, "Input", "Podaj wysokość (10-30):", 20, 10, 30, 1)
        if not ok:
            if not ok:
                if window.windowTitle() == "sig":
                    quit()
                window.show()
                return

        self.window = window
        self.window.setWindowTitle("Tomasz Piechocki, 175690")
        self.window.setStyleSheet("* { background-color: lightgray; }")

        self.__world = SquareWorld(self, self.x, self.y)

        temp = self.__world.getRandomEmptyField()
        self.__player = Player(temp.getX(), temp.getY(), self.__world)
        self.__world.addOrganism(self.__player)

        self.__world.setPlayer(self.__player)

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 200)
        limit = random.randint(2 * rate, 4 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Sheep(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 400)
        limit = random.randint(2 * rate, 3 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Wolf(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 300)
        limit = random.randint(2 * rate, 4 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Fox(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 500)
        limit = random.randint(2 * rate, 3 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Tortoise(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 500)
        limit = random.randint(2 * rate, 4 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Antelope(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 100)
        limit = random.randint(2 * rate, 4 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Grass(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 100)
        limit = random.randint(1 * rate, 3 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Dandelion(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 500)
        limit = random.randint(1 * rate, 3 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Guarana(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 500)
        limit = random.randint(1 * rate, 3 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Belladonna(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 1000)
        limit = rate
        for i in range(0, 10):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(Hogweed(temp.getX(), temp.getY(), self.__world))

        rate = 1 + math.floor((self.__world.getSizeX() * self.__world.getSizeY()) / 1000)
        limit = random.randint(2 * rate, 4 * rate)
        for i in range(0, limit):
            temp = self.__world.getRandomEmptyField()
            self.__world.addOrganism(CyberSheep(temp.getX(), temp.getY(), self.__world))

        self.__world.displayWorld()

    def newTurn(self):
        self.__world.makeTurn()

    def newGame(self):
        self.__world.clearNotifications()
        Game(self.window)

    def setImmortality(self):
        self.__player.activateImmortality()
        self.__world.refreshInfo()

    def changeDirection(self, dir):
        """
        Change player direction
        :param dir: member of Direction derived class
        :return: none
        """
        self.__player.setDirection(dir)
        self.__world.makeTurn()

    def saveGame(self):
        sys.setrecursionlimit(5000)

        filename, okPressed = QInputDialog.getText(None, "Nazwa pliku", "Podaj nazwę zapisu")
        if okPressed and filename != '':
            file = open(filename, 'wb')
            pickle.dump(self.__world, file)

    def loadGame(self):
        filename, okPressed = QInputDialog.getText(None, "Nazwa pliku", "Podaj nazwę zapisu")
        if okPressed and filename != '':
            try:
                file = open(filename, 'rb')
                self.__world = SquareWorld(self, self.x, self.y)
                self.__world = pickle.load(file)
                self.__player = self.__world.getPlayer()
                self.__world.recreateWindow(self)
                self.__world.displayWorld()
                self.__world.refreshInfo()
            except:
                error = QErrorMessage()
                error.setWindowTitle("Error")
                error.showMessage("Nie udało się otworzyć pliku")
                error.exec_()

    def addOrganism(self, x, y):
        field = self.__world.getField(x, y)
        options = ("Owca", "Wilk", "Lis", "Żółw", "Antylopa", "Trawa", "Mlecz", "Guarana", "Wilcza Jagoda", "Barszcz Sosnowskiego", "Cyberowca")

        if field.isEmpty():
            item, okPressed = QInputDialog.getItem(None, "Gatunek", "Wybierz gatunek:", options, 0, False)
            if okPressed and item:
                if item == "Owca":
                    self.__world.addOrganism(Sheep(x, y, self.__world))
                elif item == "Wilk":
                    self.__world.addOrganism(Wolf(x, y, self.__world))
                elif item == "Lis":
                    self.__world.addOrganism(Fox(x, y, self.__world))
                elif item == "Żółw":
                    self.__world.addOrganism(Tortoise(x, y, self.__world))
                elif item == "Antylopa":
                    self.__world.addOrganism(Antelope(x, y, self.__world))
                elif item == "Trawa":
                    self.__world.addOrganism(Grass(x, y, self.__world))
                elif item == "Mlecz":
                    self.__world.addOrganism(Dandelion(x, y, self.__world))
                elif item == "Guarana":
                    self.__world.addOrganism(Guarana(x, y, self.__world))
                elif item == "Wilcza Jagoda":
                    self.__world.addOrganism(Belladonna(x, y, self.__world))
                elif item == "Barszcz Sosnowskiego":
                    self.__world.addOrganism(Hogweed(x, y, self.__world))
                elif item == "Cyberowca":
                    self.__world.addOrganism(CyberSheep(x, y, self.__world))

        self.__world.displayWorld()

    def stopNotifications(self):
        self.__world.clearNotifications()