from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        ''' вікно, в якому проводиться опитування '''
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()
    
    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''

    def initUI(self):
        ''' створює графічні елементи '''
    
    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
        self.setWindowTitle(txt_title)
        # TODO вствановити розмір вікна в pyqt
        # TODO вствановити місце де вікно зявлятиметься в pyqt
