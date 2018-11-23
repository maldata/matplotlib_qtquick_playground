from .base_content_area_controller import BaseContentAreaController


class ContentArea1Controller(BaseContentAreaController):
    # signals

    def __init__(self, qml_file):
        super().__init__(qml_file)

    def initialize(self):
        print('Initializing screen 1 controller')

    def deinitialize(self):
        print('Deinitializing screen 1 controller')
