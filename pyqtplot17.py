#!/usr/bin/env python
# File: pyqtplot17.py
# Name: D.Saravanan
# Date: 23/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys

import numpy as np
import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets

pg.setConfigOptions(antialias=True)


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize qpplication's main window."""

    def __init__(self, xval, wav1, wav2):
        super().__init__()
        self.xval = xval
        self.wav1 = wav1
        self.wav2 = wav2
        self.nval = 0

        # set the size parameters (width, height) pixels
        self.setFixedSize(QtCore.QSize(640, 480))

        # set the central widget of the window
        self.graphWidget = pg.GraphicsLayoutWidget(show=True)
        self.setCentralWidget(self.graphWidget)

        # set the background color using hex notation #121317 as string
        self.graphWidget.setBackground("#121317")

        # widget for generating multi-panel figures
        self.graphLine1 = self.graphWidget.addPlot(row=0, col=0)
        self.graphLine2 = self.graphWidget.addPlot(row=1, col=0)

        # set the axis labels (position and text), style parameters
        styles = {"color": "#dcdcdc", "font-size": "10pt"}
        self.graphLine1.setLabel("left", "sin(x)", **styles)
        self.graphLine1.setLabel("bottom", " ", **styles)
        self.graphLine2.setLabel("left", "cos(x)", **styles)
        self.graphLine2.setLabel("bottom", "x", **styles)

        # set the legend which represents given line
        self.graphLine1.addLegend(offset=(-10, 10), labelTextSize="9pt")
        self.graphLine2.addLegend(offset=(-10, 10), labelTextSize="9pt")

        # set the background grid for both the x and y axis
        self.graphLine1.showGrid(x=True, y=True, alpha=0.5)
        self.graphLine2.showGrid(x=True, y=True, alpha=0.5)

        # graphPlot method call
        self.graphPlot(self.xval, self.wav1, self.wav2)

    def graphPlot(self, xval, wav1, wav2):
        """Method accepts x and y parameters to plot."""

        # set the axis limits within the specified ranges and padding
        self.graphLine1.setXRange(xval[0], xval[-1], padding=0)
        self.graphLine1.setYRange(min(wav1), max(wav1), padding=0.1)

        self.data_line1 = self.graphLine1.plot(
            xval[0:1], wav1[0:1], name="sin(x)", pen=pg.mkPen(color="#fa8775")
        )

        # set the axis limits within the specified ranges and padding
        self.graphLine2.setXRange(xval[0], xval[-1], padding=0)
        self.graphLine2.setYRange(min(wav2), max(wav2), padding=0.1)

        self.data_line2 = self.graphLine2.plot(
            xval[0:1], wav2[0:1], name="cos(x)", pen=pg.mkPen(color="#3574e2")
        )

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_data_line)
        self.timer.start()

    def update_data_line(self):
        """Method uses QTimer to update the data every 50ms."""
        self.nval = self.nval + 1
        self.data_line1.setData(self.xval[0 : self.nval], self.wav1[0 : self.nval])
        self.data_line2.setData(self.xval[0 : self.nval], self.wav2[0 : self.nval])


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    xval = np.linspace(-2 * np.pi, 2 * np.pi, 1000, retstep=False)

    # an instance of the class MainWindow
    window = MainWindow(xval, np.sin(xval), np.cos(xval))
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
