#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.animal import Animal

class Fox(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 2
        self._initiative = 1

    def createNewInstance(self, x, y, wrld):
        return Fox(x, y, wrld)

    def action(self):
        field = self._world.getField(self._x, self._y)
        direction = field.getDirection().randomDirection()

        for i in range (0, direction.amountOfDirections()):
            target = field.getNeighbour(direction)
            if (target == None):
                direction = direction.getNextDirection()
                i += 1
                continue
            if target.isEmpty() or target.getOrganism().getStrength() <= self.getStrength():
                self._travel(field, direction)
                return
            else:
                direction.getNextDirection()
                i += 1

    def color(self) -> str:
        return "orange"

    def __repr__(self) -> str:
        return "Lis"