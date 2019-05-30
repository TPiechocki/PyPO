#  Copyright (c) 2019. Created by Tomasz Piechocki

from abc import ABC


class Organism(ABC):
    def __init__(self, x, y, world):
        self._x = x
        self._y = y
        self._world = world

        self.__strength = 0
        self.__initiative = 0
        self.__age = 0
        self.__killed = False
        self.__direction = None