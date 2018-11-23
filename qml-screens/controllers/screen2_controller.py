from PyQt5.QtCore import QObject, pyqtProperty


class Screen2Controller(QObject):
    # signals

    def __init__(self):
        super().__init__()

        self._qml_file = './screens/screen2.qml'

    def initialize(self):
        print('Initializing screen 2 controller')

    def deinitialize(self):
        print('Deinitializing screen 2 controller')

    @pyqtProperty(str, constant=True)
    def qml_file(self):
        return self._qml_file
