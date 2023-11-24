from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QVBoxLayout, QStackedWidget
from app.ui.Ui_main import Ui_Zunkin
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)
from qfluentwidgets import (BodyLabel, LineEdit, PushButton, SplitFluentWindow, FluentIcon)
from app.common.start import Start
from app.common.download import Download
from app.common.settings import Settings
from app.common.verset import Verset
from PIL import Image, ImageQt


DATA_LIST = \
{
    'title_icon_pic' : './app/data/zunkin.png'
}


class Main(SplitFluentWindow, Ui_Zunkin):

    def __init__(self):
        

        
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Zunkin - A simple minecraft launcher')
        self.setWindowIcon(QIcon(DATA_LIST['title_icon_pic']))


        self.start = Start(self)
        self.download = Download(self)
        self.settings = Settings(self)
        self.verset = Verset(self)

        self.addSubInterface(self.start, FluentIcon.HOME, '启动游戏')
        self.addSubInterface(self.download, FluentIcon.DOWNLOAD, '下载')
        self.addSubInterface(self.settings, FluentIcon.SETTING, '设置')
        self.addSubInterface(self.verset, '', '')

        self.switchTo(self.verset)

        
        



        




if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
