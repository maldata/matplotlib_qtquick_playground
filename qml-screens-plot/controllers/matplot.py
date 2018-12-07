from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtCore import Qt, QTimer, QVariant, pyqtProperty, pyqtSignal

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

from random import random


class MatplotlibController(QQuickPaintedItem):
    modelChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # A figure contains the axes, legends, titles, labels, etc.
        # The canvas is what the figure gets rendered onto, and can be exported to bytes or a file.
        self._figure = Figure()
        self._canvas = FigureCanvasAgg(self._figure)

        self._axis = self._figure.add_subplot(1, 1, 1)

        self._model = []

        self.modelChanged.connect(self.onDataUpdate)

        # https://stackoverflow.com/questions/19480209/qt-quick-2-paint-method-doesnt-get-called
        # We need to call self.update() once in the constructor and then every time we need a refresh
        # QTimer.singleShot(10, self.update)

    @pyqtProperty(QVariant, notify=modelChanged)
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        variant = value.toVariant()
        if self._model != variant:
            self._model = variant
            self.modelChanged.emit()

    def paint(self, painter):
        """
        Overrides QQuickPaintedItem.paint(). This creates the image in the QML item. The QQuickPaintedItem.update()
        method will schedule a paint request to be processed by the QML Scene Graph when the next frame is rendered.
        The item will only be redrawn if it is visible.

        http://doc.qt.io/qt-5/qquickpainteditem.html#paint
        http://doc.qt.io/qt-5/qquickpainteditem.html#update
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
        # QTimer.singleShot(100, self.update)

    def geometryChanged(self, new_geometry, old_geometry):
        """
        Overrides QQuickItem.geometryChanged(). This runs whenever the QML object's size is changed.
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

        # print('OLD: {0} x {1}'.format(old_width, old_height))
        # print('NEW: {0} x {1}'.format(new_width, new_height))

        # dpival = self.figure.dpi
        # winch = w / dpival
        # hinch = h / dpival
        # self.figure.set_size_inches(winch, hinch)
        # FigureCanvasAgg.resize_event(self)
        # self.draw_idle()
        # QQuickPaintedItem.geometryChanged(self, new_geometry, old_geometry)

    def onDataUpdate(self):
        # Probably want to throttle this a little. Maybe only draw/update once every X milliseconds?
        self._axis.cla()
        x = list(range(len(self.model)))
        self._axis.plot(x, self.model)
        self._canvas.draw()
        self.update()
