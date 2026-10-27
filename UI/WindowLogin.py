# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(20, 65, 30, 255),\n"
"    stop:0.427447 rgba(35, 95, 55, 235),\n"
"    stop:1 rgba(110, 160, 90, 255));")
        self.pushButton_Login = QPushButton(Dialog)
        self.pushButton_Login.setObjectName(u"pushButton_Login")
        self.pushButton_Login.setGeometry(QRect(140, 190, 121, 31))
        self.pushButton_Login.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px;\n"
"font-size: 16px;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 61, 31))
        self.label.setStyleSheet(u"background-color: none;\n"
"font-size: 24px;")
        self.pushButton_Register = QPushButton(Dialog)
        self.pushButton_Register.setObjectName(u"pushButton_Register")
        self.pushButton_Register.setGeometry(QRect(80, 240, 111, 31))
        self.pushButton_Register.setStyleSheet(u"background-color: none;\n"
"color: rgb(190, 188, 184);\n"
"border: none;\n"
"font-size: 14px")
        self.pushButton_ForgetPass = QPushButton(Dialog)
        self.pushButton_ForgetPass.setObjectName(u"pushButton_ForgetPass")
        self.pushButton_ForgetPass.setGeometry(QRect(210, 240, 111, 31))
        self.pushButton_ForgetPass.setStyleSheet(u"background-color: none;\n"
"color: rgb(190, 188, 184);\n"
"border: none;\n"
"font-size: 14px")
        self.lineEdit_Login = QLineEdit(Dialog)
        self.lineEdit_Login.setObjectName(u"lineEdit_Login")
        self.lineEdit_Login.setGeometry(QRect(50, 70, 291, 41))
        self.lineEdit_Login.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.lineEdit_Password = QLineEdit(Dialog)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setGeometry(QRect(50, 130, 291, 41))
        self.lineEdit_Password.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_Login.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.pushButton_Register.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_ForgetPass.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_Login.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d:", None))
        self.lineEdit_Password.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
    # retranslateUi

