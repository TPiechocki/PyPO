#  Copyright (c) 2019. Created by Tomasz Piechocki

import random
from abc import ABC

from World.Directions.direction import Direction
from World.Directions.squareDirection import SquareDirection


class Field(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

        self._full_neighbours = None
        self._neighbours = []
        self._direction = None

        self._organism = None

    def color(self):
        if self._organism:
            return self._organism.color()
        else:
            return "white"

    def isEmpty(self):
        return self._organism is None

    def setNeighbours(self, fields, x_size, y_size):
        direction = self._direction.defaultDirection()
        temp_full = 0

        for i in range(0, direction.amountOfDirections()):
            x_temp = self._x + direction.getX()
            y_temp = self._y + direction.getY()
            if 0 <= x_temp < x_size and 0 <= y_temp < y_size:
                self._neighbours[direction._value_[0]] = fields[x_temp][y_temp]
                temp_full += 1
            direction = direction.getNextDirection()

        self._full_neighbours = temp_full

    def setOrganism(self, org):
        self._organism = org

    def getOrganism(self):
        return self._organism

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getDirection(self) -> Direction:
        return self._direction

    def getNeighbour(self, direction):
        return self._neighbours[direction._value_[0]]

    def getFullNeighbours(self):
        index = 0
        temp = [None] * self._full_neighbours
        for i in range(0, self._direction.amountOfDirections):
            if self._neighbours[i] is not None:
                temp[index] = self._neighbours[i]
                index += 1

        return temp

    def randomNeighbour(self):
        full = self.getFullNeighbours()
        return full[random.random() * (self._full_neighbours - 1)]

    def hasEmptyNeighbour(self):
        for i in range(0, self._direction.amountOfDirections()):
            if self._neighbours[i] is not None and self._neighbours[i].isEmpty():
                return True
        return False

    def randomEmptyNeighbour(self):
        index = 0
        temp = [None] * self._full_neighbours
        for i in range(0, self._direction.amountOfDirections()):
            if self._neighbours[i] is not None and self._neighbours[i].isEmpty():
                temp[index] = self._neighbours[i]
                index += 1
        return temp[random.randint(0, index-1)]


class SquareField(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._organism = None
        self._neighbours = [None] * 4
        self._direction = SquareDirection.NORTH
