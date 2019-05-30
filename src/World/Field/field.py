#  Copyright (c) 2019. Created by Tomasz Piechocki

import random

from abc import ABC, abstractmethod
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QColor

class Field(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__full_neighbours = None
        self.__neighbours = []
        self.__direction = None

        self.__organism = None

    def color(self):
        if (self.__organism):
            return self.__organism.color()
        else:
            return QColor(Qt.white)

    def isEmpty(self):
        return self.__organism != None

    def setNeighbours(self, fields, x_size, y_size):
        direction = self.__direction.defaultDirection()
        temp_full = 0

        for i in range(0, direction.amountOfDirections):
            x_temp = self.__x + direction.getX()
            y_temp = self.__y + direction.getY()
            if (x_temp >= 0 and x_temp < x_size and y_temp >= 0 and y_temp < y_size):
                self.__neighbours[direction.toInt()] = fields[x_temp][y_temp]
                temp_full += 1
            direction = direction.getNextDirection()

        self.__full_neighbours = temp_full

    def setOrganism(self, org):
        self.__organism = org

    def getOrganism(self):
        return self.__organism

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getNeighbour(self, direction):
        return self.__neighbours[direction.toInt()]

    def getFullNeighbours(self):
        index = 0
        temp = [None] * self.__full_neighbours
        for i in range(0, self.__direction.amountOfDirections):
            if (self.__neighbours[i] != None):
                temp[index] = self.__neighbours[i]
                index += 1

        return temp

    def randomNeighbour(self):
        full = self.getFullNeighbours()
        return full[random.random() * (self.__full_neighbours - 1)]

    def hasEmptyNeighbour(self):
        for i in range(0, self.__direction.amountOfDirections):
            if (self.__neighbours[i] != None and self.__neighbours[i].isEmpty()):
                return True
        return False

    def RandomEmptyNeighbour(self):
        index = 0
        temp = [None] * self.__full_neighbours
        for i in range(0, self.__direction.amountOfDirections):
            if (self.__neighbours[i] != None and self.__neighbours[i].isEmpty()):
                temp[index] = self.__neighbours[i]
                index += 1
        return temp[random.random() * (index - 1)]