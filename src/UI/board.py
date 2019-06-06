#  Copyright (c) 2019. Created by Tomasz Piechocki

from functools import partial
from abc import ABCMeta

from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton


class UIBoard(QFrame):
    __metaclass__ = ABCMeta

    GRID_BORDER = 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self._rows = 0
        self._cols = 0

        self._buttons = None

        self._player = None

    def getButtons(self):
        return self._buttons


class UISquareBoard(UIBoard):
    def __init__(self, controller, x, y, parent=None):
        super().__init__(parent)

        self.setMaximumWidth(1000)
        self.setMinimumWidth(800)
        self.setFixedHeight(650)

        self._rows = y
        self._cols = x

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setVerticalSpacing(0)
        layout.setVerticalSpacing(0)

        self._buttons = []
        for j in range(0, self._cols):
            col = []
            for i in range(0, self._rows):
                col.append(0)
            self._buttons.append(col)

        for j in range(0, self._rows):
            for i in range(self._cols):
                button = QPushButton()

                top = self.GRID_BORDER
                bot = self.GRID_BORDER
                left = self.GRID_BORDER
                right = self.GRID_BORDER

                if i == 0:
                    left *= 2
                elif i == self._cols - 1:
                    right *= 2
                if j == 0:
                    top *= 2
                elif j == self._rows - 1:
                    bot *= 2
                string = "* {" \
                         "border-top: " + str(top) + "px solid black; " \
                            "border-bottom: " + str(bot) + "px solid black; " \
                            "border-left: " + str(left) + "px solid black; " \
                            "border-right: " + str(right) + "px solid black; " \
                            "background-color: white; " \
                            "height: 100%" \
                            "}"
                button.setStyleSheet(string)

                layout.addWidget(button, j, i)

                self._buttons[i][j] = button
                self._buttons[i][j].clicked.connect(partial(controller.addOrganism, i, j))

        self.setLayout(layout)
