import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem

import dbconnect
from UI.WindowLogin import Ui_Dialog as Ui_LoginWindow
from UI.MainWindowAdmin import Ui_MainWindow as Ui_MainWindowAdmin
from UI.MainWindowTourist import Ui_MainWindow as Ui_MainWindowTourist

def open_main_window_admin():
    global main_window_admin, ui_main_window_admin

    main_window_admin = QMainWindow()
    ui_main_window_admin = Ui_MainWindowAdmin()
    ui_main_window_admin.setupUi(main_window_admin)
    main_window_admin.show()
    window.close()

def open_main_window_tourist():
    global main_window_tourist, ui_main_window_tourist

    main_window_tourist = QMainWindow()
    ui_main_window_tourist = Ui_MainWindowTourist()
    ui_main_window_tourist.setupUi(main_window_tourist)
    main_window_tourist.show()
    window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(window)

    ui.pushButton_Login.clicked.connect(open_main_window_admin)

    window.show()
    sys.exit(app.exec())
