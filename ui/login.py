import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit,
                             QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout,
                             QDialog, QFormLayout, QToolTip, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import pyqtSlot

from prj_utils.db_session import session as Session
from prj_utils.models import User
from ui.main import MainWindow


class LoginWindow(QWidget, QGridLayout):

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setGeometry(1200, 920, 800, 600)
        self.setWindowTitle('Логин')
        self.center()

        # Создаём кнопку логин
        login_btn = QPushButton('Логин', self)
        login_btn.setToolTip('Введите имя пользвателя и пароль и нажмите кнопку')
        login_btn.move(450, 450)
        login_btn.clicked.connect(self.login_btn_method)

        # Создаём кнопку выход
        exit_btn = QPushButton('Выйти', self)
        exit_btn.setToolTip('Выход')
        exit_btn.move(250, 450)
        exit_btn.clicked.connect(self.close)

        # Создаём текстовое поле для логина
        self.textbox_login = QLineEdit(self)
        self.textbox_login.move(250, 250)
        self.textbox_login.resize(280, 40)

        # Создаём текстовое поле для пароля
        self.textbox_password = QLineEdit(self)
        self.textbox_password.move(250, 350)
        self.textbox_password.resize(280, 40)

        # Создаём подпись для поля ввода логина
        label = QLabel('Логин', self)
        label.move(250, 230)

        # Создаём подпись для поля ввода пароля
        label2 = QLabel('Пароль', self)
        label2.move(250, 330)

        self.show()

    """def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Message', "Вы уверены, что хотите выйти?",
                                     QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
    """
    def login_btn_method(self):
        login_textbox_Value = self.textbox_login.text()
        password_textbox_Value = self.textbox_password.text()
        sess = Session()
        user = sess.query(User).filter(User.username == login_textbox_Value).count()

        if user == 0:
            QMessageBox.question(self, '!ВНИМАНИЕ!', f"Вы ввели неправильное имя пользователя или пароль")
            self.textbox_login.setText("")
            self.textbox_password.setText("")

        else:
            user = sess.query(User).filter(User.username == login_textbox_Value).first()
            is_password_right = user.password == password_textbox_Value

            if is_password_right:
                # перейти на MainWindow

                self.main_window = MainWindow()
                self.main_window.show()
                self.close()

            else:
                QMessageBox.question(self, '!ВНИМАНИЕ!', f"Вы ввели неправильное имя пользователя или пароль")
                self.textbox_login.setText("")
                self.textbox_password.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    sys.exit(app.exec_())
