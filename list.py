import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QDialog)
class Example(QWidget, QGridLayout):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        title = QLabel('Login')
        author = QLabel('Password')
        
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)


        self.setLayout(grid)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)

        self.login = QLineEdit()
        self.login.setPlaceholderText('Введите логин...')

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Введите пароль...')

        layout = QFormLayout()
        layout.addRow('Login:', self.login)
        layout.addRow('Password:', self.password)

        self.setLayout(layout)

         

        
        self.setGeometry(750, 300, 350, 300)
        self.setWindowTitle('Авторизация')   
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


#сlass LoginWindow(QDialog):
   # def __init__(self):
        #super().__init__()

        #self.login = QLineEdit()
        #self.login.setPlaceholderText('Введите логин...')

        #self.password = QLineEdit()
        #self.password.setEchoMode(QLineEdit.Password)
        #self.password.setPlaceholderText('Введите пароль...')

        #layout = QFormLayout()
        #layout.addRow('Login:', self.login)
        #layout.addRow('Password:', self.password)

        #self.setLayout(layout)
        
         
        
        