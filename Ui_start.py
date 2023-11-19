# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

from qfluentwidgets import PushButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QSize(800, 500))
        Form.setMaximumSize(QSize(800, 500))
        self.PushButton = PushButton(Form)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(550, 390, 151, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(14)
        font.setBold(True)
        self.PushButton.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 15, 750, 350))
        self.VerSet = PushButton(Form)
        self.VerSet.setObjectName(u"VerSet")
        self.VerSet.setGeometry(QRect(440, 440, 102, 41))
        self.VerCon = PushButton(Form)
        self.VerCon.setObjectName(u"VerCon")
        self.VerCon.setGeometry(QRect(440, 380, 102, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u6e38\u620f", None))
        self.label.setText("")
        self.VerSet.setText(QCoreApplication.translate("Form", u"\u7248\u672c\u8bbe\u7f6e", None))
        self.VerCon.setText(QCoreApplication.translate("Form", u"\u7248\u672c\u9009\u62e9", None))
    # retranslateUi

