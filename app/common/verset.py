from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QVBoxLayout, QStackedWidget
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
from ..ui.Ui_verset import Ui_Form_VerSet
from PIL import Image, ImageQt
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

class Verset(QWidget, Ui_Form_VerSet):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


        # self.VerSet.clicked.connect(self.vertion_contrl)


