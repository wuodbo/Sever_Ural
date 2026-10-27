# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Notifications.ui'
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
        Dialog.resize(640, 440)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(20, 65, 30, 255),\n"
"    stop:0.427447 rgba(35, 95, 55, 235),\n"
"    stop:1 rgba(110, 160, 90, 255));")
        self.label_Guide = QLabel(Dialog)
        self.label_Guide.setObjectName(u"label_Guide")
        self.label_Guide.setGeometry(QRect(20, 10, 161, 31))
        self.label_Guide.setStyleSheet(u"background-color: none;\n"
"font-size: 24px;\n"
"border: none;\n"
"color: white;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 601, 371))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 20, 561, 331))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 550, 332))
        self.label_GuideName_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_GuideName_5.setObjectName(u"label_GuideName_5")
        self.label_GuideName_5.setGeometry(QRect(10, 10, 231, 31))
        self.label_GuideName_5.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_GuideName_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_GuideName_7.setObjectName(u"label_GuideName_7")
        self.label_GuideName_7.setGeometry(QRect(10, 130, 221, 31))
        self.label_GuideName_7.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_Role_5.setObjectName(u"label_Role_5")
        self.label_Role_5.setGeometry(QRect(10, 90, 101, 31))
        self.label_Role_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_4.setObjectName(u"pushButton_Profile_4")
        self.pushButton_Profile_4.setGeometry(QRect(300, 20, 111, 31))
        self.pushButton_Profile_4.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_7.setObjectName(u"pushButton_Profile_7")
        self.pushButton_Profile_7.setGeometry(QRect(300, 80, 111, 31))
        self.pushButton_Profile_7.setStyleSheet(u"background-color: rgba(110, 115, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_6.setObjectName(u"pushButton_Profile_6")
        self.pushButton_Profile_6.setGeometry(QRect(420, 80, 111, 31))
        self.pushButton_Profile_6.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.label_Role_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_Role_4.setObjectName(u"label_Role_4")
        self.label_Role_4.setGeometry(QRect(10, 30, 101, 31))
        self.label_Role_4.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_Role_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_Role_6.setObjectName(u"label_Role_6")
        self.label_Role_6.setGeometry(QRect(10, 150, 101, 31))
        self.label_Role_6.setStyleSheet(u"background-color: none;\n"
"font-size: 14px;\n"
"border: none;\n"
"color: white;")
        self.label_GuideName_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_GuideName_6.setObjectName(u"label_GuideName_6")
        self.label_GuideName_6.setGeometry(QRect(10, 70, 221, 31))
        self.label_GuideName_6.setStyleSheet(u"background-color: none;\n"
"font-size: 16px;\n"
"border: none;\n"
"color: white;")
        self.pushButton_Profile_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_5.setObjectName(u"pushButton_Profile_5")
        self.pushButton_Profile_5.setGeometry(QRect(420, 20, 111, 31))
        self.pushButton_Profile_5.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.pushButton_Profile_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Profile_8.setObjectName(u"pushButton_Profile_8")
        self.pushButton_Profile_8.setGeometry(QRect(420, 140, 111, 31))
        self.pushButton_Profile_8.setStyleSheet(u"background-color: rgba(140, 110, 110, 140);\n"
"color: rgba(235, 235, 232, 235);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 8px 18px;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_Logout = QPushButton(Dialog)
        self.pushButton_Logout.setObjectName(u"pushButton_Logout")
        self.pushButton_Logout.setGeometry(QRect(480, 10, 141, 31))
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
        self.label_Guide.setText(QCoreApplication.translate("Dialog", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.label_GuideName_5.setText(QCoreApplication.translate("Dialog", u"\u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e!", None))
        self.label_GuideName_7.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0437\u044b\u0432 \u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d!", None))
        self.label_Role_5.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u043f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e", None))
        self.pushButton_Profile_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_Profile_7.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_Profile_6.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_Role_4.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u043f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e", None))
        self.label_Role_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e", None))
        self.label_GuideName_6.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440 \u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d!", None))
        self.pushButton_Profile_5.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_Profile_8.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_Logout.setText(QCoreApplication.translate("Dialog", u"\u0412 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

