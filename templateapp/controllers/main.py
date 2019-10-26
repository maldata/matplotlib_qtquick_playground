from PySide2.QtCore import QObject, Property, Signal, Slot

from .content_area1_controller import ContentArea1Controller
from .content_area2_controller import ContentArea2Controller


class MainController(QObject):
    # signals
    active_content_area_changed = Signal()

    def __init__(self, app):
        super().__init__()

        self._app = app
        self._active_content_area_controller = None

        self._content_map = {
            "SCREEN1": ContentArea1Controller('./main_content_areas/content_area1.qml'),
            "SCREEN2": ContentArea2Controller('./main_content_areas/content_area2.qml')
        }

    @Property(QObject, notify=active_content_area_changed)
    def active_content_area_controller(self):
        return self._active_content_area_controller

    @active_content_area_controller.setter
    def set_active_content_area_controller(self, value):
        if self._active_content_area_controller != value:
            self._active_content_area_controller = value
            self.active_content_area_changed.emit()
    
    @Slot()
    def close_application(self):
        self.shutdown()
        
    def start(self):
        print("start()")
        self.set_active_content_area_controller(self._content_map["SCREEN1"])
        
    def shutdown(self):
        print("shutdown()")
        self.active_content_area_controller.deinitialize()
        self._app.quit()
        
    @Slot(str)
    def change_content(self, screen_key):
        try:
            new_controller = self._content_map[screen_key]
        except KeyError as ex:
            print('Failed to change to controller {0} (key not found)'.format(screen_key))
            return

        if new_controller == self.active_content_area_controller:
            return

        print("Changing to {0}".format(screen_key))

        if self.active_content_area_controller is not None:
            self.active_content_area_controller.deinitialize()

        self.set_active_content_area_controller(new_controller)
        self.active_content_area_controller.initialize()
