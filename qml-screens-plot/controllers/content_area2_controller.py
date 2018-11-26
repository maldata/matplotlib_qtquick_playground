from .base_content_area_controller import BaseContentAreaController


class ContentArea2Controller(BaseContentAreaController):
    # signals

    def __init__(self, qml_file):
        super().__init__(qml_file)

    def initialize(self):
        print('Initializing screen 2 controller')

    def deinitialize(self):
        print('Deinitializing screen 2 controller')
