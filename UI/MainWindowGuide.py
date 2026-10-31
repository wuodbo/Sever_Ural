# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainwindowGuide.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(20, 65, 30, 255),\n"
"    stop:0.427447 rgba(35, 95, 55, 235),\n"
"    stop:1 rgba(110, 160, 90, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 251, 631))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_Guide = QLabel(self.frame)
        self.label_Guide.setObjectName(u"label_Guide")
        self.label_Guide.setGeometry(QRect(90, 30, 141, 31))
        self.label_Guide.setStyleSheet(u"background-color: none;\n"
"font-size: 18px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageGuide = QLabel(self.frame)
        self.label_ImageGuide.setObjectName(u"label_ImageGuide")
        self.label_ImageGuide.setGeometry(QRect(20, 20, 51, 51))
        self.label_ImageGuide.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.pushButton_Tour = QPushButton(self.frame)
        self.pushButton_Tour.setObjectName(u"pushButton_Tour")
        self.pushButton_Tour.setGeometry(QRect(20, 90, 211, 31))
        self.pushButton_Tour.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Guide = QPushButton(self.frame)
        self.pushButton_Guide.setObjectName(u"pushButton_Guide")
        self.pushButton_Guide.setGeometry(QRect(20, 130, 211, 31))
        self.pushButton_Guide.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Review = QPushButton(self.frame)
        self.pushButton_Review.setObjectName(u"pushButton_Review")
        self.pushButton_Review.setGeometry(QRect(20, 170, 211, 31))
        self.pushButton_Review.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Booking = QPushButton(self.frame)
        self.pushButton_Booking.setObjectName(u"pushButton_Booking")
        self.pushButton_Booking.setGeometry(QRect(20, 210, 211, 31))
        self.pushButton_Booking.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_ControlTour = QPushButton(self.frame)
        self.pushButton_ControlTour.setObjectName(u"pushButton_ControlTour")
        self.pushButton_ControlTour.setGeometry(QRect(20, 250, 211, 31))
        self.pushButton_ControlTour.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Logout = QPushButton(self.frame)
        self.pushButton_Logout.setObjectName(u"pushButton_Logout")
        self.pushButton_Logout.setGeometry(QRect(20, 580, 111, 31))
        self.pushButton_Logout.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_ControlTour_2 = QPushButton(self.frame)
        self.pushButton_ControlTour_2.setObjectName(u"pushButton_ControlTour_2")
        self.pushButton_ControlTour_2.setGeometry(QRect(20, 290, 211, 31))
        self.pushButton_ControlTour_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_ControlTour_3 = QPushButton(self.frame)
        self.pushButton_ControlTour_3.setObjectName(u"pushButton_ControlTour_3")
        self.pushButton_ControlTour_3.setGeometry(QRect(20, 330, 211, 31))
        self.pushButton_ControlTour_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_ControlTour_4 = QPushButton(self.frame)
        self.pushButton_ControlTour_4.setObjectName(u"pushButton_ControlTour_4")
        self.pushButton_ControlTour_4.setGeometry(QRect(20, 370, 211, 31))
        self.pushButton_ControlTour_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(290, 20, 591, 631))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_Search = QLineEdit(self.frame_3)
        self.lineEdit_Search.setObjectName(u"lineEdit_Search")
        self.lineEdit_Search.setGeometry(QRect(20, 30, 421, 41))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 201, 31))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Search = QPushButton(self.frame_3)
        self.pushButton_Search.setObjectName(u"pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(460, 30, 111, 31))
        self.pushButton_Search.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Search_2 = QPushButton(self.frame_3)
        self.pushButton_Search_2.setObjectName(u"pushButton_Search_2")
        self.pushButton_Search_2.setGeometry(QRect(460, 70, 111, 31))
        self.pushButton_Search_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 201, 31))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(20, 120, 551, 491))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setEnabled(True)
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 535, 510))
        self.label_TouristName_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_TouristName_3.setObjectName(u"label_TouristName_3")
        self.label_TouristName_3.setGeometry(QRect(70, 10, 281, 31))
        self.label_TouristName_3.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Role_5.setObjectName(u"label_Role_5")
        self.label_Role_5.setGeometry(QRect(70, 30, 101, 31))
        self.label_Role_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTourist_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ImageTourist_3.setObjectName(u"label_ImageTourist_3")
        self.label_ImageTourist_3.setGeometry(QRect(10, 10, 51, 50))
        self.label_ImageTourist_3.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_ActiveBookings_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ActiveBookings_3.setObjectName(u"label_ActiveBookings_3")
        self.label_ActiveBookings_3.setGeometry(QRect(10, 60, 201, 31))
        self.label_ActiveBookings_3.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_Profile_5.setObjectName(u"pushButton_Profile_5")
        self.pushButton_Profile_5.setGeometry(QRect(410, 10, 111, 31))
        self.pushButton_Profile_5.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_Profile_6.setObjectName(u"pushButton_Profile_6")
        self.pushButton_Profile_6.setGeometry(QRect(410, 130, 111, 31))
        self.pushButton_Profile_6.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ActiveBookings_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ActiveBookings_4.setObjectName(u"label_ActiveBookings_4")
        self.label_ActiveBookings_4.setGeometry(QRect(10, 180, 201, 31))
        self.label_ActiveBookings_4.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Role_6.setObjectName(u"label_Role_6")
        self.label_Role_6.setGeometry(QRect(70, 150, 101, 31))
        self.label_Role_6.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_TouristName_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_TouristName_4.setObjectName(u"label_TouristName_4")
        self.label_TouristName_4.setGeometry(QRect(70, 130, 291, 31))
        self.label_TouristName_4.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTourist_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ImageTourist_4.setObjectName(u"label_ImageTourist_4")
        self.label_ImageTourist_4.setGeometry(QRect(10, 130, 51, 50))
        self.label_ImageTourist_4.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.pushButton_Profile_7 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_Profile_7.setObjectName(u"pushButton_Profile_7")
        self.pushButton_Profile_7.setGeometry(QRect(410, 250, 111, 31))
        self.pushButton_Profile_7.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ImageGuide_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ImageGuide_4.setObjectName(u"label_ImageGuide_4")
        self.label_ImageGuide_4.setGeometry(QRect(10, 250, 51, 50))
        self.label_ImageGuide_4.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_GuideName_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_GuideName_6.setObjectName(u"label_GuideName_6")
        self.label_GuideName_6.setGeometry(QRect(70, 250, 301, 31))
        self.label_GuideName_6.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Role_7.setObjectName(u"label_Role_7")
        self.label_Role_7.setGeometry(QRect(70, 270, 101, 31))
        self.label_Role_7.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ActiveTours_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ActiveTours_3.setObjectName(u"label_ActiveTours_3")
        self.label_ActiveTours_3.setGeometry(QRect(10, 300, 201, 31))
        self.label_ActiveTours_3.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Specialization_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Specialization_5.setObjectName(u"label_Specialization_5")
        self.label_Specialization_5.setGeometry(QRect(10, 320, 341, 31))
        self.label_Specialization_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_8 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_Profile_8.setObjectName(u"pushButton_Profile_8")
        self.pushButton_Profile_8.setGeometry(QRect(410, 370, 111, 31))
        self.pushButton_Profile_8.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_Specialization_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Specialization_6.setObjectName(u"label_Specialization_6")
        self.label_Specialization_6.setGeometry(QRect(10, 440, 351, 31))
        self.label_Specialization_6.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ActiveTours_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ActiveTours_4.setObjectName(u"label_ActiveTours_4")
        self.label_ActiveTours_4.setGeometry(QRect(10, 420, 201, 31))
        self.label_ActiveTours_4.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_GuideName_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_GuideName_7.setObjectName(u"label_GuideName_7")
        self.label_GuideName_7.setGeometry(QRect(70, 370, 271, 31))
        self.label_GuideName_7.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageGuide_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ImageGuide_5.setObjectName(u"label_ImageGuide_5")
        self.label_ImageGuide_5.setGeometry(QRect(10, 370, 51, 50))
        self.label_ImageGuide_5.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_Role_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Role_8.setObjectName(u"label_Role_8")
        self.label_Role_8.setGeometry(QRect(70, 390, 101, 31))
        self.label_Role_8.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Specialization_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Specialization_7.setObjectName(u"label_Specialization_7")
        self.label_Specialization_7.setGeometry(QRect(10, 200, 381, 31))
        self.label_Specialization_7.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Specialization_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Specialization_8.setObjectName(u"label_Specialization_8")
        self.label_Specialization_8.setGeometry(QRect(10, 80, 381, 31))
        self.label_Specialization_8.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Guide.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0438\u0434", None))
        self.label_ImageGuide.setText("")
        self.pushButton_Tour.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0442\u0443\u0440\u043e\u0432", None))
        self.pushButton_Guide.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0433\u0438\u0434\u043e\u0432", None))
        self.pushButton_Review.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0437\u044b\u0432\u044b", None))
        self.pushButton_Booking.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.pushButton_ControlTour.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_Logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_ControlTour_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0442\u0443\u0440\u044b", None))
        self.pushButton_ControlTour_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0443\u0440", None))
        self.pushButton_ControlTour_4.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.lineEdit_Search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_Search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_Search_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label_TouristName_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0432\u0430\u043d \u041f\u0435\u0442\u0440\u043e\u0432", None))
        self.label_Role_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0433\u0438\u0434", None))
        self.label_ImageTourist_3.setText("")
        self.label_ActiveBookings_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0442\u0443\u0440\u043e\u0432: 2", None))
        self.pushButton_Profile_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.pushButton_Profile_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.label_ActiveBookings_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0442\u0443\u0440\u043e\u0432: 2", None))
        self.label_Role_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0433\u0438\u0434", None))
        self.label_TouristName_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c \u0421\u043c\u0438\u0440\u043d\u043e\u0432", None))
        self.label_ImageTourist_4.setText("")
        self.pushButton_Profile_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.label_ImageGuide_4.setText("")
        self.label_GuideName_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0440\u044c\u044f \u041a\u0430\u0440\u043f\u0435\u043d\u043a\u043e", None))
        self.label_Role_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0433\u0438\u0434", None))
        self.label_ActiveTours_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0442\u0443\u0440\u043e\u0432: 2", None))
        self.label_Specialization_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0433\u043e\u0440\u043d\u044b\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u044b", None))
        self.pushButton_Profile_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.label_Specialization_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0432\u043e\u0434\u043d\u044b\u0435 \u0441\u043f\u043b\u0430\u0432\u044b", None))
        self.label_ActiveTours_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0442\u0443\u0440\u043e\u0432: 2", None))
        self.label_GuideName_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0438\u044f \u041f\u043e\u043f\u043e\u0432\u0430", None))
        self.label_ImageGuide_5.setText("")
        self.label_Role_8.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0433\u0438\u0434", None))
        self.label_Specialization_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0433\u043e\u0440\u043d\u044b\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u044b", None))
        self.label_Specialization_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0433\u043e\u0440\u043d\u044b\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u044b", None))
    # retranslateUi

