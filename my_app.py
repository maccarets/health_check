from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

       
class MainWin(QWidget):
    def __init__(self):
        ''' вікно, в якому розташовується привітання '''
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        ''' створює графічні елементи '''

    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''


app = QApplication([])
mw = MainWin()
app.exec_()
