#!/usr/bin/env python
# File: pyqtplot10.py
# Name: D.Saravanan
# Date: 16/07/2023

""" Script to create plot using the PlotWidget in PyQtGraph """

import sys

import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize application's main window."""

    def __init__(self):
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

        # set the axis labels (position and text), style parameters
        styles = {"color": "#dcdcdc", "font-size": "10pt"}
        self.graphWidget.setLabel(
            "left", "Temperature", units="\N{DEGREE SIGN}C", **styles
        )
        self.graphWidget.setLabel("bottom", "Hour", units="H", **styles)

        # set the legend which represents given line
        self.graphWidget.addLegend(offset=(-10, 10))

        # set the background grid for both the x and y axis
        self.graphWidget.showGrid(x=True, y=True)

        # set the axis limits within the specified ranges and padding
        self.graphWidget.setXRange(1, 10, padding=0.1)
        self.graphWidget.setYRange(22, 50, padding=0.1)

    def graphPlot(self, abscissa, ordinate, legend, lcolor, scolor):
        """plot data: abscissa, ordinate values with lines
        drawn using Qt's QPen types & marker '+'"""

        # set line color in hex notation as string, line width in pixels, line style
        lvalue = pg.mkPen(color=lcolor, width=1, style=QtCore.Qt.PenStyle.SolidLine)

        self.graphWidget.plot(
            abscissa,
            ordinate,
            name=legend,
            pen=lvalue,
            symbol="+",
            symbolSize=8,
            symbolBrush=(scolor),
        )


def main():
    """Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments than QApplication([]) is required."""
    app = QtWidgets.QApplication(sys.argv)

    hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
    temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

    window = MainWindow()  # an instance of the class MainWindow
    window.graphPlot(hour, temperature_1, "Sensor 1", "#d81b60", "#004d40")
    window.graphPlot(hour, temperature_2, "Sensor 2", "#1e88e5", "#ffc107")
    window.show()  # windows are hidden by default

    sys.exit(app.exec())  # start the event loop


if __name__ == "__main__":
    main()
