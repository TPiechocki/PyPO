#  Copyright (c) 2019. Created by Tomasz Piechocki

import random

from enum import Enum

from World.Directions.direction import Direction


class SquareDirection(Direction, Enum):
    __metaclass__ = Enum

    NORTH = 0, (0, -1)
    EAST = 1, (1, 0)
    SOUTH = 2, (0, 1)
    WEST = 3, (-1, 0)
    NONE = -1, (0, 0)

    def __new__(cls, value, coords):
        obj = object.__new__(cls)
        obj._value_ = (value, coords)
        obj.vector = coords
        return obj

    def intToDirection(self, n):
        return {
            0: SquareDirection.NORTH,
            1: SquareDirection.EAST,
            2: SquareDirection.SOUTH,
            3: SquareDirection.WEST,
            -1: SquareDirection.NONE
        }.get(n, -1)  # default is NONE direction

    def getNextDirection(self):
        return {
            SquareDirection.NORTH: SquareDirection.EAST,
            SquareDirection.EAST: SquareDirection.SOUTH,
            SquareDirection.SOUTH: SquareDirection.WEST,
            SquareDirection.WEST: SquareDirection.NORTH,

        }.get(self, self.defaultDirection())

    def defaultDirection(self):
        return SquareDirection.NORTH

    def randomDirection(self):
        return self.intToDirection(random.randint(0,3))

    def amountOfDirections(self):
        return 4


