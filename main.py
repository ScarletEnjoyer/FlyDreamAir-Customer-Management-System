import sys

from PyQt5.QtWidgets import QApplication
from storage.userStorage import init_user_storage
from ui.mainWindow import MainWindow

if __name__ == '__main__':
    init_user_storage()

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
