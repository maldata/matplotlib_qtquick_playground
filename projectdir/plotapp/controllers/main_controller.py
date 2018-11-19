from controllers.base_controller import BaseController


class MainController(BaseController):
    def __init__(self, app):
        super().__init__(app)

    def startup(self):
        print('main startup')

