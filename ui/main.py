from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from main_window import Ui_MainWindow
import sys
from prj_utils.processes import Process


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.process = Process()
        process = self.process.get_procs()
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(len(process))

        # Headers for Columns
        self.ui.tableWidget.setHorizontalHeaderLabels(process[0].keys())

        row = 0
        for proc in process:
            col = 0

            for item in proc.values():
                print(item)

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
