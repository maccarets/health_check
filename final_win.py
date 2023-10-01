from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *

class FinalWin(QWidget):
    ''' вікно, в якому проводиться опитування '''
    def __init__(self):
        
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()
    
    def initUI(self):
       ''' створює графічні елементи '''
       

    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
