from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QVBoxLayout
from ..ui.Ui_main import Ui_Zunkin
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)
from qfluentwidgets import (BodyLabel, LineEdit, PushButton, SplitFluentWindow)
from ..ui.Ui_download import Ui_download
from PIL import Image, ImageQt

class Download(QWidget, Ui_download):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        # self.AutoInstall.isChecked.connect(self.set_no_check(self.AutoInstall))
        # self.Mod.isChecked.connect(self.set_no_check(self.Mod))
        # self.Pack.isChecked.connect(self.set_no_check(self.PAck))
    # def set_no_check(self, org):
    #     self.AutoInstall.setChecked == False
    #     self.Mod.setChecked == False
    #     self.Pack.setChecked == False
    #     org == True