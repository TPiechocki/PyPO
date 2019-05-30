#  Copyright (c) 2019. Created by Tomasz Piechocki

from abc import ABC, abstractmethod


class Direction(ABC):
    amountOfDirections = 0

    def __new__(cls, int, coords):
        obj = object.__new__(cls)
        obj._value_ = int
        obj.coords = coords


    def toInt(self):
        return self.__int

    @abstractmethod
    def intToDirection(self, n):
        pass

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    @abstractmethod
    def getNextDirection(self):
        pass

    @abstractmethod
    def defaultDirection(self):
        pass

    @abstractmethod
    def randomDirection(self):
        pass