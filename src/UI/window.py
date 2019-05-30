#  Copyright (c) 2019. Created by Tomasz Piechocki

import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel, QInputDialog


class UIWindow(QtWidgets.QFrame):
    def __init__(self, controller):
        super().__init__()

        """ side panel """
        self.__info = UIInfo(controller)
        self.__board = None
        self.__notification = UINotifications()

        self.__layout = QWidget()

        """ field and notifcations """
        self.__vbox = QVBoxLayout()
        self.__vbox.addStretch()
        self.__vbox.addWidget(self.__notification)

        self.__hbox = QHBoxLayout()
        self.__hbox.addLayout(self.__vbox)
        self.__hbox.addStretch()
        self.__hbox.addWidget(self.__info)

        self.__layout.setLayout(self.__hbox)
        controller.window.setCentralWidget(self.__layout)


class UIInfo(QFrame):
    def __init__(self, controller ,parent=None):
        super().__init__(parent)
        self.controller = controller;

        self.__new_turn = QPushButton("Nowa tura")

        self.__new_game = QPushButton("Nowa gra")
        self.__new_game.clicked.connect(self.newGame)

        self.__immortality = QPushButton("Nieśmiertelność")

        self.__save_game = QPushButton("Zapisz")

        self.__load_game = QPushButton("Wczytaj")


        vbox = QVBoxLayout()

        vbox.addWidget(self.__new_turn)
        vbox.addWidget(self.__immortality)
        vbox.addSpacing(40)
        vbox.addWidget(self.__new_game)
        vbox.addWidget(self.__save_game)
        vbox.addWidget(self.__load_game)
        vbox.addStretch()

        self.setLayout(vbox)

    def newGame(self):
        self.controller.newGame()


class UINotifications(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        hbox = QHBoxLayout()
        self.__text = QtWidgets.QLabel("Hello World")

        hbox.addWidget(self.__text)

        self.setLayout(hbox)