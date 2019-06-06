#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.plant import Plant

class Guarana(Plant):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 0

    def createNewInstance(self, x, y, wrld):
        return Guarana(x, y, wrld)

    def _collision(self, attacker):
        self._world.addNotification("Atakujący " + repr(attacker) + " zjada " +
                                    repr(self) + ". Siła atakującego wzrosła o 3.")
        self._world.setOrganismOnBoard(attacker)
        attacker.changeStrength(3)
        self.kill()
        

    def color(self) -> str:
        return "red"

    def __repr__(self) -> str:
        return "Guarana"