import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *


class MyWidget(QMainWindow):
    """ главное окно"""

    def __init__(self):
        super().__init__()
        uic.loadUi('try menu.ui', self)

        self.play_btn.clicked.connect(lambda: self.num(1))
        self.again_btn.clicked.connect(lambda: self.num(2))
        self.info_btn.clicked.connect(lambda: self.num(0))

    def num(self, k):
        self.lcdNumber.display(k)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
