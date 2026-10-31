import sys
import os

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

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

current_main_window = None

def open_tour_view(tour_id):
    global tour_window, tour_ui

    data = dbconnect.get_tour_by_id(tour_id)
    if not data:
        print(f"Тур с id={tour_id} не найден")
        return

    t_id, name, status, seats, start_d, end_d = data

    tour_window, tour_ui = open_dialog(Tour, close_parent=False)

    tour_ui.label_2.setText(name)
    tour_ui.label_3.setText(status)
    tour_ui.label_4.setText(str(seats))
    tour_ui.label_5.setText(start_d.strftime("%d.%m.%Y"))
    tour_ui.label_6.setText(end_d.strftime("%d.%m.%Y"))

def open_review_view(review_id):
    global review_view_window, review_view_ui

    data = dbconnect.get_review_by_id(review_id)
    if not data:
        print(f"Отзыв с id={review_id} не найден")
        return

    r_id, rating, comment, review_date, tourist_name, tour_name, guide_name = data

    review_view_window, review_view_ui = open_dialog(ReviewView, close_parent=False)

    review_view_ui.label_2.setText(tour_name)
    review_view_ui.label_3.setText(comment)
    review_view_ui.label_3.setWordWrap(True)
    review_view_ui.label_3.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    review_view_ui.label_4.setText(f"{rating} / 5")


def _open_review_from_button(btn):
    review_id = btn.property("review_id")
    if review_id is None:
        return
    open_review_view(review_id)


def fill_review_slots(ui, reviews):
    cards = [
        {
            "tour":   ui.label_TouristName_5,
            "author": ui.label_ActiveBookings_5,
            "btn":    ui.pushButton_Profile_9,
        },
        {
            "tour":   ui.label_TouristName_6,
            "author": ui.label_ActiveBookings_6,
            "btn":    ui.pushButton_Profile_10,
        },
        {
            "tour":   ui.label_TouristName_7,
            "author": ui.label_ActiveBookings_7,
            "btn":    ui.pushButton_Profile_11,
        },
        {
            "tour":   ui.label_TouristName_8,
            "author": ui.label_ActiveBookings_8,
            "btn":    ui.pushButton_Profile_12,
        },
    ]

    for i, card in enumerate(cards):
        if i < len(reviews):
            r_id, rating, comment, review_date, tourist_name, tour_name, guide_name = reviews[i]

            card["tour"].setText(f'Отзыв на тур "{tour_name}"')
            card["author"].setText(f"Турист: {tourist_name}")
            card["btn"].setVisible(True)
            card["btn"].setEnabled(True)
            card["btn"].setProperty("review_id", r_id)

            try:
                card["btn"].clicked.disconnect()
            except RuntimeError:
                pass
            card["btn"].clicked.connect(
                lambda checked=False, b=card["btn"]: _open_review_from_button(b)
            )
        else:
            card["tour"].setText("")
            card["author"].setText("")
            card["btn"].setVisible(False)
            card["btn"].setEnabled(False)
            card["btn"].setProperty("review_id", None)


def fill_guide_cards_on_main(ui, guides):
    cards = [
        {
            "name":  ui.label_TouristName_3,
            "spec":  ui.label_Specialization_7,
            "tours": ui.label_ActiveBookings_3,
            "role":  ui.label_Role_5,
            "btn":   ui.pushButton_Profile_5,
        },
        {
            "name":  ui.label_GuideName_6,
            "spec":  ui.label_Specialization_5,
            "tours": ui.label_ActiveTours_3,
            "role":  ui.label_Role_7,
            "btn":   ui.pushButton_Profile_7,
        },
        {
            "name":  ui.label_GuideName_7,
            "spec":  ui.label_Specialization_6,
            "tours": ui.label_ActiveTours_4,
            "role":  ui.label_Role_8,
            "btn":   ui.pushButton_Profile_8,
        },
        {
            "name":  ui.label_TouristName_4,
            "spec":  ui.label_Specialization_8,
            "tours": ui.label_ActiveBookings_4,
            "role":  ui.label_Role_6,
            "btn":   ui.pushButton_Profile_6,
        },
    ]

    for i, card in enumerate(cards):
        if i < len(guides):
            g_id, full_name, qual, active_tours = guides[i]

            card["name"].setText(full_name)
            card["role"].setText("Роль: гид")
            card["tours"].setText(f"Активных туров: {active_tours}")
            card["spec"].setText(f"Специализация: {qual}")
            card["btn"].setVisible(True)
            card["btn"].setEnabled(True)
            card["btn"].setProperty("guide_id", g_id)

            try:
                card["btn"].clicked.disconnect()
            except RuntimeError:
                pass
            card["btn"].clicked.connect(
                lambda checked=False, b=card["btn"]: _open_profile_from_button(b)
            )
        else:
            card["name"].setText("")
            card["role"].setText("")
            card["tours"].setText("")
            card["spec"].setText("")
            card["btn"].setVisible(False)
            card["btn"].setEnabled(False)
            card["btn"].setProperty("guide_id", None)


