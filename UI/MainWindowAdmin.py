# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowAdmin.ui'
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
        self.label_Admin = QLabel(self.frame)
        self.label_Admin.setObjectName(u"label_Admin")
        self.label_Admin.setGeometry(QRect(90, 30, 141, 31))
        self.label_Admin.setStyleSheet(u"background-color: none;\n"
"font-size: 18px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageAdmin = QLabel(self.frame)
        self.label_ImageAdmin.setObjectName(u"label_ImageAdmin")
        self.label_ImageAdmin.setGeometry(QRect(20, 20, 51, 51))
        self.label_ImageAdmin.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.pushButton_ControlTourist = QPushButton(self.frame)
        self.pushButton_ControlTourist.setObjectName(u"pushButton_ControlTourist")
        self.pushButton_ControlTourist.setGeometry(QRect(20, 90, 211, 31))
        self.pushButton_ControlTourist.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_ControlTour = QPushButton(self.frame)
        self.pushButton_ControlTour.setObjectName(u"pushButton_ControlTour")
        self.pushButton_ControlTour.setGeometry(QRect(20, 130, 211, 31))
        self.pushButton_ControlTour.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_ControlReview = QPushButton(self.frame)
        self.pushButton_ControlReview.setObjectName(u"pushButton_ControlReview")
        self.pushButton_ControlReview.setGeometry(QRect(20, 170, 211, 31))
        self.pushButton_ControlReview.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Route = QPushButton(self.frame)
        self.pushButton_Route.setObjectName(u"pushButton_Route")
        self.pushButton_Route.setGeometry(QRect(20, 210, 211, 31))
        self.pushButton_Route.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Equipment = QPushButton(self.frame)
        self.pushButton_Equipment.setObjectName(u"pushButton_Equipment")
        self.pushButton_Equipment.setGeometry(QRect(20, 250, 211, 31))
        self.pushButton_Equipment.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
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
        self.pushButton_Logs = QPushButton(self.frame)
        self.pushButton_Logs.setObjectName(u"pushButton_Logs")
        self.pushButton_Logs.setGeometry(QRect(20, 290, 211, 31))
        self.pushButton_Logs.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(290, 20, 591, 631))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(20, 120, 551, 491))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 535, 510))
        self.label_TouristName = QLabel(self.scrollAreaWidgetContents)
        self.label_TouristName.setObjectName(u"label_TouristName")
        self.label_TouristName.setGeometry(QRect(70, 10, 101, 31))
        self.label_TouristName.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_Role = QLabel(self.scrollAreaWidgetContents)
        self.label_Role.setObjectName(u"label_Role")
        self.label_Role.setGeometry(QRect(70, 30, 101, 31))
        self.label_Role.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTourist = QLabel(self.scrollAreaWidgetContents)
        self.label_ImageTourist.setObjectName(u"label_ImageTourist")
        self.label_ImageTourist.setGeometry(QRect(10, 10, 51, 50))
        self.label_ImageTourist.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_ActiveBookings = QLabel(self.scrollAreaWidgetContents)
        self.label_ActiveBookings.setObjectName(u"label_ActiveBookings")
        self.label_ActiveBookings.setGeometry(QRect(10, 60, 201, 31))
        self.label_ActiveBookings.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile.setObjectName(u"pushButton_Profile")
        self.pushButton_Profile.setGeometry(QRect(410, 10, 111, 31))
        self.pushButton_Profile.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_2.setObjectName(u"pushButton_Profile_2")
        self.pushButton_Profile_2.setGeometry(QRect(410, 120, 111, 31))
        self.pushButton_Profile_2.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ActiveBookings_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_ActiveBookings_2.setObjectName(u"label_ActiveBookings_2")
        self.label_ActiveBookings_2.setGeometry(QRect(10, 170, 201, 31))
        self.label_ActiveBookings_2.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_Role_2.setObjectName(u"label_Role_2")
        self.label_Role_2.setGeometry(QRect(70, 140, 101, 31))
        self.label_Role_2.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_TouristName_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_TouristName_2.setObjectName(u"label_TouristName_2")
        self.label_TouristName_2.setGeometry(QRect(70, 120, 131, 31))
        self.label_TouristName_2.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTourist_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_ImageTourist_2.setObjectName(u"label_ImageTourist_2")
        self.label_ImageTourist_2.setGeometry(QRect(10, 120, 51, 50))
        self.label_ImageTourist_2.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.pushButton_Profile_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_3.setObjectName(u"pushButton_Profile_3")
        self.pushButton_Profile_3.setGeometry(QRect(410, 230, 111, 31))
        self.pushButton_Profile_3.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ImageGuide = QLabel(self.scrollAreaWidgetContents)
        self.label_ImageGuide.setObjectName(u"label_ImageGuide")
        self.label_ImageGuide.setGeometry(QRect(10, 230, 51, 50))
        self.label_ImageGuide.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_GuideName_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_GuideName_4.setObjectName(u"label_GuideName_4")
        self.label_GuideName_4.setGeometry(QRect(70, 230, 131, 31))
        self.label_GuideName_4.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_Role_3.setObjectName(u"label_Role_3")
        self.label_Role_3.setGeometry(QRect(70, 250, 101, 31))
        self.label_Role_3.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ActiveTours = QLabel(self.scrollAreaWidgetContents)
        self.label_ActiveTours.setObjectName(u"label_ActiveTours")
        self.label_ActiveTours.setGeometry(QRect(10, 280, 201, 31))
        self.label_ActiveTours.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Specialization = QLabel(self.scrollAreaWidgetContents)
        self.label_Specialization.setObjectName(u"label_Specialization")
        self.label_Specialization.setGeometry(QRect(10, 310, 241, 31))
        self.label_Specialization.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_4.setObjectName(u"pushButton_Profile_4")
        self.pushButton_Profile_4.setGeometry(QRect(410, 360, 111, 31))
        self.pushButton_Profile_4.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_Specialization_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_Specialization_2.setObjectName(u"label_Specialization_2")
        self.label_Specialization_2.setGeometry(QRect(10, 440, 241, 31))
        self.label_Specialization_2.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ActiveTours_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_ActiveTours_2.setObjectName(u"label_ActiveTours_2")
        self.label_ActiveTours_2.setGeometry(QRect(10, 410, 201, 31))
        self.label_ActiveTours_2.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_GuideName_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_GuideName_5.setObjectName(u"label_GuideName_5")
        self.label_GuideName_5.setGeometry(QRect(70, 360, 131, 31))
        self.label_GuideName_5.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageGuide_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_ImageGuide_2.setObjectName(u"label_ImageGuide_2")
        self.label_ImageGuide_2.setGeometry(QRect(10, 360, 51, 50))
        self.label_ImageGuide_2.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_Role_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_Role_4.setObjectName(u"label_Role_4")
        self.label_Role_4.setGeometry(QRect(70, 380, 101, 31))
        self.label_Role_4.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit_Search = QLineEdit(self.frame_2)
        self.lineEdit_Search.setObjectName(u"lineEdit_Search")
        self.lineEdit_Search.setGeometry(QRect(20, 30, 421, 41))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 201, 31))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Search = QPushButton(self.frame_2)
        self.pushButton_Search.setObjectName(u"pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(460, 30, 111, 31))
        self.pushButton_Search.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.pushButton_Search_2 = QPushButton(self.frame_2)
        self.pushButton_Search_2.setObjectName(u"pushButton_Search_2")
        self.pushButton_Search_2.setGeometry(QRect(460, 70, 111, 31))
        self.pushButton_Search_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 201, 31))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
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
        self.label_Admin.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.label_ImageAdmin.setText("")
        self.pushButton_ControlTourist.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.pushButton_ControlTour.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u0443\u0440\u0430\u043c\u0438", None))
        self.pushButton_ControlReview.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0437\u044b\u0432\u0430\u043c\u0438", None))
        self.pushButton_Route.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.pushButton_Equipment.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043d\u0430\u0440\u044f\u0436\u0435\u043d\u0438\u0435", None))
        self.pushButton_Logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_Logs.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
        self.label_TouristName.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0432\u0430\u043d \u041f\u0435\u0442\u0440\u043e\u0432", None))
        self.label_Role.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0442\u0443\u0440\u0438\u0441\u0442", None))
        self.label_ImageTourist.setText("")
        self.label_ActiveBookings.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0439: 2", None))
        self.pushButton_Profile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.pushButton_Profile_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.label_ActiveBookings_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0439: 4", None))
        self.label_Role_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0442\u0443\u0440\u0438\u0441\u0442", None))
        self.label_TouristName_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c \u0421\u043c\u0438\u0440\u043d\u043e\u0432", None))
        self.label_ImageTourist_2.setText("")
        self.pushButton_Profile_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.label_ImageGuide.setText("")
        self.label_GuideName_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0440\u044c\u044f \u041a\u0430\u0440\u043f\u0435\u043d\u043a\u043e", None))
        self.label_Role_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0433\u0438\u0434", None))
        self.label_ActiveTours.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0442\u0443\u0440\u043e\u0432: 2", None))
        self.label_Specialization.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0433\u043e\u0440\u043d\u044b\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u044b", None))
        self.pushButton_Profile_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.label_Specialization_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0432\u043e\u0434\u043d\u044b\u0435 \u0441\u043f\u043b\u0430\u0432\u044b", None))
        self.label_ActiveTours_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0442\u0443\u0440\u043e\u0432: 2", None))
        self.label_GuideName_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0438\u044f \u041f\u043e\u043f\u043e\u0432\u0430", None))
        self.label_ImageGuide_2.setText("")
        self.label_Role_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c: \u0433\u0438\u0434", None))
        self.lineEdit_Search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_Search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_Search_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
    # retranslateUi

