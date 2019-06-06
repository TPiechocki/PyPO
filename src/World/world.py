#  Copyright (c) 2019. Created by Tomasz Piechocki

import random
from abc import ABC, abstractmethod

from PyQt5 import QtWidgets


class World(ABC):
    # noinspection PyTypeChecker
    def __init__(self, x, y):
        self.__x_size = x
        self.__y_size = y

        self.__entities = []
        self.__hogweeds = []
        self.__player = None

        self.__notifications = []

        self._fields = []
        for i in range(0, self.__x_size):
            new = []
            for j in range(0, self.__y_size):
                new.append(None)
            self._fields.append(new)

        self._window = QtWidgets.QMainWindow()

    def setNeighbours(self):
        """
        Set neighbours for all of board tiles
        :return: None
        """
        for j in range(0, self.__y_size):
            for i in range(0, self.__x_size):
                if self._fields[i][j]:
                    self._fields[i][j].setNeighbours(self._fields, self.__x_size, self.__y_size)

    def makeTurn(self):
        """
        Make turn
        :return: None
        """
        self._window.stopNotifications()
        self.clearNotifications()
        limit = len(self.__entities)

        self.__entities.sort()
        for i in range(0, limit):
            if not self.__entities[i].isKilled():
                self.__entities[i].addOneAge()
                self.__entities[i].action()

        for i in self.__entities:
            if i.isKilled():
                self.__entities.remove(i)

        for i in self.__hogweeds:
            if i.isKilled():
                self.__hogweeds.remove(i)

        #self._window.repaint()
        self.displayWorld()
        self.displayNotifications()
        self._window.refreshInfo()

    def displayWorld(self):
        """
        Display world fields
        :return: None
        """
        self._window.drawFields(self._fields)

    def refreshInfo(self):
        """
        Refresh info about immortality
        :return: None
        """
        self._window.refreshInfo()

    def addOrganism(self, org):
        """
        Add organism to the game
        :param org: organism to be added
        :return: None
        """
        self.__entities.append(org)
        if self._fields[org.getX()][org.getY()].isEmpty():
            self._fields[org.getX()][org.getY()].setOrganism(org)

        from Organisms.Plants.hogweed import Hogweed
        if isinstance(org, Hogweed):
            self.__hogweeds.append(org)

    def setOrganismOnBoard(self, org):
        """
        Set organism on the field
        :param org: organism to be set
        :return: None
        """
        self._fields[org.getX()][org.getY()].setOrganism(org)

    def setPlayer(self, player):
        """
        Set player to the board
        :param player: player organism
        :return: None
        """
        self.__player = player
        self._window.setPlayer(player)

    def getPlayer(self):
        """
        Get active player
        :return: player
        """
        return self.__player

    def getField(self, x, y) -> 'Field':
        """
        Get field object from the board
        :param x: x coordinate
        :param y: y coordinate
        :return: Field on this coordinates
        """
        return self._fields[x][y]

    def getRandomEmptyField(self) -> 'Field':
        """
        Get random empty field
        :return: Random empty field
        """
        while True:
            x = random.randint(0, self.__x_size - 1)
            y = random.randint(0, self.__y_size - 1)
            fld = self.getField(x, y)
            if fld and fld.isEmpty():
                break
        return fld

    def getSizeX(self):
        return self.__x_size

    def getSizeY(self):
        return self.__y_size

    def getHogweeds(self):
        return self.__hogweeds

    """ Notifications """

    def displayNotifications(self):
        """
        Display notifications
        :return: None
        """
        self._window.displayNotifications(self.__notifications)

    def stopNotifications(self):
        """
        Stop displaying notifications without clearing
        :return: None
        """
        self._window.stopNotifications()

    def clearNotifications(self):
        """
        Clear messages in notifications list
        :return: None
        """
        self._window.stopNotifications()
        self.__notifications.clear()

    def addNotification(self, msg):
        """
        Add notification at the end
        :param msg: Message text
        :return: None
        """
        self.__notifications.append(msg)

    def addPriorityNotification(self, msg):
        """
        Add notification at the beginning of the list
        :param msg: Message text
        :return: None
        """
        self._window.stopNotifications()
        self.__notifications.insert(0, msg)
        self._window.displayNotifications(self.__notifications)

    @abstractmethod
    def recreateWindow(self, controller):
        pass

    def __getstate__(self):
        return (self.__x_size, self.__y_size, self.__entities, self.__player, self._fields, self.__notifications,
                self.__hogweeds)

    def __setstate__(self, state):
        self.__x_size, self.__y_size, self.__entities, self.__player, self._fields,\
        self.__hogweeds, self.__notifications = state