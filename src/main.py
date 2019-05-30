#  Copyright (c) 2019. Created by Tomasz Piechocki

from game import Game

import sys
import time
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    window.show()

    Game(window)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()