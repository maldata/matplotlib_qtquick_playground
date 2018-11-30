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
        """
        Overrides QQuickPaintedItem.paint().
        http://doc.qt.io/qt-5/qquickpainteditem.html#paint
        """
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

    def geometryChanged(self, new_geometry, old_geometry):
        """
        Overrides QQuickItem.geometryChanged().
        Must call the base class method.
        http://doc.qt.io/qt-5/qquickitem.html#geometryChanged
        """
        super().geometryChanged(new_geometry, old_geometry)
        old_width = old_geometry.width()
        old_height = old_geometry.height()
        new_width = new_geometry.width()
        new_height = new_geometry.height()

        if (new_width <= 0.0) and (new_height <= 0.0):
            return

        print('OLD: {0} x {1}'.format(old_width, old_height))
        print('NEW: {0} x {1}'.format(new_width, new_height))

        # dpival = self.figure.dpi
        # winch = w / dpival
        # hinch = h / dpival
        # self.figure.set_size_inches(winch, hinch)
        # FigureCanvasAgg.resize_event(self)
        # self.draw_idle()
        # QQuickPaintedItem.geometryChanged(self, new_geometry, old_geometry)
