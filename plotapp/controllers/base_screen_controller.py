from PyQt5.QtCore import QObject, pyqtSlot


class BaseScreenController(QObject):
    def __init__(self, app):
        super().__init__()

        self._app = app

    def startup(self, qml_engine):
        pass

    @pyqtSlot()
    def shutdown(self):
        print("Shutting down.")
        self._app.quit()