def open_guide_profile(guide_id):
    global guide_profile_window, guide_profile_ui

    data = dbconnect.get_guide_profile(guide_id)
    if not data:
        print(f"Гид с id={guide_id} не найден")
        return

    first, last, phone, email, login, qual, rating, status = data

    guide_profile_window, guide_profile_ui = open_dialog(
        ProfileGuideList, close_parent=False
    )

    guide_profile_ui.label_2.setText(first)
    guide_profile_ui.label_3.setText(last)
    guide_profile_ui.label_4.setText(phone)
    guide_profile_ui.label_5.setText(email)
    guide_profile_ui.label_6.setText(login)
    guide_profile_ui.label_7.setText(f"{float(rating):.2f}")
    guide_profile_ui.label_8.setText(status)

    idx = guide_profile_ui.comboBox.findText(qual)
    if idx >= 0:
        guide_profile_ui.comboBox.setCurrentIndex(idx)
    else:
        guide_profile_ui.comboBox.addItem(qual)
        guide_profile_ui.comboBox.setCurrentIndex(guide_profile_ui.comboBox.count() - 1)


def _open_profile_from_button(btn):
    guide_id = btn.property("guide_id")
    if guide_id is None:
        return
    open_guide_profile(guide_id)


def fill_guide_slots(ui, guides):
    cards = [
        {"name": ui.label_GuideName_5, "role": ui.label_Role_4,
         "tours": ui.label_ActiveTours_2, "spec": ui.label_Specialization_2,
         "btn": ui.pushButton_Profile_4},
        {"name": ui.label_GuideName_6, "role": ui.label_Role_5,
         "tours": ui.label_ActiveTours_3, "spec": ui.label_Specialization_3,
         "btn": ui.pushButton_Profile_5},
        {"name": ui.label_GuideName_7, "role": ui.label_Role_6,
         "tours": ui.label_ActiveTours_4, "spec": ui.label_Specialization_4,
         "btn": ui.pushButton_Profile_6},
        {"name": ui.label_GuideName_8, "role": ui.label_Role_7,
         "tours": ui.label_ActiveTours_5, "spec": ui.label_Specialization_5,
         "btn": ui.pushButton_Profile_7},
    ]

    for i, card in enumerate(cards):
        if i < len(guides):
            g_id, full_name, qual, active_tours = guides[i]

            card["name"].setText(full_name)
            card["role"].setText("Роль: гид")
            card["tours"].setText(f"Активных туров: {active_tours}")
            card["spec"].setText(f"Специализация: {qual}")
            card["btn"].setVisible(True)
            card["btn"].setEnabled(True)
            card["btn"].setProperty("guide_id", g_id)
        else:
            card["name"].setText("")
            card["role"].setText("")
            card["tours"].setText("")
            card["spec"].setText("")
            card["btn"].setVisible(False)
            card["btn"].setEnabled(False)
            card["btn"].setProperty("guide_id", None)


def fill_tour_slots(ui, tours):
    suffixes = ["", "_2", "_3", "_4", "_5"]
    name_labels  = [getattr(ui, f"label_TourName{s}")    for s in suffixes]
    guide_labels = [getattr(ui, f"label_GuideName{s}")   for s in suffixes]
    image_labels = [getattr(ui, f"label_ImageTour{s}")   for s in suffixes]
    booking_btns = [getattr(ui, f"pushButton_OnBooking{s}") for s in suffixes]

    for i in range(len(suffixes)):
        if i < len(tours):
            t_id, name, guide_name = tours[i]
            name_labels[i].setText(name)
            guide_labels[i].setText(f"Гид: {guide_name}")
            booking_btns[i].setVisible(True)
            booking_btns[i].setEnabled(True)
            image_labels[i].setText("")
        else:
            name_labels[i].setText("")
            guide_labels[i].setText("")
            image_labels[i].setText("")
            booking_btns[i].setVisible(False)
            booking_btns[i].setEnabled(False)


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

    guides = dbconnect.get_active_guides(limit=4)
    fill_guide_slots(guide_list_window_ui, guides)

    for btn_name in ("pushButton_Profile_4", "pushButton_Profile_5",
                     "pushButton_Profile_6", "pushButton_Profile_7"):
        btn = getattr(guide_list_window_ui, btn_name)
        btn.clicked.connect(lambda checked=False, b=btn: _open_profile_from_button(b))

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

    reviews = dbconnect.get_reviews(limit=4)
    fill_review_slots(list_reviews_window_ui, reviews)

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

    tours = dbconnect.get_active_tours(limit=5)
    fill_tour_slots(list_tour_window_ui, tours)

    suffixes = ["", "_2", "_3", "_4", "_5"]
    for i, s in enumerate(suffixes):
        btn = getattr(list_tour_window_ui, f"pushButton_OnBooking{s}")
        if i < len(tours):
            tour_id = tours[i][0]
            try:
                btn.clicked.disconnect()
            except RuntimeError:
                pass
            btn.clicked.connect(
                lambda checked=False, tid=tour_id: open_tour_view(tid)
            )

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

        guides = dbconnect.get_active_guides(limit=4)
        fill_guide_cards_on_main(guide_ui, guides)

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
            lambda: list_reviews(guide_window)
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