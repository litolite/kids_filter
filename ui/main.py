from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMessageBox, QCheckBox
from ui.main_window import Ui_MainWindow
import sys
from prj_utils.db_session import session as Session
from prj_utils.models import Process, User


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

        for row, proc in enumerate(self.processes):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(proc.get('username')))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(proc.get('name')))
            cb = QtWidgets.QCheckBox(parent=self.ui.tableWidget)
            self.ui.tableWidget.setCellWidget(row, 2, cb)

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
