from PySide2.QtCore import Property, Signal, QTimer

from random import random

from .base_content_area_controller import BaseContentAreaController


class ContentArea2Controller(BaseContentAreaController):
    # signals
    plotDataChanged = Signal()

    def __init__(self, qml_file):
        super().__init__(qml_file)

        self._plot_data = []
        QTimer.singleShot(500, self.new_thing)

    def initialize(self):
        print('Initializing screen 2 controller')

    def deinitialize(self):
        print('Deinitializing screen 2 controller')

    @Property(list, notify=plotDataChanged)
    def plot_data(self):
        return self._plot_data

    @plot_data.setter
    def set_plot_data(self, value):
        if self._plot_data != value:
            self._plot_data = value
            self.plotDataChanged.emit()

    def new_thing(self):
        self.set_plot_data(self.plot_data + [random()])
        QTimer.singleShot(500, self.new_thing)
