# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListTour.ui'
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
        Dialog.resize(900, 700)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(20, 65, 30, 255),\n"
"    stop:0.427447 rgba(35, 95, 55, 235),\n"
"    stop:1 rgba(110, 160, 90, 255));\n"
"")
        self.label_Admin = QLabel(Dialog)
        self.label_Admin.setObjectName(u"label_Admin")
        self.label_Admin.setGeometry(QRect(30, 20, 211, 31))
        self.label_Admin.setStyleSheet(u"background-color: none;\n"
"font-size: 20px;\n"
"border: none;\n"
"color: white;")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 60, 841, 631))
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
        self.scrollArea_2.setGeometry(QRect(20, 50, 801, 561))
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setEnabled(True)
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 790, 610))
        self.label_TourName = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TourName.setObjectName(u"label_TourName")
        self.label_TourName.setGeometry(QRect(70, 10, 371, 31))
        self.label_TourName.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTour = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ImageTour.setObjectName(u"label_ImageTour")
        self.label_ImageTour.setGeometry(QRect(10, 10, 51, 50))
        self.label_ImageTour.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_GuideName = QLabel(self.scrollAreaWidgetContents_3)
        self.label_GuideName.setObjectName(u"label_GuideName")
        self.label_GuideName.setGeometry(QRect(70, 30, 181, 31))
        self.label_GuideName.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_OnBooking = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_OnBooking.setObjectName(u"pushButton_OnBooking")
        self.pushButton_OnBooking.setGeometry(QRect(660, 20, 111, 31))
        self.pushButton_OnBooking.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_OnBooking_2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_OnBooking_2.setObjectName(u"pushButton_OnBooking_2")
        self.pushButton_OnBooking_2.setGeometry(QRect(660, 110, 111, 31))
        self.pushButton_OnBooking_2.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_TourName_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TourName_2.setObjectName(u"label_TourName_2")
        self.label_TourName_2.setGeometry(QRect(70, 100, 391, 31))
        self.label_TourName_2.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTour_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ImageTour_2.setObjectName(u"label_ImageTour_2")
        self.label_ImageTour_2.setGeometry(QRect(10, 100, 51, 50))
        self.label_ImageTour_2.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_GuideName_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_GuideName_2.setObjectName(u"label_GuideName_2")
        self.label_GuideName_2.setGeometry(QRect(70, 120, 181, 31))
        self.label_GuideName_2.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_OnBooking_3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_OnBooking_3.setObjectName(u"pushButton_OnBooking_3")
        self.pushButton_OnBooking_3.setGeometry(QRect(660, 200, 111, 31))
        self.pushButton_OnBooking_3.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_ImageTour_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ImageTour_3.setObjectName(u"label_ImageTour_3")
        self.label_ImageTour_3.setGeometry(QRect(10, 190, 51, 50))
        self.label_ImageTour_3.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.label_TourName_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TourName_3.setObjectName(u"label_TourName_3")
        self.label_TourName_3.setGeometry(QRect(70, 190, 411, 31))
        self.label_TourName_3.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_GuideName_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_GuideName_3.setObjectName(u"label_GuideName_3")
        self.label_GuideName_3.setGeometry(QRect(70, 210, 181, 31))
        self.label_GuideName_3.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTour_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ImageTour_4.setObjectName(u"label_ImageTour_4")
        self.label_ImageTour_4.setGeometry(QRect(10, 280, 51, 50))
        self.label_ImageTour_4.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.pushButton_OnBooking_4 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_OnBooking_4.setObjectName(u"pushButton_OnBooking_4")
        self.pushButton_OnBooking_4.setGeometry(QRect(660, 290, 111, 31))
        self.pushButton_OnBooking_4.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_GuideName_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_GuideName_4.setObjectName(u"label_GuideName_4")
        self.label_GuideName_4.setGeometry(QRect(70, 300, 181, 31))
        self.label_GuideName_4.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_TourName_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TourName_4.setObjectName(u"label_TourName_4")
        self.label_TourName_4.setGeometry(QRect(70, 280, 421, 31))
        self.label_TourName_4.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_OnBooking_5 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_OnBooking_5.setObjectName(u"pushButton_OnBooking_5")
        self.pushButton_OnBooking_5.setGeometry(QRect(660, 380, 111, 31))
        self.pushButton_OnBooking_5.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_GuideName_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_GuideName_5.setObjectName(u"label_GuideName_5")
        self.label_GuideName_5.setGeometry(QRect(70, 390, 181, 31))
        self.label_GuideName_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_TourName_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_TourName_5.setObjectName(u"label_TourName_5")
        self.label_TourName_5.setGeometry(QRect(70, 370, 401, 31))
        self.label_TourName_5.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_ImageTour_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_ImageTour_5.setObjectName(u"label_ImageTour_5")
        self.label_ImageTour_5.setGeometry(QRect(10, 370, 51, 50))
        self.label_ImageTour_5.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_Logout = QPushButton(Dialog)
        self.pushButton_Logout.setObjectName(u"pushButton_Logout")
        self.pushButton_Logout.setGeometry(QRect(730, 20, 141, 31))
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
        self.label_Admin.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u044b", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u0442\u0443\u0440\u044b", None))
        self.label_TourName.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043b\u0430\u0432 \u043f\u043e \u0440\u0435\u043a\u0435 \u041f\u0435\u0447\u043e\u0440\u0430", None))
        self.label_ImageTour.setText("")
        self.label_GuideName.setText(QCoreApplication.translate("Dialog", u"\u0413\u0438\u0434: \u0414\u0430\u0440\u044c\u044f \u041a\u0430\u0440\u043f\u0435\u043d\u043a\u043e", None))
        self.pushButton_OnBooking.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.pushButton_OnBooking_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.label_TourName_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043e\u0440\u0443", None))
        self.label_ImageTour_2.setText("")
        self.label_GuideName_2.setText(QCoreApplication.translate("Dialog", u"\u0413\u0438\u0434: \u0410\u043d\u0434\u0440\u0435\u0439 \u0410\u043d\u0442\u043e\u043d\u043e\u0432", None))
        self.pushButton_OnBooking_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.label_ImageTour_3.setText("")
        self.label_TourName_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043b\u0430\u0432 \u043f\u043e \u0440\u0435\u043a\u0435 \u0412\u044b\u0447\u0435\u0433\u0434\u0430", None))
        self.label_GuideName_3.setText(QCoreApplication.translate("Dialog", u"\u0413\u0438\u0434: \u0410\u043d\u0434\u0440\u0435\u0439 \u0410\u043d\u0442\u043e\u043d\u043e\u0432", None))
        self.label_ImageTour_4.setText("")
        self.pushButton_OnBooking_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.label_GuideName_4.setText(QCoreApplication.translate("Dialog", u"\u0413\u0438\u0434: \u0414\u0430\u0440\u044c\u044f \u041a\u0430\u0440\u043f\u0435\u043d\u043a\u043e", None))
        self.label_TourName_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043b\u0430\u0432 \u043f\u043e \u0440\u0435\u043a\u0435 \u041f\u0435\u0447\u043e\u0440\u0430", None))
        self.pushButton_OnBooking_5.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.label_GuideName_5.setText(QCoreApplication.translate("Dialog", u"\u0413\u0438\u0434: \u0410\u043d\u0434\u0440\u0435\u0439 \u0410\u043d\u0442\u043e\u043d\u043e\u0432", None))
        self.label_TourName_5.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043e\u0440\u0443", None))
        self.label_ImageTour_5.setText("")
        self.pushButton_Logout.setText(QCoreApplication.translate("Dialog", u"\u0412 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

