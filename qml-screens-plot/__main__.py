import os
import pathlib
import sys
import signal

from PyQt5.QtCore import QTimer
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

from controllers.main import MainController


def main():
    print('main()')

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main_controller = MainController(app)
    context = engine.rootContext()
    context.setContextProperty("main", main_controller)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    engine.load(os.path.join(script_directory, 'qml/main.qml'))

    # hook into SIGINT signal to shutdown the application when commanded
    def sig_int_handler(signal, frame):
        logger.info('SIGINT received')
        main_controller.shutdown()
    signal.signal(signal.SIGINT, sig_int_handler)

    # Python cannot handle signals while the Qt event loop is running
    # So we'll let the python interpreter run periodically so any
    # SIGINT signals can be processed
    timer = QTimer()
    timer.start(500)  # You may change this if you wish.
    timer.timeout.connect(lambda: None)

    main_controller.start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
