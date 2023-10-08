from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        index_text = QLabel(txt_index,)
        result_text = QLabel(txt_workheart,)

        vbox = QVBoxLayout()
        vbox.addWidget(index_text,alignment=Qt.AlignCenter)
        vbox.addWidget(result_text,alignment=Qt.AlignCenter)


        self.setLayout(vbox)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
window = FinalWin()
app.exec()
