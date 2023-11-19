from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QVBoxLayout
from Ui_main import Ui_Zunkin
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)
from qfluentwidgets import (BodyLabel, LineEdit, PushButton, SplitFluentWindow)
from Ui_start import Ui_Form
from PIL import Image, ImageQt

class Start(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.img = Image.open('./data/bg.png')
        self.label.setPixmap(ImageQt.toqpixmap(self.img))

