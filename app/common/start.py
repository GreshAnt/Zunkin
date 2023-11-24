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
from ..ui.Ui_start import Ui_Form
from PIL import Image, ImageQt
import os
# from ....Zunkin.main import Main

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
DATA_LIST = \
{
    'background' : f'{parent_dir}/data/bg.png'
}

class Start(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.img = Image.open(DATA_LIST['background'])
        self.label.setPixmap(ImageQt.toqpixmap(self.img))

        # self.VerSet.clicked.connect()

        # self.VerSet.clicked.connect(self.vertion_contrl)


