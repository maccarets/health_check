from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *
#edited
class FinalWin(QWidget):
    ''' вікно, в якому проводиться опитування '''
    def __init__(self):
        
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()
    
    def initUI(self):
       ''' створює графічні елементи '''
       # TODO self.index_text = створити напис
       # TODO self.result_text = створити напис

        # TODO свтворити вертикальний лайоут і додати на нього створенні віджети
       

    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
        self.setWindowTitle(txt_title)
        # TODO вствановити розмір вікна в pyqt
        # TODO вствановити місце де вікно зявлятиметься в pyqt

