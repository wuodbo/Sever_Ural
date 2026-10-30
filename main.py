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
from UI.ProfileTouristList import Ui_Dialog as ProfileTouristList
from UI.Filters import Ui_Dialog as Filters
from UI.ProfileGuideAdmin import Ui_Dialog as ProfileGuide_admin
from UI.ProfileTouristAdmin import Ui_Dialog as ProfileTourist_admin
from UI.Tour import Ui_Dialog as Tour
from UI.TourEdit import Ui_Dialog as TourEdit
from UI.ReviewView import Ui_Dialog as ReviewView
from UI.WindowRegistration import Ui_Dialog as RegistrationWindow
from UI.TouristListTour import Ui_Dialog as TouristListTour
from UI.Booking import Ui_Dialog as Booking
from UI.ListGuide import Ui_Dialog as ListGuide
from UI.Notifications import Ui_Dialog as Notifications
from UI.ControlBooking import Ui_Dialog as ControlBooking
from UI.BookingView import Ui_Dialog as BookingView
from UI.ListReviews import Ui_Dialog as ListReviews
from UI.ProfileGuide import Ui_Dialog as ProfileGuide
from UI.ProfileTouristEdit import Ui_Dialog as ProfileTourist
from UI.AddTour import Ui_Dialog as AddTour
from UI.ListTour import Ui_Dialog as ListTour
from UI.ForgotPass import Ui_Dialog as ForgotPass
from UI.ChangePass import Ui_Dialog as ChangePass

current_main_window = None

def safe_close(window):
    if window is None:
        return
    try:
        window.close()
    except RuntimeError:
        pass

def open_dialog(ui_class, parent=None, close_parent=True):
    win = QDialog()
    ui = ui_class()
    ui.setupUi(win)
    win.show()
    if close_parent and parent is not None:
        safe_close(parent)
    return win, ui

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
    global current_main_window

    safe_close(current_main_window)
    current_main_window = None

    window.show()
    ui.lineEdit_Login.clear()
    ui.lineEdit_Password.clear()

def return_to_main(current_window, main_window):
    safe_close(current_window)
    if main_window is not None:
        main_window.show()

def return_to_login(current_window):
    global window, ui

    safe_close(current_window)

    if ui:
        ui.lineEdit_Login.clear()
        ui.lineEdit_Password.clear()

    if window:
        window.show()

def control_user(parent=None):
    global user_control_window, user_control_ui
    user_control_window, user_control_ui = open_dialog(ControlTourist_admin, parent)

    user_control_ui.pushButton_Profile_11.clicked.connect(profile_guide_admin)
    user_control_ui.pushButton_Profile_12.clicked.connect(profile_guide_admin)
    user_control_ui.pushButton_Profile_9.clicked.connect(profile_tourist_admin)
    user_control_ui.pushButton_Profile_10.clicked.connect(profile_tourist_admin)
    user_control_ui.pushButton_OnBooking.clicked.connect(profile_tourist_list)
    user_control_ui.pushButton_OnBooking_2.clicked.connect(profile_tourist_list)
    user_control_ui.pushButton_OnBooking_3.clicked.connect(profile_guide_list)
    user_control_ui.pushButton_OnBooking_4.clicked.connect(profile_guide_list)

    user_control_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(user_control_window, current_main_window)
    )

def profile_guide_admin():
    global profile_guide_window, profile_guide_ui
    profile_guide_window, profile_guide_ui = open_dialog(ProfileGuide_admin, close_parent=False)

def profile_tourist_list():
    global profile_tourist_window, profile_tourist_ui
    profile_tourist_window, profile_tourist_ui = open_dialog(ProfileTouristList, close_parent=False)

def profile_tourist_admin():
    global profile_tourist_window, profile_tourist_ui
    profile_tourist_window, profile_tourist_ui = open_dialog(ProfileTourist_admin, close_parent=False)

def control_tour(parent=None):
    global tour_control_window, tour_control_ui
    tour_control_window, tour_control_ui = open_dialog(ControlTour_admin, parent)

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

    tour_control_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(tour_control_window, current_main_window)
    )

def tour_edit():
    global tour_edit_window, tour_edit_ui
    tour_edit_window, tour_edit_ui = open_dialog(TourEdit, close_parent=False)

def tour_view():
    global tour_window, tour_ui
    tour_window, tour_ui = open_dialog(Tour, close_parent=False)

def control_reviews(parent=None):
    global reviews_control_window, reviews_control_ui
    reviews_control_window, reviews_control_ui = open_dialog(ControlReviews_admin, parent)

    reviews_control_ui.pushButton_Profile_13.clicked.connect(review_view)
    reviews_control_ui.pushButton_Profile_19.clicked.connect(review_view)
    reviews_control_ui.pushButton_Profile_20.clicked.connect(review_view)
    reviews_control_ui.pushButton_Profile_21.clicked.connect(review_view)

    reviews_control_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(reviews_control_window, current_main_window)
    )

