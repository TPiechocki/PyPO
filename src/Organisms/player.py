#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.animal import Animal
from World.Directions.squareDirection import SquareDirection


class Player(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 5
        self._initiative = 4
        self.__immortality_end = -10   # age at which immortality will end
        self._direction = SquareDirection.NORTH

    def createNewInstance(self, x, y, wrld):
        return Player(x, y, wrld)

    def setDirection(self, dir):
        """
        Set player direction
        :param dir: direction - enum Direction
        :return: None
        """
        self._direction = dir
        self._world.addPriorityNotification("Zmieniono kierunek")

    def activateImmortality(self):
        """
        Activate immortality if possible
        :return: None
        """
        if self.__immortality_end < self._age-5:
            self.__immortality_end = self._age + 5
            self._world.addPriorityNotification("Aktywowano nieśmiertelność")
        elif self.__immortality_end >= self._age:
            self._world.addPriorityNotification("Nieśmiertelność jeszcze aktywna przez " +
                                                repr(self.__immortality_end - self._age) + " tur.")
        else:
            self._world.addPriorityNotification("Nie możesz jeszcze aktywować nieśmiertelności. Możliwe za " + repr(
                        self.__immortality_end + 5 - self._age + 1) + " tur.")

    def isImmortalityReady(self):
        """
        Immortality status
        :return: True if can be activated
        """
        return self.__immortality_end < self._age - 5

    def immortalityStatus(self):
        """
        Get status info about immortality
        :return: string with info
        """
        if self.__immortality_end < self._age-5:
            return ""
        elif self.__immortality_end >= self._age:
            return "Nieśmiertelność jeszcze aktywna przez " + repr(self.__immortality_end - self._age) + " tur."
        else:
            return "Nie możesz jeszcze aktywować nieśmiertelności.\nMożliwe za " + repr(self.__immortality_end +
                                                                                   5 - self._age + 1) + " tur."

    def kill(self):
        """
        Survive if immortality is active
        :return: None
        """
        if self.__immortality_end >= self._age:
            self._world.addNotification("Ale dzięki nieśmiertelności człowiek przeżył.")
            if self._world.getField(self._x, self._y).isEmpty():
                self._world.setOrganismOnBoard(self)
            else:
                field = self._world.getField(self._x, self._y)
                target = field.randomEmptyNeighbour()
                self._x = target.getX()
                self._y = target.getY()
                target.setOrganism(self)
        else:
            super().kill()

    def action(self):
        """
        Travel without random direction
        :return: None
        """
        field = self._world.getField(self._x, self._y)
        self._travel(field, self._direction)

    def color(self) -> str:
        return "black"

    def __repr__(self) -> str:
        return "Człowiek"