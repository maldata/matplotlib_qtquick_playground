import sys
import os.path

from PyQt5.QtCore import QTimer
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication

from plotapp.controllers.window_controller import WindowController
from plotapp.controllers.figure_controller import FigureCanvasQtQuickAgg


def main():
    qmlRegisterType(FigureCanvasQtQuickAgg, "QtQuickFigureCanvas", 1, 0, "FigureCanvas")

    app = QGuiApplication(sys.argv)
    qml_engine = QQmlApplicationEngine()

    main_controller = WindowController(app)
    context = qml_engine.rootContext()
    context.setContextProperty("main", main_controller)

    this_directory = os.path.dirname(os.path.abspath(__file__))
    qml_path = os.path.join(this_directory, 'qml/main_window.qml')
    qml_engine.load(qml_path)

    QTimer.singleShot(0, lambda arg=qml_engine: main_controller.startup(arg))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
