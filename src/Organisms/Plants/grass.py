#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.plant import Plant

class Grass(Plant):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 0

    def createNewInstance(self, x, y, wrld):
        return Grass(x, y, wrld)

    def color(self) -> str:
        return "chartreuse"

    def __repr__(self) -> str:
        return "Trawa"