def review_view():
    global reviews_view_window, reviews_view_window_ui
    reviews_view_window, reviews_view_window_ui = open_dialog(ReviewView, close_parent=False)

def add_route():
    global add_route_window, add_route_ui
    add_route_window, add_route_ui = open_dialog(AddRoute_admin, close_parent=False)

def add_equipment():
    global add_equipment_window, add_equipment_ui
    add_equipment_window, add_equipment_ui = open_dialog(AddEquipment_admin, close_parent=False)

def profile_guide_list():
    global profile_guide_window, profile_guide_ui
    profile_guide_window, profile_guide_ui = open_dialog(ProfileGuideList, close_parent=False)

def filters():
    global filters_window, filters_ui
    filters_window, filters_ui = open_dialog(Filters, close_parent=False)

def registration():
    global registration_window, registration_ui
    registration_window, registration_ui = open_dialog(RegistrationWindow, parent=window)

    registration_ui.pushButton_BackOnLogin.clicked.connect(
        lambda: return_to_login(registration_window)
    )

def booking():
    global booking_window, booking_window_ui
    booking_window, booking_window_ui = open_dialog(Booking, close_parent=False)

def tourist_list_tour(parent=None):
    global tourist_list_window, tourist_list_window_ui
    tourist_list_window, tourist_list_window_ui = open_dialog(TouristListTour, parent)

    tourist_list_window_ui.pushButton_OnBooking.clicked.connect(tour_view)
    tourist_list_window_ui.pushButton_OnBooking_2.clicked.connect(tour_view)
    tourist_list_window_ui.pushButton_OnBooking_3.clicked.connect(tour_view)
    tourist_list_window_ui.pushButton_OnBooking_13.clicked.connect(tour_view)
    tourist_list_window_ui.pushButton_OnBooking_24.clicked.connect(tour_view)
    tourist_list_window_ui.pushButton_OnBooking_6.clicked.connect(booking)
    tourist_list_window_ui.pushButton_OnBooking_7.clicked.connect(booking)
    tourist_list_window_ui.pushButton_OnBooking_8.clicked.connect(booking)
    tourist_list_window_ui.pushButton_OnBooking_14.clicked.connect(booking)
    tourist_list_window_ui.pushButton_OnBooking_23.clicked.connect(booking)

    tourist_list_window_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(tourist_list_window, current_main_window)
    )

def guide_list(parent=None):
    global guide_list_window, guide_list_window_ui
    guide_list_window, guide_list_window_ui = open_dialog(ListGuide, parent)

    guide_list_window_ui.pushButton_Profile_4.clicked.connect(profile_guide_list)
    guide_list_window_ui.pushButton_Profile_5.clicked.connect(profile_guide_list)
    guide_list_window_ui.pushButton_Profile_6.clicked.connect(profile_guide_list)
    guide_list_window_ui.pushButton_Profile_7.clicked.connect(profile_guide_list)

    guide_list_window_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(guide_list_window, current_main_window)
    )

def notifications_window(parent=None):
    global notifications_window_view, notifications_window_ui
    notifications_window_view, notifications_window_ui = open_dialog(Notifications, parent)

    notifications_window_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(notifications_window_view, current_main_window)
    )

def control_booking(parent=None):
    global control_booking_window, control_booking_window_ui
    control_booking_window, control_booking_window_ui = open_dialog(ControlBooking, parent)

    control_booking_window_ui.pushButton_Profile_9.clicked.connect(booking_view)
    control_booking_window_ui.pushButton_Profile_10.clicked.connect(booking_view)
    control_booking_window_ui.pushButton_Profile_12.clicked.connect(booking)
    control_booking_window_ui.pushButton_Profile_14.clicked.connect(booking)

    control_booking_window_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(control_booking_window, current_main_window)
    )

def booking_view():
    global view_booking_window, view_booking_window_ui
    view_booking_window, view_booking_window_ui = open_dialog(BookingView, close_parent=False)

def list_reviews(parent=None):
    global list_reviews_window, list_reviews_window_ui
    list_reviews_window, list_reviews_window_ui = open_dialog(ListReviews, parent)

    list_reviews_window_ui.pushButton_Profile_9.clicked.connect(review_view)
    list_reviews_window_ui.pushButton_Profile_10.clicked.connect(review_view)
    list_reviews_window_ui.pushButton_Profile_11.clicked.connect(review_view)
    list_reviews_window_ui.pushButton_Profile_12.clicked.connect(review_view)

    list_reviews_window_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(list_reviews_window, current_main_window)
    )

def profile_tourist_edit():
    global profile_tourist_edit_window, profile_tourist_edit_window_ui
    profile_tourist_edit_window, profile_tourist_edit_window_ui = open_dialog(ProfileTourist, close_parent=False)

    profile_tourist_edit_window_ui.pushButton_Login_3.clicked.connect(change_pass)

