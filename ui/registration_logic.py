from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from ui.registration import Ui_MainWindow
from ui.login import LoginWindow
import sys
import user


class RegistrationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.warning_lable.hide()
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.ok_btn_method)
        self.show()

    def ok_btn_method(self):
        password1 = self.ui.lineEdit_2.text()
        password2 = self.ui.lineEdit_3.text()
        if password1 != password2:
            self.ui.warning_lable.show()
        else:
            user.add_user(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_1.text())
            self.login_window = LoginWindow()
            self.login_window.show()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration_window = RegistrationWindow()
    sys.exit(app.exec())
