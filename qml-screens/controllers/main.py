from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

from .screen1_controller import Screen1Controller
from .screen2_controller import Screen2Controller


class MainController(QObject):
    # signals
    active_content_changed = pyqtSignal()

    def __init__(self, app):
        super().__init__()

        self._app = app
        self._active_content_controller = None

        self._content_map = {
            "SCREEN1": Screen1Controller(),
            "SCREEN2": Screen2Controller()
        }

    @pyqtProperty(QObject, notify=active_content_changed)
    def active(self):
        return self._active_content_controller

    @active.setter
    def active(self, value):
        if self._active_content_controller != value:
            self._active_content_controller = value
            self.active_content_changed.emit()
    
    @pyqtSlot()
    def closeApplication(self):
        self.shutdown()
        
    def start(self):
        print("start()")
        self.active = self._content_map["SCREEN1"]
        
    def shutdown(self):
        print("shutdown()")
        self.active.deinitialize()
        self._app.quit()
        
    @pyqtSlot(str)
    def changeContent(self, screen_key):
        try:
            new_controller = self._content_map[screen_key]
        except KeyError as ex:
            print('Failed to change to controller {0} (key not found)'.format(screen_key))
            return

        if new_controller == self.active:
            return

        print("Changing to {0}".format(screen_key))

        if self.active is not None:
            self.active.deinitialize()

        self.active = new_controller
        self.active.initialize()
