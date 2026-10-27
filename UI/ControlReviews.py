# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlReviews.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(20, 65, 30, 255),\n"
"    stop:0.427447 rgba(35, 95, 55, 235),\n"
"    stop:1 rgba(110, 160, 90, 255));\n"
"")
        self.label_Admin = QLabel(Dialog)
        self.label_Admin.setObjectName(u"label_Admin")
        self.label_Admin.setGeometry(QRect(20, 10, 211, 31))
        self.label_Admin.setStyleSheet(u"background-color: none;\n"
"font-size: 20px;\n"
"border: none;\n"
"color: white;")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 50, 761, 531))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 231, 31))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 18px;\n"
"border: none;\n"
"color: white;")
        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setGeometry(QRect(20, 50, 721, 461))
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setEnabled(True)
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 710, 610))
        self.label_TouristName_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TouristName_5.setObjectName(u"label_TouristName_5")
        self.label_TouristName_5.setGeometry(QRect(10, 10, 291, 31))
        self.label_TouristName_5.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ActiveBookings_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ActiveBookings_5.setObjectName(u"label_ActiveBookings_5")
        self.label_ActiveBookings_5.setGeometry(QRect(10, 30, 201, 31))
        self.label_ActiveBookings_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_9 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_9.setObjectName(u"pushButton_Profile_9")
        self.pushButton_Profile_9.setGeometry(QRect(580, 20, 111, 31))
        self.pushButton_Profile_9.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_10 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_10.setObjectName(u"pushButton_Profile_10")
        self.pushButton_Profile_10.setGeometry(QRect(580, 90, 111, 31))
        self.pushButton_Profile_10.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ActiveBookings_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ActiveBookings_6.setObjectName(u"label_ActiveBookings_6")
        self.label_ActiveBookings_6.setGeometry(QRect(10, 100, 201, 31))
        self.label_ActiveBookings_6.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_TouristName_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TouristName_6.setObjectName(u"label_TouristName_6")
        self.label_TouristName_6.setGeometry(QRect(10, 80, 291, 31))
        self.label_TouristName_6.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ActiveBookings_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ActiveBookings_7.setObjectName(u"label_ActiveBookings_7")
        self.label_ActiveBookings_7.setGeometry(QRect(10, 170, 201, 31))
        self.label_ActiveBookings_7.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_11 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_11.setObjectName(u"pushButton_Profile_11")
        self.pushButton_Profile_11.setGeometry(QRect(580, 160, 111, 31))
        self.pushButton_Profile_11.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_TouristName_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TouristName_7.setObjectName(u"label_TouristName_7")
        self.label_TouristName_7.setGeometry(QRect(10, 150, 291, 31))
        self.label_TouristName_7.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_12 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_12.setObjectName(u"pushButton_Profile_12")
        self.pushButton_Profile_12.setGeometry(QRect(580, 230, 111, 31))
        self.pushButton_Profile_12.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ActiveBookings_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ActiveBookings_8.setObjectName(u"label_ActiveBookings_8")
        self.label_ActiveBookings_8.setGeometry(QRect(10, 240, 201, 31))
        self.label_ActiveBookings_8.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_TouristName_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TouristName_8.setObjectName(u"label_TouristName_8")
        self.label_TouristName_8.setGeometry(QRect(10, 220, 291, 31))
        self.label_TouristName_8.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_13 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_13.setObjectName(u"pushButton_Profile_13")
        self.pushButton_Profile_13.setGeometry(QRect(460, 20, 111, 31))
        self.pushButton_Profile_13.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_19 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_19.setObjectName(u"pushButton_Profile_19")
        self.pushButton_Profile_19.setGeometry(QRect(460, 90, 111, 31))
        self.pushButton_Profile_19.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_20 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_20.setObjectName(u"pushButton_Profile_20")
        self.pushButton_Profile_20.setGeometry(QRect(460, 160, 111, 31))
        self.pushButton_Profile_20.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_21 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_Profile_21.setObjectName(u"pushButton_Profile_21")
        self.pushButton_Profile_21.setGeometry(QRect(460, 230, 111, 31))
        self.pushButton_Profile_21.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_Logout = QPushButton(Dialog)
        self.pushButton_Logout.setObjectName(u"pushButton_Logout")
        self.pushButton_Logout.setGeometry(QRect(640, 10, 141, 31))
        self.pushButton_Logout.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 14px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_Admin.setText(QCoreApplication.translate("Dialog", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0437\u044b\u0432\u0430\u043c\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0437\u044b\u0432\u044b", None))
        self.label_TouristName_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0437\u044b\u0432 \u043d\u0430 \u0442\u0443\u0440 \"\u0412\u043e\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043e\u0440\u0443\"", None))
        self.label_ActiveBookings_5.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u0438\u0441\u0442: \u0415\u0432\u0433\u0435\u043d\u0438\u0439 \u0421\u043c\u0438\u0440\u043d\u043e\u0432", None))
        self.pushButton_Profile_9.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_Profile_10.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_ActiveBookings_6.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u0438\u0441\u0442: \u041c\u0430\u043a\u0441\u0438\u043c \u041a\u0430\u0440\u043f\u0435\u043d\u043a\u043e", None))
        self.label_TouristName_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0437\u044b\u0432 \u043d\u0430 \u0442\u0443\u0440 \"\u0421\u043f\u043b\u0430\u0432 \u043f\u043e \u0440\u0435\u043a\u0435 \u041f\u0435\u0447\u043e\u0440\u0430\"", None))
        self.label_ActiveBookings_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u0438\u0441\u0442: \u0415\u0432\u0433\u0435\u043d\u0438\u0439 \u0421\u043c\u0438\u0440\u043d\u043e\u0432", None))
        self.pushButton_Profile_11.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_TouristName_7.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0437\u044b\u0432 \u043d\u0430 \u0442\u0443\u0440 \"\u0421\u043f\u043b\u0430\u0432 \u043f\u043e \u0440\u0435\u043a\u0435 \u0412\u044b\u0447\u0435\u0433\u0434\u0430\"", None))
        self.pushButton_Profile_12.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_ActiveBookings_8.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u0438\u0441\u0442: \u0415\u0432\u0433\u0435\u043d\u0438\u0439 \u0421\u043c\u0438\u0440\u043d\u043e\u0432", None))
        self.label_TouristName_8.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0437\u044b\u0432 \u043d\u0430 \u0442\u0443\u0440 \"\u0412\u043e\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043e\u0440\u0443\"", None))
        self.pushButton_Profile_13.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.pushButton_Profile_19.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.pushButton_Profile_20.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.pushButton_Profile_21.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.pushButton_Logout.setText(QCoreApplication.translate("Dialog", u"\u0412 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

