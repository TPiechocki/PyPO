#  Copyright (c) 2019. Created by Tomasz Piechocki

import sys

from PyQt5 import QtWidgets

from game import Game


def main():
    app = QtWidgets.QApplication(sys.argv)

    # noinspection PyCallByClass,PyTypeChecker
    QtWidgets.QApplication.setStyle("Fusion")

    window = QtWidgets.QMainWindow()
    window.setWindowTitle("sig")

    Game(window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
