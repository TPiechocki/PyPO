#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.plant import Plant

class Dandelion(Plant):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 0

    def createNewInstance(self, x, y, wrld):
        return Dandelion(x, y, wrld)

    def action(self):
        for i in range (0,3):
            super().action()

    def color(self) -> str:
        return "yellow"

    def __repr__(self) -> str:
        return "Mlecz"