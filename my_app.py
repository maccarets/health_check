from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *
#srlgmdd;lrfmgekgmrveklmrgfvksletrbgv
       
class MainWin(QWidget):
    def __init__(self):
        ''' вікно, в якому розташовується привітання '''
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        ''' створює графічні елементи '''
        # TODO self.hello_text = створити напис
        # TODO self.instruction = створити напис
        # TODO self.button = створити кнопку
        # TODO self.layout = створити лейаут

        # приклад як додавати віджети self.layout.addWidget(self.hello_text)

        # TODO добавить виджет self.hello_text на self.layout
        # TODO добавить виджет self.instruction на self.layout
        # TODO добавить виджет self.button на self.layout

    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
        self.setWindowTitle(txt_title)
        # TODO вствановити розмір вікна в pyqt
        # TODO вствановити місце де вікно зявлятиметься в pyqt



app = QApplication([])
mw = MainWin()
app.exec_()
