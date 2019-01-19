import sys
from PyQt5.QtWidgets import QApplication
from ui.login import LoginWindow
from ui.main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    main_window = MainWindow()
   # main_window.show()

    sys.exit(app.exec_())
