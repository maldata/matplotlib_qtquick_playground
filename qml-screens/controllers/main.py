from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot


class MainController(QObject):
    # signals
    engines_initialized = pyqtSignal()
    screen_changed = pyqtSignal(str)
    dryer_connection_changed = pyqtSignal()
    alert_status_changed = pyqtSignal()
    param_changed = pyqtSignal()

    def __init__(self, app):
        super().__init__()

        self._app = app
        self._active_content_controller = None

    # property exposing the current active controller to allow binding
    # even though it technically changes, it's marked as constant
    # so binding errors aren't raised when the controller changes
    # before switching to a new screen
    @pyqtProperty(QObject, constant=True)
    def active(self):
        return self._active_content_controller
    
    @pyqtSlot()
    def closeApplication(self):
        self.shutdown()
        
    def start(self):
        print("start()")
        
    def shutdown(self):
        print("shutdown()")
    
        self._app.quit()
        
    @pyqtSlot(str)
    def changeContent(self, screen_key):
        print("Changing to {0}".format(screen_key))
        
