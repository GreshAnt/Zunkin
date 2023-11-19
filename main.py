from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QVBoxLayout, QStackedWidget
from Ui_main import Ui_Zunkin
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)
from qfluentwidgets import (BodyLabel, LineEdit, PushButton, SplitFluentWindow, FluentIcon)
from start import Start
from download import Download
from settings import Settings
from PIL import Image, ImageQt



class Main(SplitFluentWindow, Ui_Zunkin):

    def __init__(self):
        

        
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Zunkin - A simple minecraft launcher')
        self.setWindowIcon(QIcon('./data/zunkin.png'))


        self.start = Start(self)
        self.download = Download(self)
        self.settings = Settings(self)

        self.addSubInterface(self.start, FluentIcon.HOME, '启动游戏')
        self.addSubInterface(self.download, FluentIcon.DOWNLOAD, '下载')
        self.addSubInterface(self.settings, FluentIcon.SETTING, '设置')

        
        



        




if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
