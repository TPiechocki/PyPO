#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.animal import Animal

class Sheep(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 4
        self._initiative = 4

    def createNewInstance(self, x, y, wrld):
        return Sheep(x, y, wrld)

    def color(self) -> str:
        return "lightblue"

    def __repr__(self) -> str:
        return "Owca"