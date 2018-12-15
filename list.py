import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)
 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(400, 300)
#     w.move(500, 300)
#     w.setWindowTitle('Input1')
#     w.show()
    
 
class Example(QWidget):
    
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
        
        self.setGeometry(300, 300, 350, 300)
           
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())