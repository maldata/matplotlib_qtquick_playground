import random
from PyQt5.QtCore import pyqtSignal, pyqtProperty, pyqtSlot

from plotapp.controllers.base_controller import BaseController


class MainController(BaseController):
    label_changed = pyqtSignal()

    def __init__(self, app):
        super().__init__(app)

        self._label = 'whatever'

    def startup(self):
        print('Main controller startup')

    @pyqtProperty(str, notify=label_changed)
    def label(self):
        return self._label

    @pyqtSlot()
    def generate_data(self):
        data = [random.random() for i in range(10)]
        print(data)
