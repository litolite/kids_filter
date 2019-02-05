from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMessageBox, QCheckBox
from main_window import Ui_MainWindow
import sys
from db_session import session as Session
from models import Process, User


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        sess = Session()
        user = sess.query(User).filter(User.is_admin == True).first()
        self.processes = [u._asdict() for u in sess.query(Process.username, Process.name, Process.is_allowed).all()]

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(self.processes))
        self.ui.label_3.setText(str(user))

        # Headers for Columns
        if not self.processes:
            pass
        else:
            self.ui.tableWidget.setHorizontalHeaderLabels(self.processes[0].keys())

        row = 0
        for proc in self.processes:
            col = 0

            for item in proc.values():
                if item == None:
                    item = 'Не определен'
                if item is True or False: #TODO сделать конвертацию в чекбоксы поля is_allowed
                    item = QtWidgets.QCheckBox(self).toggle()



                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы уверены, что хотите выйти?",
                                     QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def show_procs(self):
        pass


if __name__ == '__main__':
    # app = QtWidgets.QApplication([])
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
