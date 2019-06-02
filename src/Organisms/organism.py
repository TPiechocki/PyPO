#  Copyright (c) 2019. Created by Tomasz Piechocki

from abc import ABC, abstractmethod

from World import world
from World.Directions.direction import Direction


class Organism(ABC):
    _direction: Direction
    _world: world.World

    def __init__(self, x, y, wrld):
        self._x = x
        self._previous_x = x
        self._previous_y = y
        self._y = y
        self._world = wrld

        self._strength = 0
        self._initiative = 0
        self.__age = 0
        self.__killed = False
        self._direction = None

    @abstractmethod
    def createNewInstance(self, x, y, wrld):
        pass

    def _collision(self, attacker):
        """
        Collision of two organisms of different species
        :type attacker: Organism
        :param attacker: organism which attacked
        :return: None
        """
        if attacker.getStrength() < self.getStrength():
            self._world.addNotification("Broniący się " + repr(self) + " zabija " + repr(attacker))
            self._world.setOrganismOnBoard(self)
            attacker.kill()
        else:
            self._world.addNotification("Atakujący " + repr(attacker) + " zabija " + repr(self))
            self._world.setOrganismOnBoard(attacker)
            self.kill()

    def kill(self):
        """
        Set killed flag for organism
        :return: None
        """
        self.__killed = True

    @abstractmethod
    def action(self):
        pass

    def setPreviousXY(self):
        """
        Move organism to the previous location
        :return: None
        """
        self._x = self._previous_x
        self._y = self._previous_y
        field = self._world.getField(self._x, self._y)
        if field.isEmpty():
            field.setOrganism(self)
        else:
            try:
                raise Exception("Organism can't go back to previous location")
            except Exception as error:
                print("Error: " + repr(error) + "\n")

    def changeStrength(self, x):
        """
        Change organism strength
        :param x: Add this value to strength
        :return: None
        """
        self._strength += x

    def addOneAge(self):
        self.__age += 1

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getInitiative(self):
        return self._initiative

    def getAge(self):
        return self.__age

    def getStrength(self):
        return self._strength

    def getDirection(self):
        return self._direction

    def isKilled(self):
        return self.__killed

    def __lt__(self, other):
        if self.getInitiative() != other.getInitiative():
            return self.getInitiative() > other.getInitiative()
        else:
            return self.getAge() > other.getAge()

    def __cmp__(self, other):
        if self.getInitiative() != other.getInitiative():
            return self.getInitiative() - other.getInitiative()
        else:
            return self.getAge() - other.getAge()

    def __repr__(self) -> str:
        return "Nieznany organizm"

    @abstractmethod
    def color(self) -> str:
        pass