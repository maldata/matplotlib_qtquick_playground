from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtCore import Qt, QTimer

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

from random import random

class MatplotlibController(QQuickPaintedItem):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self._figure = Figure()
        self._canvas = FigureCanvasAgg(self._figure)
        
        # https://stackoverflow.com/questions/19480209/qt-quick-2-paint-method-doesnt-get-called
        # We need to call self.update() once in the constructor and then every time we need a refresh
        QTimer.singleShot(10, self.update)
        
    def paint(self, painter):
        green_color = QColor("#007430")
        brush = QBrush(green_color)

        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        width = 20 + (random() * 50)
        height = 20 + (random() * 50)
        x = 10 + (random() * 100)
        y = 10 + (random() * 100)
        
        painter.drawRoundedRect(x, y, width, height, 5, 5)
        QTimer.singleShot(100, self.update)