def profile_guide_edit():
    global profile_guide_edit_window, profile_guide_edit_window_ui
    profile_guide_edit_window, profile_guide_edit_window_ui = open_dialog(ProfileGuide, close_parent=False)

    profile_guide_edit_window_ui.pushButton_Login_3.clicked.connect(change_pass)


def change_pass():
    global change_pass_window, change_pass_window_ui
    change_pass_window, change_pass_window_ui = open_dialog(ChangePass, close_parent=False)

def add_tour():
    global add_tour_window, add_tour_window_ui
    add_tour_window, add_tour_window_ui = open_dialog(AddTour, close_parent=False)

def list_tour(parent=None):
    global list_tour_window, list_tour_window_ui
    list_tour_window, list_tour_window_ui = open_dialog(ListTour, parent)

    list_tour_window_ui.pushButton_OnBooking.clicked.connect(tour_view)
    list_tour_window_ui.pushButton_OnBooking_2.clicked.connect(tour_view)
    list_tour_window_ui.pushButton_OnBooking_3.clicked.connect(tour_view)
    list_tour_window_ui.pushButton_OnBooking_4.clicked.connect(tour_view)
    list_tour_window_ui.pushButton_OnBooking_5.clicked.connect(tour_view)

    list_tour_window_ui.pushButton_Logout.clicked.connect(
        lambda: return_to_main(list_tour_window, current_main_window)
    )

def forget_pass():
    global forget_pass_window, forget_pass_window_ui
    forget_pass_window, forget_pass_window_ui = open_dialog(ForgotPass, close_parent=False)


def login():
    global admin_window, admin_ui, user_window, user_ui, guide_window, guide_ui
    global window, ui, current_main_window

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
        current_main_window = admin_window
        admin_window.show()

        admin_ui.pushButton_ControlTourist.clicked.connect(
            lambda: control_user(admin_window)
        )
        admin_ui.pushButton_ControlTour.clicked.connect(
            lambda: control_tour(admin_window)
        )
        admin_ui.pushButton_ControlReview.clicked.connect(
            lambda: control_reviews(admin_window)
        )
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
        current_main_window = user_window
        user_window.show()

        user_ui.pushButton_Profile_9.clicked.connect(profile_guide_list)
        user_ui.pushButton_Profile_10.clicked.connect(profile_guide_list)
        user_ui.pushButton_Profile_11.clicked.connect(profile_guide_list)
        user_ui.pushButton_Profile_12.clicked.connect(profile_guide_list)
        user_ui.pushButton_Search_2.clicked.connect(filters)

        user_ui.pushButton_Tour.clicked.connect(
            lambda: tourist_list_tour(user_window)
        )
        user_ui.pushButton_Guide.clicked.connect(
            lambda: guide_list(user_window)
        )
        user_ui.pushButton_Booking_2.clicked.connect(
            lambda: notifications_window(user_window)
        )
        user_ui.pushButton_Booking.clicked.connect(
            lambda: control_booking(user_window)
        )
        user_ui.pushButton_Review.clicked.connect(
            lambda: list_reviews(user_window)
        )
        user_ui.pushButton_ControlTour_4.clicked.connect(profile_tourist_edit)

        user_ui.pushButton_Logout.clicked.connect(window_close)

    elif role == 'guide':
        print("Авторизация успешна (Гид)")
        window.hide()

        guide_window = QMainWindow()
        guide_ui = Mainwindow_guide()
        guide_ui.setupUi(guide_window)
        current_main_window = guide_window
        guide_window.show()

        guide_ui.pushButton_Profile_5.clicked.connect(profile_guide_list)
        guide_ui.pushButton_Profile_6.clicked.connect(profile_guide_list)
        guide_ui.pushButton_Profile_7.clicked.connect(profile_guide_list)
        guide_ui.pushButton_Profile_8.clicked.connect(profile_guide_list)
        guide_ui.pushButton_Search_2.clicked.connect(filters)
        guide_ui.pushButton_ControlTour_4.clicked.connect(profile_guide_edit)
        guide_ui.pushButton_ControlTour_3.clicked.connect(add_tour)

        guide_ui.pushButton_ControlTour_2.clicked.connect(
            lambda: control_tour(guide_window)
        )
        guide_ui.pushButton_ControlTour.clicked.connect(
            lambda: notifications_window(guide_window)
        )
        guide_ui.pushButton_Booking.clicked.connect(
            lambda: control_booking(guide_window)
        )
        guide_ui.pushButton_Review.clicked.connect(
            lambda: control_reviews(guide_window)
        )
        guide_ui.pushButton_Guide.clicked.connect(
            lambda: guide_list(guide_window)
        )
        guide_ui.pushButton_Tour.clicked.connect(
            lambda: list_tour(guide_window)
        )

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
    ui.pushButton_Register.clicked.connect(registration)
    ui.pushButton_ForgetPass.clicked.connect(forget_pass)
    ui.lineEdit_Password.returnPressed.connect(login)

    window.show()
    sys.exit(app.exec())