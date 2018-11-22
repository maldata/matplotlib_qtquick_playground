from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot


class Screen2Controller(QObject):
    # signals
    engines_initialized = pyqtSignal()
    screen_changed = pyqtSignal(str)
    dryer_connection_changed = pyqtSignal()
    alert_status_changed = pyqtSignal()
    param_changed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self._qml_file = './screens/screen2.qml'

    def initialize(self):
        print('Initializing screen 2 controller')

    def deinitialize(self):
        print('Deinitializing screen 2 controller')

    def get_qml(self):
        return self._qml_file
