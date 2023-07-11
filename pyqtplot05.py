#!/usr/bin/env python
# File: pyqtplot05.py
# Name: D.Saravanan
# Date: 11/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys

import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize application's main window."""

    def __init__(self, hour, temperature):
        super().__init__()

        # set the size parameters (width, height) pixels
        self.setFixedSize(QtCore.QSize(640, 480))

        # set the central widget of the window
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # set the background color using hex notation #121317 as string
        self.graphWidget.setBackground("#121317")

        # set the main plot title, text color, text size, text weight, text style
        self.graphWidget.setTitle(
            "Temperature Plot", color="#dcdcdc", size="10pt", bold=True, italic=False
        )

        # set the line color in 3-tuple of int values, line width in pixels, line style
        lvalue = pg.mkPen(
            color=(220, 220, 220), width=1, style=QtCore.Qt.PenStyle.SolidLine
        )

        # plot data: x, y values with lines drawn using Qt's QPen types & marker '+'
        self.graphWidget.plot(
            hour, temperature, pen=lvalue, symbol="+", symbolSize=8, symbolBrush=("r")
        )


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

    window = MainWindow(hour, temperature)  # an instance of the class MainWindow
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
