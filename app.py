import sys
from PyQt5.QtWidgets import QApplication
from ui.login import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()

    sys.exit(app.exec_())
