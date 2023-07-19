#!/usr/bin/env python
# File: pyqtplot13.py
# Name: D.Saravanan
# Date: 19/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys

import numpy as np
import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize application's main window."""

    def __init__(self, xval, yval, step):
        super().__init__()
        self.xval = xval
        self.yval = yval
        self.step = step

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

        # graphPlot method call
        self.graphPlot(self.xval, self.yval)

    def graphPlot(self, xval, yval):
        """Method accepts x and y parameters to plot."""

        # set the axis limits within the specified ranges and padding
        self.graphWidget.setXRange(xval[0], xval[-1], padding=0)
        self.graphWidget.setYRange(min(yval), max(yval), padding=0.1)

        # set the line color in 3-tuple of int values, line width in pixels, line style
        lvalue = pg.mkPen(color="#77ab56", width=1, style=QtCore.Qt.PenStyle.SolidLine)

        # plot data: x, y values with lines drawn using Qt's QPen types
        self.data_line = self.graphWidget.plot(xval, yval, pen=lvalue)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_data_line)
        self.timer.start()

    def update_data_line(self):
        """Method uses QTimer to update the data every 50ms."""

        self.xval = np.linspace(self.xval[1], self.xval[-1] + self.step, 1000)
        self.yval = np.sin(self.xval)

        # set the axis limits within the specified ranges and padding
        self.graphWidget.setXRange(self.xval[0], self.xval[-1], padding=0)
        self.graphWidget.setYRange(min(self.yval), max(self.yval), padding=0.1)

        self.data_line.setData(self.xval, self.yval)


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    xval = np.linspace(-2 * np.pi, 2 * np.pi, 1000, retstep=True)

    # an instance of the class MainWindow
    window = MainWindow(xval[0], np.sin(xval[0]), xval[1])
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
