from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot


class BaseController(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app

    def startup(self):
        pass

    @pyqtSlot()
    def shutdown(self):
        print("Shutting down.")
        self._app.quit()
