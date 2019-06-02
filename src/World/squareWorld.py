#  Copyright (c) 2019. Created by Tomasz Piechocki

from UI.window import UIWindow
from World.Field.field import SquareField
from World.world import World


class SquareWorld(World):
    def __init__(self, controller, x, y):
        super().__init__(x, y)

        for j in range (0, self.getSizeY()):
            for i in range(0, self.getSizeX()):
                self._fields[i][j] = SquareField(i, j)
        self.setNeighbours()

        self._window = UIWindow(controller, x, y)
