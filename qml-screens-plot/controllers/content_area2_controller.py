from PyQt5.QtCore import pyqtProperty, pyqtSignal, QTimer

from random import random

from .base_content_area_controller import BaseContentAreaController


class ContentArea2Controller(BaseContentAreaController):
    # signals
    sampleFloatChanged = pyqtSignal()

    def __init__(self, qml_file):
        super().__init__(qml_file)

        self._sample_float = random()
        QTimer.singleShot(5000, self.new_thing)

    def initialize(self):
        print('Initializing screen 2 controller')

    def deinitialize(self):
        print('Deinitializing screen 2 controller')

    @pyqtProperty(float, notify=sampleFloatChanged)
    def sample_float(self):
        return self._sample_float

    @sample_float.setter
    def sample_float(self, value):
        if self._sample_float != value:
            self._sample_float = value
            self.sampleFloatChanged.emit()

    def new_thing(self):
        self.sample_float = random()
        QTimer.singleShot(5000, self.new_thing)
