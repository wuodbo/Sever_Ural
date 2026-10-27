import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit

import dbconnect

from UI.WindowLogin import Ui_Dialog as Ui_LoginWindow
from UI.MainWindowAdmin import Ui_MainWindow as Mainwindow_admin
from UI.MainWindowTourist import Ui_MainWindow as Mainwindow_user
from UI.MainWindowGuide import Ui_MainWindow as Mainwindow_guide
from UI.ControlTourist import Ui_Dialog as ControlTourist_admin
from UI.ControlTour import Ui_Dialog as ControlTour_admin
from UI.ControlReviews import Ui_Dialog as ControlReviews_admin
from UI.AddRoute import Ui_Dialog as AddRoute_admin
from UI.AddEquipment import Ui_Dialog as AddEquipment_admin
from UI.ProfileGuideList import Ui_Dialog as ProfileGuideList
from UI.Filters import Ui_Dialog as Filters
from UI.ProfileGuideAdmin import Ui_Dialog as ProfileGuide_admin
from UI.ProfileTouristAdmin import Ui_Dialog as ProfileTourist_admin
from UI.Tour import Ui_Dialog as Tour
from UI.TourEdit import Ui_Dialog as TourEdit
from UI.ReviewView import Ui_Dialog as ReviewView


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

def control_user():
    global user_control_window, user_control_ui

    user_control_window = QDialog()
    user_control_ui = ControlTourist_admin()
    user_control_ui.setupUi(user_control_window)
    user_control_window.show()
    admin_window.close()

    user_control_ui.pushButton_Profile_11.clicked.connect(profile_guide_admin)
    user_control_ui.pushButton_Profile_12.clicked.connect(profile_guide_admin)
    user_control_ui.pushButton_Profile_9.clicked.connect(profile_tourist_admin)
    user_control_ui.pushButton_Profile_10.clicked.connect(profile_tourist_admin)
    user_control_ui.pushButton_OnBooking.clicked.connect(profile_guide_list)
    user_control_ui.pushButton_OnBooking_2.clicked.connect(profile_guide_list)
    user_control_ui.pushButton_OnBooking_3.clicked.connect(profile_guide_list)
    user_control_ui.pushButton_OnBooking_4.clicked.connect(profile_guide_list)

    user_control_ui.pushButton_Logout.clicked.connect(lambda: return_to_main(user_control_window, admin_window))

def profile_guide_admin():
    global profile_guide_window, profile_guide_ui

    profile_guide_window = QDialog()
    profile_guide_ui = ProfileGuide_admin()
    profile_guide_ui.setupUi(profile_guide_window)
    profile_guide_window.show()

def profile_tourist_admin():
    global profile_tourist_window, profile_tourist_ui

    profile_tourist_window = QDialog()
    profile_tourist_ui = ProfileTourist_admin()
    profile_tourist_ui.setupUi(profile_tourist_window)
    profile_tourist_window.show()

def control_tour():
    global tour_control_window, tour_control_ui

    tour_control_window = QDialog()
    tour_control_ui = ControlTour_admin()
    tour_control_ui.setupUi(tour_control_window)
    tour_control_window.show()
    admin_window.close()

    tour_control_ui.pushButton_OnBooking.clicked.connect(tour_view)
    tour_control_ui.pushButton_OnBooking_2.clicked.connect(tour_view)
    tour_control_ui.pushButton_OnBooking_3.clicked.connect(tour_view)
    tour_control_ui.pushButton_OnBooking_4.clicked.connect(tour_view)
    tour_control_ui.pushButton_OnBooking_5.clicked.connect(tour_view)
    tour_control_ui.pushButton_OnBooking_6.clicked.connect(tour_edit)
    tour_control_ui.pushButton_OnBooking_8.clicked.connect(tour_edit)
    tour_control_ui.pushButton_OnBooking_9.clicked.connect(tour_edit)
    tour_control_ui.pushButton_OnBooking_10.clicked.connect(tour_edit)
    tour_control_ui.pushButton_OnBooking_11.clicked.connect(tour_edit)

    tour_control_ui.pushButton_Logout.clicked.connect(lambda: return_to_main(tour_control_window, admin_window))

