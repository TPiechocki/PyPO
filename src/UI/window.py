#  Copyright (c) 2019. Created by Tomasz Piechocki

import copy
import re
import threading
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QAction, QLabel

from Organisms.player import Player
from UI.board import UISquareBoard
from World.Directions.squareDirection import SquareDirection


class UIWindow(QtWidgets.QFrame):
    def __init__(self, controller, x, y):
        super().__init__()

        self.__x = x
        self.__y = y

        """ side panel """
        self.__info = UIInfo(controller)
        self.__board = UISquareBoard(controller, x, y, self)
        self.__notif_label = QtWidgets.QLabel("")
        self.__notification = UINotifications(self.__notif_label)

        self.__layout = QWidget()

        """ field and notifcations """
        self.__vbox = QVBoxLayout()
        self.__vbox.addWidget(self.__board)
        self.__vbox.addStretch()
        self.__vbox.addWidget(self.__notification)

        self.__hbox = QHBoxLayout()
        self.__hbox.addLayout(self.__vbox)
        self.__hbox.addStretch()
        self.__hbox.addWidget(self.__info)

        self.__layout.setLayout(self.__hbox)
        controller.window.setCentralWidget(self.__layout)

        self.__notification.renderNotifications([])
        controller.window.show()

    def displayNotifications(self, messages):
        """
        Display notifications below the board
        :param messages: List of messages to show in order
        :return: None
        """
        self.__notification.renderNotifications(messages)

    def stopNotifications(self):
        """
        Stop displaying notifications
        :return: None
        """
        self.__notification.stopNotifications()

    def drawFields(self, fields):
        buttons = self.__board.getButtons()
        for j in range (0,self.__y):
            for i in range (0, self.__x):
                if isinstance(self.__board, UISquareBoard):
                    string = buttons[i][j].styleSheet()
                    string = re.sub("background-color: \w+;", "background-color: " + fields[i][j].color() + ";", string)
                    buttons[i][j].setStyleSheet(string)
                    buttons[i][j].repaint()

    def setPlayer(self, player):
        self.__info.setPlayer(player)

    def refreshInfo(self):
        self.__info.refreshInfo()

class UIInfo(QFrame):
    """
    Side panel with buttons to control and basic info about immortality
    """
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.__player: Player = None

        self.setMinimumWidth(400)

        self.__new_turn = QPushButton("Nowa tura")
        self.__new_turn.clicked.connect(self.controller.newTurn)

        self.__new_game = QPushButton("Nowa gra")
        self.__new_game.clicked.connect(self.controller.newGame)

        self.__immortality = QPushButton("Nieśmiertelność")
        self.__immortality.clicked.connect(self.controller.setImmortality)

        self.__immo_info = QLabel("")
        self.__immo_info.setFixedHeight(50)
        self.__immo_info.setAlignment(QtCore.Qt.AlignCenter)

        self.__save_game = QPushButton("Zapisz")
        self.__save_game.clicked.connect(self.controller.saveGame)

        self.__load_game = QPushButton("Wczytaj")
        self.__load_game.clicked.connect(self.controller.loadGame)

        self.__dir_up = QAction()
        self.__dir_up.setShortcut(QtCore.Qt.Key_Up)
        self.__dir_up.triggered.connect(lambda: self.controller.changeDirection(SquareDirection.NORTH))
        self.addAction(self.__dir_up)

        self.__dir_right = QAction()
        self.__dir_right.setShortcut(QtCore.Qt.Key_Right)
        self.__dir_right.triggered.connect(lambda: self.controller.changeDirection(SquareDirection.EAST))
        self.addAction(self.__dir_right)

        self.__dir_down = QAction()
        self.__dir_down.setShortcut(QtCore.Qt.Key_Down)
        self.__dir_down.triggered.connect(lambda: self.controller.changeDirection(SquareDirection.SOUTH))
        self.addAction(self.__dir_down)

        self.__dir_left = QAction()
        self.__dir_left.setShortcut(QtCore.Qt.Key_Left)
        self.__dir_left.triggered.connect(lambda: self.controller.changeDirection(SquareDirection.WEST))
        self.addAction(self.__dir_left)

        vbox = QVBoxLayout()

        vbox.addWidget(self.__new_turn)
        vbox.addWidget(self.__immortality)
        vbox.addWidget(self.__immo_info)
        vbox.addWidget(self.__new_game)
        vbox.addWidget(self.__save_game)
        vbox.addWidget(self.__load_game)
        vbox.addStretch()

        self.setLayout(vbox)

    def setPlayer(self, player):
        self.__player = player

    def refreshInfo(self):
        if (self.__player.isImmortalityReady() and not self.__player.isKilled()):
            self.__immortality.setEnabled(True)
        else:
            self.__immortality.setEnabled(False)

        self.__immo_info.setText(self.__player.immortalityStatus())


class UINotifications(QFrame, threading.Thread):
    """
    Notifications which are displayed below the board in another thread
    """
    def __init__(self, label, parent=None):
        super().__init__(parent)

        hbox = QHBoxLayout()
        self.__text = label

        hbox.addWidget(self.__text)

        self.worker = None
        self.worker_handle = threading.Event()
        self.finish_work = False

        self.messages = []

        self.setLayout(hbox)

    def clearLabel(self):
        self.__text.setText("")

    def work(self, handle):
        """
        Worker function for notifications thread
        :param handle: threading.Event() object so it's possible to pause sleep time
        :return: None
        """
        try:
            while len(self.messages) and not self.finish_work:
                self.__text.setText(self.messages.pop(0))
                handle.wait(timeout=2)
            self.__text.clear()
            self.finish_work = False
        except:
            pass

    def renderNotifications(self, messages):
        """
        Render given notifications with 'work' function
        :param messages: List of messages to display
        :return: None
        """
        self.stopNotifications()

        self.messages = messages
        self.finish_work = False
        self.worker = threading.Thread(target=self.work, args=(self.worker_handle,))
        self.worker.start()

    def stopNotifications(self):
        """
        Stop displaying notifications
        :return: None
        """
        if self.worker and self.worker.isAlive():
            self.finish_work = True
            self.worker_handle.set()
            while self.finish_work or\
                    self.worker.isAlive():
                time.sleep(0.001)

        self.worker_handle.clear()
