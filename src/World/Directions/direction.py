#  Copyright (c) 2019. Created by Tomasz Piechocki

from abc import ABC, abstractmethod,ABCMeta
from enum import Enum, EnumMeta


class Direction(metaclass=EnumMeta):
    def __new__(cls, x, coords):
        obj = object.__new__(cls)
        obj._value_ = x
        obj.coords = coords

    def toInt(self):
        return self._value_

    @abstractmethod
    def intToDirection(self, n):
        pass

    @abstractmethod
    def amountOfDirections(self):
        pass

    def getX(self):
        return self._value_[1][0]

    def getY(self):
        return self._value_[1][1]

    @abstractmethod
    def getNextDirection(self):
        pass

    @abstractmethod
    def defaultDirection(self):
        pass

    @abstractmethod
    def randomDirection(self):
        pass
