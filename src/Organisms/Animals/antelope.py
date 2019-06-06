#  Copyright (c) 2019. Created by Tomasz Piechocki

import random

from Organisms.animal import Animal

class Antelope(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 4
        self._initiative = 4

    def action(self):
        field = self._world.getField(self._x, self._y)
        direction = field.getDirection().randomDirection()

        for i in range (0,2):
            if self.isKilled():
                break
            field = self._world.getField(self._x, self._y)
            self._travel(field, direction)

    def _collision(self, attacker):
        if random.randint(0,1) is 0:
            super()._collision(attacker)
        else:
            self._world.setOrganismOnBoard(attacker)
            field = self._world.getField(self._x, self._y)
            target = field.randomEmptyNeighbour()

            self._x = target.getX()
            self._y = target.getY()
            target.setOrganism(self)

    def createNewInstance(self, x, y, wrld):
        return Antelope(x, y, wrld)

    def color(self) -> str:
        return "wheat"

    def __repr__(self) -> str:
        return "Antylopa"