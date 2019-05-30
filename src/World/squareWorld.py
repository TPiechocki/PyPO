#  Copyright (c) 2019. Created by Tomasz Piechocki

import sys

from PyQt5 import QtWidgets

from World.world import World
from UI.window import UIWindow

class SquareWorld(World):
    def __init__(self, controller, x, y):
        super().__init__(controller, x, y)

        self._window = UIWindow(controller)