from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from main_window import Ui_MainWindow
import sys
from db_session import session as Session
from models import Process


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        sess = Session()
        self.processes = [u._asdict() for u in sess.query(Process.username, Process.name).all()]

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(len(self.processes))

        # Headers for Columns
        self.ui.tableWidget.setHorizontalHeaderLabels(self.processes[0].keys())

        row = 0
        for proc in self.processes:
            col = 0

            for item in proc.values():
                if item == None:
                    item = 'Не определен'
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def show_procs(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
