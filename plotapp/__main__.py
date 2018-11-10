import sys
import os.path

from PyQt5.QtCore import QTimer, QObject
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication

from plotapp.controllers.main_controller import MainController
from plotapp.controllers.figure_controller import FigureCanvasQTAgg


def main():
    qmlRegisterType(FigureCanvasQTAgg, "QtQuickFigureCanvas", 1, 0, "FigureCanvas")

    app = QGuiApplication(sys.argv)
    qml_engine = QQmlApplicationEngine()

    main_controller = MainController(app)
    context = qml_engine.rootContext()
    context.setContextProperty("main", main_controller)

    this_directory = os.path.dirname(os.path.abspath(__file__))
    qml_path = os.path.join(this_directory, 'qml/main_window.qml')
    qml_engine.load(qml_path)

    QTimer.singleShot(0, lambda arg=qml_engine: main_controller.startup(arg))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
