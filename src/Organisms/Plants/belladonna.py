#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.plant import Plant

class Belladonna(Plant):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)
        self._strength = 99

    def createNewInstance(self, x, y, wrld):
        return Belladonna(x, y, wrld)

    def _collision(self, attacker):
        self._world.addNotification(repr(attacker) + " został zatruty przez " + repr(self))
        self._world.getField(self._x, self._y).setOrganism(None)
        attacker.kill()
        self.kill()

    def color(self) -> str:
        return "darkmagenta"

    def __repr__(self) -> str:
        return "Wilcza jagoda"