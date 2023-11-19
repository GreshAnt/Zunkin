# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(800, 500)
        Settings.setMinimumSize(QSize(800, 500))
        Settings.setMaximumSize(QSize(800, 500))
        self.Game = PushButton(Settings)
        self.Game.setObjectName(u"Game")
        self.Game.setGeometry(QRect(20, 170, 101, 31))
        self.Launcher = PushButton(Settings)
        self.Launcher.setObjectName(u"Launcher")
        self.Launcher.setGeometry(QRect(20, 230, 101, 31))
        self.SelectionCriteria = QLabel(Settings)
        self.SelectionCriteria.setObjectName(u"SelectionCriteria")
        self.SelectionCriteria.setGeometry(QRect(20, 180, 16, 16))
        self.SelectionCriteria2 = QLabel(Settings)
        self.SelectionCriteria2.setObjectName(u"SelectionCriteria2")
        self.SelectionCriteria2.setGeometry(QRect(20, 240, 16, 16))
        self.refreshGame = PushButton(Settings)
        self.refreshGame.setObjectName(u"refreshGame")
        self.refreshGame.setGeometry(QRect(120, 170, 31, 32))
        self.refreshLaucher = PushButton(Settings)
        self.refreshLaucher.setObjectName(u"refreshLaucher")
        self.refreshLaucher.setGeometry(QRect(120, 230, 31, 32))

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.Game.setText(QCoreApplication.translate("Settings", u"\u6e38\u620f", None))
        self.Launcher.setText(QCoreApplication.translate("Settings", u"\u542f\u52a8\u5668", None))
        self.SelectionCriteria.setText("")
        self.SelectionCriteria2.setText("")
        self.refreshGame.setText("")
        self.refreshLaucher.setText("")
    # retranslateUi

