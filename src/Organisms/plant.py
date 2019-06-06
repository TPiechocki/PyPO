#  Copyright (c) 2019. Created by Tomasz Piechocki

import random

from Organisms.organism import Organism

class Plant(Organism):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._scatter_possibility = 15 # per cents
        self._initiative = 0

    def action(self):
        field = self._world.getField(self._x, self._y)
        direction = field.getDirection()
        field = field.getNeighbour(direction.randomDirection())

        if field is not None and field.isEmpty() and random.randint(0,100) <= self._scatter_possibility:
            new_x, new_y = field.getX(), field.getY()
            self._world.addOrganism(self.createNewInstance(new_x, new_y, self._world))
            self._world.addNotification(repr(self) + ": Roślina się rozprzestrzeniła.")

