import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit

import dbconnect

from UI.WindowLogin import Ui_Dialog as Ui_LoginWindow
from UI.MainWindowAdmin import Ui_MainWindow as Mainwindow_admin
from UI.MainWindowTourist import Ui_MainWindow as Mainwindow_user
from UI.MainWindowGuide import Ui_MainWindow as Mainwindow_guide

def check_login(loginValue, passwordValue):
    try:
        conn = dbconnect.get_db_connection()
        
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM administrator WHERE login = %s AND password = %s",
                (loginValue, passwordValue)
            )
            if cursor.fetchone():
                return 'admin'

            cursor.execute(
                "SELECT id FROM tourist WHERE login = %s AND password = %s",
                (loginValue, passwordValue)
            )
            if cursor.fetchone():
                return 'tourist'
                
            cursor.execute(
                "SELECT id FROM guide WHERE login = %s AND password = %s",
                (loginValue, passwordValue)
            )
            if cursor.fetchone():
                return 'guide'

            return None
            
    except Exception as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

def window_close():
    global win, admin_window, user_window, guide_window, window, ui
    
    if win == 'admin' and admin_window:
        admin_window.close()
    elif win == 'user' and user_window:
        user_window.close()
    elif win == 'guide' and guide_window:
        guide_window.close()
    
    window.show()
    ui.lineEdit_Login.clear()
    ui.lineEdit_Password.clear()


def login():
    global win, admin_window, admin_ui, user_window, user_ui, guide_window, guide_ui, window, ui
    
    loginValue = ui.lineEdit_Login.text().strip()
    passwordValue = ui.lineEdit_Password.text()

    print(f"Попытка входа -> Логин: {loginValue}")

    role = check_login(loginValue, passwordValue)

    if role == 'admin':
        print("Авторизация успешна (Администратор)")
        window.hide() 
        
        admin_window = QMainWindow()
        admin_ui = Mainwindow_admin()
        admin_ui.setupUi(admin_window)

        win = 'admin'

        admin_window.show()

    elif role == 'tourist':
        print("Авторизация успешна (Турист)")
        window.hide() 

        user_window = QMainWindow()
        user_ui = Mainwindow_user()
        user_ui.setupUi(user_window)

        win = 'user'

        user_window.show()
        
    elif role == 'guide':
        print("Авторизация успешна (Гид)")
        window.hide() 

        guide_window = QMainWindow()
        guide_ui = Mainwindow_guide()
        guide_ui.setupUi(guide_window)

        win = 'guide'

        guide_window.show()
        
    else:
        print("Неверный логин или пароль")

if __name__ == "__main__":
    global window, ui
    
    app = QApplication(sys.argv)

    window = QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(window)

    ui.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

    ui.pushButton_Login.clicked.connect(login)
    
    ui.lineEdit_Password.returnPressed.connect(login)

    window.show()
    sys.exit(app.exec())