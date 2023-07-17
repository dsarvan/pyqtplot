#!/usr/bin/env python
# File: pyqtplot11.py
# Name: D.Saravanan
# Date: 17/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys
from random import randint

import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize application's main window."""

    def __init__(self, xval, yval):
        super().__init__()
        self.xval = xval
        self.yval = yval

        # set the size parameters (width, height) pixels
        self.setFixedSize(QtCore.QSize(640, 480))

        # set the central widget of the window
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # set the background color using hex notation #121317 as string
        self.graphWidget.setBackground("#121317")

        # set the main plot title, text color, text size, text weight, text style
        self.graphWidget.setTitle(
            "Updating Plot", color="#dcdcdc", size="10pt", bold=True, italic=False
        )

        # set the axis labels (position and text), style parameters
        styles = {"color": "#dcdcdc", "font-size": "10pt"}
        self.graphWidget.setLabel("left", "y-value", **styles)
        self.graphWidget.setLabel("bottom", "x-value", **styles)

        # set the legend which represents given line
        self.graphWidget.addLegend()

        # set the background grid for both the x and y axis
        self.graphWidget.showGrid(x=True, y=True, alpha=0.5)

        # set line color in hex notation as string, line width in pixels, line style
        lvalue = pg.mkPen(color="#77ab56", width=1, style=QtCore.Qt.PenStyle.SolidLine)

        # plot data: x, y values with lines drawn using Qt's QPen types
        self.data_line = self.graphWidget.plot(self.xval, self.yval, pen=lvalue)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_data_line)
        self.timer.start()

    def update_data_line(self):
        """Method uses QTimer to update the data every 50ms."""

        self.xval = self.xval[1:]
        self.xval.append(self.xval[-1] + 1)

        self.yval = self.yval[1:]
        self.yval.append(randint(0, 100))

        self.data_line.setData(self.xval, self.yval)


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    xval = list(range(100))
    yval = [randint(0, 100) for _ in xval]

    window = MainWindow(xval, yval)  # an instance of the class MainWindow
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
