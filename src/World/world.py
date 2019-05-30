#  Copyright (c) 2019. Created by Tomasz Piechocki

import sys
import random
from abc import ABC, abstractmethod

from PyQt5 import QtWidgets

class World(ABC):
    def __init__(self, controller, x, y):
        self.__x_size = x
        self.__y_size = y

        self.__entities = []
        self.__player = None

        self.__notifications = []

        self.__fields = []
        for i in range(0, self.__x_size):
            new = []
            for j in range(0, self.__y_size):
                new.append(0)
            self.__fields.append(new)

        self.__fields[5][5] = 10

        self._window = QtWidgets.QMainWindow()