def tour_edit():
    global tour_edit_window, tour_edit_ui

    tour_edit_window = QDialog()
    tour_edit_ui = TourEdit()
    tour_edit_ui.setupUi(tour_edit_window)
    tour_edit_window.show()

def tour_view():
    global tour_window, tour_ui

    tour_window = QDialog()
    tour_ui = Tour()
    tour_ui.setupUi(tour_window)
    tour_window.show()

def control_reviews():
    global reviews_control_window, reviews_control_ui

    reviews_control_window = QDialog()
    reviews_control_ui = ControlReviews_admin()
    reviews_control_ui.setupUi(reviews_control_window)
    reviews_control_window.show()
    admin_window.close()

    reviews_control_ui.pushButton_Profile_13.clicked.connect(review_view)
    reviews_control_ui.pushButton_Profile_19.clicked.connect(review_view)
    reviews_control_ui.pushButton_Profile_20.clicked.connect(review_view)
    reviews_control_ui.pushButton_Profile_21.clicked.connect(review_view)

    reviews_control_ui.pushButton_Logout.clicked.connect(lambda: return_to_main(reviews_control_window, admin_window))

def review_view():
    global review_view_window, review_view_ui

    review_view_window = QDialog()
    review_view_ui = ReviewView()
    review_view_ui.setupUi(review_view_window)
    review_view_window.show()

def return_to_main(current_window, main_window):
    if current_window:
        current_window.close()

    if main_window:
        main_window.show()

def add_route():
    global add_route_window, add_route_ui

    add_route_window = QDialog()
    add_route_ui = AddRoute_admin()
    add_route_ui.setupUi(add_route_window)
    add_route_window.show()

def add_equipment():
    global add_equipment_window, add_equipment_ui

    add_equipment_window = QDialog()
    add_equipment_ui = AddEquipment_admin()
    add_equipment_ui.setupUi(add_equipment_window)
    add_equipment_window.show()

def profile_guide_list():
    global profile_guide_window, profile_guide_ui

    profile_guide_window = QDialog()
    profile_guide_ui = ProfileGuideList()
    profile_guide_ui.setupUi(profile_guide_window)
    profile_guide_window.show()

def filters():
    global filters_window, filters_ui

    filters_window = QDialog()
    filters_ui = Filters()
    filters_ui.setupUi(filters_window)
    filters_window.show()

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

        admin_ui.pushButton_ControlTourist.clicked.connect(control_user)
        admin_ui.pushButton_ControlTour.clicked.connect(control_tour)
        admin_ui.pushButton_ControlReview.clicked.connect(control_reviews)
        admin_ui.pushButton_Route.clicked.connect(add_route)
        admin_ui.pushButton_Equipment.clicked.connect(add_equipment)
        admin_ui.pushButton_Profile.clicked.connect(profile_guide_list)
        admin_ui.pushButton_Profile_2.clicked.connect(profile_guide_list)
        admin_ui.pushButton_Profile_3.clicked.connect(profile_guide_list)
        admin_ui.pushButton_Profile_4.clicked.connect(profile_guide_list)
        admin_ui.pushButton_Search_2.clicked.connect(filters)

        admin_ui.pushButton_Logout.clicked.connect(window_close)

    elif role == 'tourist':
        print("Авторизация успешна (Турист)")
        window.hide() 

        user_window = QMainWindow()
        user_ui = Mainwindow_user()
        user_ui.setupUi(user_window)

        win = 'user'

        user_window.show()
        user_ui.pushButton_Logout.clicked.connect(window_close)

    elif role == 'guide':
        print("Авторизация успешна (Гид)")
        window.hide() 

        guide_window = QMainWindow()
        guide_ui = Mainwindow_guide()
        guide_ui.setupUi(guide_window)

        win = 'guide'

        guide_window.show()
        guide_ui.pushButton_Logout.clicked.connect(window_close)
        
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