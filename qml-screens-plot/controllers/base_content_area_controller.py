from PySide2.QtCore import QObject, Property


class BaseContentAreaController(QObject):
    # signals

    def __init__(self, qml_file):
        super().__init__()

        self._qml_file = qml_file

    def initialize(self):
        raise NotImplementedError

    def deinitialize(self):
        raise NotImplementedError

    @Property(str, constant=True)
    def qml_file(self):
        return self._qml_file
