import os
import sys

from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtWidgets import QApplication

from main_controller import MainController
from custom_painted_item import CustomPaintedItem


def main():
    print('main()')

    qmlRegisterType(CustomPaintedItem, "CustomPaintedItem", 1, 0, "CustomPaintedItem")

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main_controller = MainController()
    context = engine.rootContext()
    context.setContextProperty("main", main_controller)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    engine.load(os.path.join(script_directory, 'main.qml'))

    main_controller.start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
