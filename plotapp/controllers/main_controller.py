import random
from PyQt5.QtCore import pyqtSignal, pyqtProperty, pyqtSlot, QObject


class MainController(QObject):
    label_changed = pyqtSignal()

    def __init__(self, app):
        super().__init__()

        self._app = app
        self._qml_engine = None
        self._label = 'whatever'

    def startup(self, qml_engine):
        print('Main controller startup')
        self._qml_engine = qml_engine

        main_window = self._qml_engine.rootObjects()[0]
        main_window.show()

        # TODO: If we have other screens, we'd probably do this there. findChild() can be called on
        # any QML object that was loaded with the QMLEngine.load() method.
        fig = main_window.findChild(QObject, "figure").getFigure()
        ax = fig.add_subplot(111)
        ax.plot([1,2,3,4], [5,6,7,8])

    @pyqtSlot()
    def shutdown(self):
        print("Shutting down.")
        self._app.quit()

    @pyqtProperty(str, notify=label_changed)
    def label(self):
        return self._label

    @pyqtSlot()
    def generate_data(self):
        data = [random.random() for i in range(10)]
        print(data)
