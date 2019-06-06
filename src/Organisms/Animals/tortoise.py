#  Copyright (c) 2019. Created by Tomasz Piechocki

import random

from Organisms.animal import Animal

class Tortoise(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 2
        self._initiative = 1

    def createNewInstance(self, x, y, wrld):
        return Tortoise(x, y, wrld)

    def action(self):
        if random.randint(1, 4) is 1:
            super().action()

    def _collision(self, attacker):
        if attacker.getStrength() < 5:
            attacker.setPreviousXY()
            self._world.addNotification(repr(self) + " odbił atak " + repr(attacker))
        else:
            super()._collision(attacker)

    def color(self) -> str:
        return "darkgreen"

    def __repr__(self) -> str:
        return "Żółw"
