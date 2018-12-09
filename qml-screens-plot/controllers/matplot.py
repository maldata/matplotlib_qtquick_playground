from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtGui import QColor, QBrush, QPainter, QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer, QVariant, pyqtProperty, pyqtSignal, QPoint

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

        self._width_px = 0
        self._height_px = 0

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
        try:
            # image_bytes_argb = self._canvas.tostring_argb()
            # It's not clear what the deal is here... this is supposedly in rgba order, but we specify ARGB32
            # as the format? If it were an endianness issue, it'd need to be ABGR, not ARGB...?
            image_bytes_rgba = self._canvas.buffer_rgba()
        except AttributeError:
            # If canvas.draw() hasn't been called yet, it'll fail to find the renderer... just move on.
            return

        image = QImage(image_bytes_rgba, self._width_px, self._height_px, QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(image)
        image_rect = image.rect()
        painter.eraseRect(image_rect)
        painter.drawPixmap(QPoint(0, 0), pixmap)

    def geometryChanged(self, new_geometry, old_geometry):
        """
        Overrides QQuickItem.geometryChanged(). This runs whenever the QML object's size is changed.
        Must call the base class method.
        http://doc.qt.io/qt-5/qquickitem.html#geometryChanged
        """
        super().geometryChanged(new_geometry, old_geometry)
        self._width_px = new_geometry.width()
        self._height_px = new_geometry.height()

        if (self._width_px <= 0.0) and (self._height_px <= 0.0):
            return

        dpi = self._figure.get_dpi()
        width_inch = self._width_px / dpi
        height_inch = self._height_px / dpi
        self._figure.set_size_inches(width_inch, height_inch)

    def onDataUpdate(self):
        # Probably want to throttle this a little. Maybe only draw/update once every X milliseconds?
        self._axis.cla()
        x = list(range(len(self.model)))
        self._axis.plot(x, self.model)
        self._canvas.draw()
        self.update()
