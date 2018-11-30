from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtCore import QTimer


class CustomPaintedItem(QQuickPaintedItem):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        QTimer.singleShot(100, self.update)

    def paint(self, QPainter):
        QTimer.singleShot(100, self.update)

    def geometryChanged(self, old_geom, new_geom):
        print('OLD: {0} x {1}'.format(old_geom.width(), old_geom.height()))
        print('NEW: {0} x {1}'.format(old_geom.width(), old_geom.height()))
