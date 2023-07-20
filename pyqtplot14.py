#!/usr/bin/env python
# File: pyqtplot14.py
# Name: D.Saravanan
# Date: 20/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys

import numpy as np
import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets

pg.setConfigOptions(antialias=True)


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize application's main window."""

    def __init__(self, xval, yval):
        super().__init__()
        self.xval = xval
        self.yval = yval
        self.nval = 0

        # set the size parameters (width, height) pixels
        self.setFixedSize(QtCore.QSize(640, 480))

        # set the central widget of the window
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # set the background color using hex notation #121317 as string
        self.graphWidget.setBackground("#121317")

        # set the main plot title, text color, text size, text weight, text style
        self.graphWidget.setTitle(
            "Sine wave", color="#dcdcdc", size="10pt", bold=True, italic=False
        )

        # set the axis labels (position and text), style parameters
        styles = {"color": "#dcdcdc", "font-size": "10pt"}
        self.graphWidget.setLabel("left", "sin(x)", **styles)
        self.graphWidget.setLabel("bottom", "x", **styles)

        # set the background grid for both the x and y axis
        self.graphWidget.showGrid(x=True, y=True, alpha=0.5)

        # set the axis limits within the specified ranges and padding
        self.graphWidget.setXRange(self.xval[0], self.xval[-1], padding=0)
        self.graphWidget.setYRange(min(self.yval), max(self.yval), padding=0.1)

        # set the line color in 3-tuple of int values, line width in pixels, line style
        lvalue = pg.mkPen(color="#77ab56", width=1, style=QtCore.Qt.PenStyle.SolidLine)

        # plot data: x, y values with lines drawn using Qt's QPen types
        self.data_line = self.graphWidget.plot(
            self.xval[0:1], self.yval[0:1], pen=lvalue
        )

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_data_line)
        self.timer.start()

    def update_data_line(self):
        """Method uses QTimer to update the data every 50ms."""
        self.nval = self.nval + 1
        self.data_line.setData(self.xval[0 : self.nval], self.yval[0 : self.nval])


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    xval = np.linspace(-2 * np.pi, 2 * np.pi, 1000, retstep=False)

    window = MainWindow(xval, np.sin(xval))  # an instance of the class MainWindow
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
