# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tour.ui'
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
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 440)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(20, 65, 30, 255),\n"
"    stop:0.427447 rgba(35, 95, 55, 235),\n"
"    stop:1 rgba(110, 160, 90, 255));")
        self.label_Guide = QLabel(Dialog)
        self.label_Guide.setObjectName(u"label_Guide")
        self.label_Guide.setGeometry(QRect(540, 10, 41, 31))
        self.label_Guide.setStyleSheet(u"background-color: none;\n"
"font-size: 24px;\n"
"border: none;\n"
"color: white;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 70, 291, 41))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 201, 191))
        self.label.setStyleSheet(u"background-color: white;\n"
"border-radius: 8px;")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 120, 291, 41))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 561, 371))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_Guide_2 = QLabel(self.frame)
        self.label_Guide_2.setObjectName(u"label_Guide_2")
        self.label_Guide_2.setGeometry(QRect(250, 120, 141, 31))
        self.label_Guide_2.setStyleSheet(u"background-color: none;\n"
"font-size: 18px;\n"
"border: none;\n"
"color: white;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 150, 291, 41))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.label_Guide_3 = QLabel(self.frame)
        self.label_Guide_3.setObjectName(u"label_Guide_3")
        self.label_Guide_3.setGeometry(QRect(250, 200, 141, 31))
        self.label_Guide_3.setStyleSheet(u"background-color: none;\n"
"font-size: 18px;\n"
"border: none;\n"
"color: white;")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 230, 291, 41))
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.label_Guide_4 = QLabel(self.frame)
        self.label_Guide_4.setObjectName(u"label_Guide_4")
        self.label_Guide_4.setGeometry(QRect(250, 280, 141, 31))
        self.label_Guide_4.setStyleSheet(u"background-color: none;\n"
"font-size: 18px;\n"
"border: none;\n"
"color: white;")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 310, 291, 41))
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.15);\n"
"color: rgb(235, 245, 235);\n"
"border: 1px solid rgba(255, 255, 255, 0.35);\n"
"border-radius: 8px")
        self.frame.raise_()
        self.label_Guide.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_Guide.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043b\u0430\u0432 \u043f\u043e \u0440\u0435\u043a\u0435 \u041f\u0435\u0447\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.label_Guide_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.label_Guide_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"20.10.2026", None))
        self.label_Guide_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"25.10.2026", None))
    # retranslateUi

