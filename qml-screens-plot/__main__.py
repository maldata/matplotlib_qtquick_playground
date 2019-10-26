import os
import sys

from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtWidgets import QApplication

from controllers.main import MainController
from controllers.matplot import MatplotlibController


def main():
    print('main()')
    
    qmlRegisterType(MatplotlibController, "Matplot", 1, 0, "Matplot")
    
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main_controller = MainController(app)
    context = engine.rootContext()
    context.setContextProperty("main", main_controller)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    engine.load(os.path.join(script_directory, 'qml/main.qml'))

    main_controller.start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
