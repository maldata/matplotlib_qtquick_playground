from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self):
        super().__init__()
        print('ctor')

    def start(self):
        print('start')

    @pyqtSlot()
    def close_application(self):
        print('close')
