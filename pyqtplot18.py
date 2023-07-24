#!/usr/bin/env python
# File: pyqtplot18.py
# Name: D.Saravanan
# Date: 24/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys

import numpy as np
import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets

pg.setConfigOptions(antialias=True)


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize qpplication's main window."""

    def __init__(self, xval, yval, zval):
        super().__init__()
        self.xval = xval
        self.yval = yval
        self.zval = zval
        self.n = 0

        # set the size parameters (width, height) pixels
        self.setFixedSize(QtCore.QSize(640, 480))

        # set the central widget of the window
        self.graphWidget = pg.GraphicsLayoutWidget(show=True)
        self.setCentralWidget(self.graphWidget)

        # set the background color using hex notation #121317 as string
        self.graphWidget.setBackground("#121317")

        # set the title of plot window
        self.graphWidget.setWindowTitle("Lorenz attractor")

        # widget for generating multi-panel figures
        self.graphLine1 = self.graphWidget.addPlot(row=0, col=0)
        self.graphLine2 = self.graphWidget.addPlot(row=0, col=1)
        self.graphLine3 = self.graphWidget.addPlot(row=0, col=2)

        # turn off axis (spines, tick labels, axis labels and grid)
        for graphLine in (self.graphLine1, self.graphLine2, self.graphLine3):
            graphLine.hideAxis("left")
            graphLine.hideAxis("bottom")

        # graphPlot method call
        self.graphPlot(self.xval, self.yval, self.zval)

    def graphPlot(self, xval, yval, zval):
        """Method accepts x and y parameters to plot."""

        self.data_line1 = self.graphLine1.plot(
            x=xval[0:1], y=zval[0:1], pen=pg.mkPen(color="#dcdcdc")
        )
        self.data_line2 = self.graphLine2.plot(
            x=yval[0:1], y=zval[0:1], pen=pg.mkPen(color="#dcdcdc")
        )
        self.data_line3 = self.graphLine3.plot(
            x=yval[0:1], y=xval[0:1], pen=pg.mkPen(color="#dcdcdc")
        )

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_data_line)
        self.timer.start()

    def update_data_line(self):
        """Method uses QTimer to update the data every 50ms."""
        self.n = self.n + 1
        self.data_line1.setData(self.xval[0 : self.n], self.zval[0 : self.n])
        self.data_line2.setData(self.yval[0 : self.n], self.zval[0 : self.n])
        self.data_line3.setData(self.yval[0 : self.n], self.xval[0 : self.n])


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    N = 5000
    DELT = 0.01
    SIGMA, BETA, RHO = 10.0, 8.0 / 3.0, 28.0

    xval, yval, zval = [np.ones(N) for _ in range(3)]

    for n in range(N - 1):
        xval[n + 1] = DELT * (SIGMA * (yval[n] - xval[n])) + xval[n]
        yval[n + 1] = DELT * (xval[n] * (RHO - zval[n]) - yval[n]) + yval[n]
        zval[n + 1] = DELT * (xval[n] * yval[n] - BETA * zval[n]) + zval[n]

    # an instance of the class MainWindow
    window = MainWindow(xval, yval, zval)
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
