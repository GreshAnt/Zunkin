# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from qfluentwidgets import (BodyLabel, PushButton)

class Ui_download(object):
    def setupUi(self, download):
        if not download.objectName():
            download.setObjectName(u"download")
        download.resize(800, 500)
        download.setMinimumSize(QSize(800, 500))
        download.setMaximumSize(QSize(800, 500))
        self.Minecraft = BodyLabel(download)
        self.Minecraft.setObjectName(u"Minecraft")
        self.Minecraft.setGeometry(QRect(50, 100, 71, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        self.Minecraft.setFont(font)
        self.BodyLabel = BodyLabel(download)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setGeometry(QRect(50, 260, 63, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Historic"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.BodyLabel.setFont(font1)
        self.AutoInstall = PushButton(download)
        self.AutoInstall.setObjectName(u"AutoInstall")
        self.AutoInstall.setGeometry(QRect(50, 140, 102, 32))
        self.Pack = PushButton(download)
        self.Pack.setObjectName(u"Pack")
        self.Pack.setGeometry(QRect(50, 350, 102, 32))
        self.Mod = PushButton(download)
        self.Mod.setObjectName(u"Mod")
        self.Mod.setGeometry(QRect(50, 300, 102, 32))

        self.retranslateUi(download)

        QMetaObject.connectSlotsByName(download)
    # setupUi

    def retranslateUi(self, download):
        download.setWindowTitle(QCoreApplication.translate("download", u"Form", None))
        self.Minecraft.setText(QCoreApplication.translate("download", u"Minecraft", None))
        self.BodyLabel.setText(QCoreApplication.translate("download", u"\u8d44\u6e90", None))
        self.AutoInstall.setText(QCoreApplication.translate("download", u"\u81ea\u52a8\u5b89\u88c5", None))
        self.Pack.setText(QCoreApplication.translate("download", u"\u6574\u5408\u5305", None))
        self.Mod.setText(QCoreApplication.translate("download", u"Mod", None))
    # retranslateUi

