import random
from PyQt5.QtCore import pyqtSignal, pyqtProperty, pyqtSlot, QObject


class WindowController(QObject):
    label_changed = pyqtSignal()

    def __init__(self, app):
        super().__init__()

        self._app = app
        self._qml_engine = None
        self._label = 'whatever'
        self._figure = None
        self._ax = None

        self._data = ([], [])

    def startup(self, qml_engine):
        print('Main controller startup')
        self._qml_engine = qml_engine

        main_window = self._qml_engine.rootObjects()[0]
        main_window.show()

        # TODO: If we have other screens, we'd probably do this there. findChild() can be called on
        # any QML object that was loaded with the QMLEngine.load() method.
        self._figure = main_window.findChild(QObject, "figure").getFigure()
        self._ax = self._figure.add_subplot(111)

    @pyqtSlot()
    def shutdown(self):
        print("Shutting down.")
        self._app.quit()

    @pyqtProperty(str, notify=label_changed)
    def label(self):
        return self._label

    @pyqtSlot()
    def generate_data(self):
        x = [random.random() for i in range(10)]
        x.sort()
        y = [random.random() for i in range(10)]

        self._data = (x, y)
        
        self._ax.clear()
        self._ax.plot(x, y)
        self._figure.canvas.draw_idle()

    @pyqtSlot()
    def append_data(self):
        x = self._data[0]
        y = self._data[1]
        
        x_offset = max(x) + 0.1
        new_x = [random.random() + x_offset for i in range(10)]
        new_x.sort()
        
        new_y = [random.random() for i in range(10)]
        
        x = x + new_x
        y = y + new_y

        self._data = (x, y)
        
        self._ax.clear()
        self._ax.plot(x, y)
        self._figure.canvas.draw_idle()
