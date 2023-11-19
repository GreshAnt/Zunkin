# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verset.ui'
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

class Ui_Form_VerSet(object):
    def setupUi(self, Form_VerSet):
        if not Form_VerSet.objectName():
            Form_VerSet.setObjectName(u"Form_VerSet")
        Form_VerSet.resize(800, 500)
        Form_VerSet.setMinimumSize(QSize(800, 500))
        Form_VerSet.setMaximumSize(QSize(800, 500))
        self.label = QLabel(Form_VerSet)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 110, 361, 271))
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)

        self.retranslateUi(Form_VerSet)

        QMetaObject.connectSlotsByName(Form_VerSet)
    # setupUi

    def retranslateUi(self, Form_VerSet):
        Form_VerSet.setWindowTitle(QCoreApplication.translate("Form_VerSet", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_VerSet", u"Verset", None))
    # retranslateUi

