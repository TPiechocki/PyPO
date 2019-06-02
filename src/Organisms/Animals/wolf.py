#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.animal import Animal

class Wolf(Animal):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 9
        self._initiative = 5

    def createNewInstance(self, x, y, wrld):
        return Wolf(x, y, wrld)

    def color(self) -> str:
        return "gray"

    def __repr__(self) -> str:
        return "Wilk"




