#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.animal import Animal
from Organisms.plant import Plant

class Hogweed(Plant):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 10

    def createNewInstance(self, x, y, wrld):
        return Hogweed(x, y, wrld)

    def action(self):
        neighbours = self._world.getField(self._x, self._y).getFullNeighbours()
        for neighbour in neighbours:
            if not neighbour.isEmpty() and isinstance(neighbour.getOrganism(), Animal):
                temp = neighbour.getOrganism()

                from Organisms.Animals.cybersheep import CyberSheep
                if not isinstance(temp, CyberSheep):
                    self._world.addNotification(repr(self) + " zatruł " + repr(temp))
                    self._world.getField(temp.getX(), temp.getY()).setOrganism(None)
                    temp.kill()

        super().action()

    def _collision(self, attacker):
        from Organisms.Animals.cybersheep import CyberSheep
        if not isinstance(attacker, CyberSheep):
            self._world.addNotification(repr(attacker) + " został zatruty przez " + repr(self))

            self._world.getField(self._x, self._y).setOrganism(None)
            attacker.kill()
            self.kill()
        else:
            self._world.addNotification(repr(attacker) + " zjadła " + repr(self))

            self._world.setOrganismOnBoard(attacker)
            self.kill()

    def color(self) -> str:
        return "plum"

    def __repr__(self) -> str:
        return "Barszcz Sosnowskiego"