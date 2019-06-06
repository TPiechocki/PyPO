#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.animal import Animal
from World.Directions.squareDirection import SquareDirection


class CyberSheep(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 11
        self._initiative = 4

    def createNewInstance(self, x, y, wrld):
        return CyberSheep(x, y, wrld)

    def action(self):
        hogweeds = self._world.getHogweeds()
        if len(hogweeds) is 0:
            super().action()
        else:
            field = self._world.getField(self.getX(), self.getY())

            target: Animal = min(hogweeds, key=lambda x:
                abs(self.getX() - x.getX()) + abs(self.getY() - x.getY()))
            if self.getX() > target.getX():
                direction = SquareDirection.WEST
            elif self.getX() < target.getX():
                direction = SquareDirection.EAST
            elif self.getY() > target.getY():
                direction = SquareDirection.NORTH
            else:
                direction = SquareDirection.SOUTH
            self._travel(field, direction)

    def color(self) -> str:
        return "chocolate"

    def __repr__(self) -> str:
        return "Cyberowca"