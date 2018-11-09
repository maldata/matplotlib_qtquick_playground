import sys
import os.path

from PyQt5.QtCore import QTimer
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication

from controllers.main_controller import MainController


def main():
    app = QGuiApplication(sys.argv)
    qml_engine = QQmlApplicationEngine()

    main_controller = MainController(app)
    context = qml_engine.rootContext()
    context.setContextProperty("main", main_controller)

    this_directory = os.path.dirname(os.path.abspath(__file__))
    qml_path = os.path.join(this_directory, 'qml/main.qml')
    qml_engine.load(qml_path)

    main_window = qml_engine.rootObjects()[0]
    main_window.show()

    QTimer.singleShot(0, main_controller.startup)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
