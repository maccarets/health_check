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
        index_text = QLabel("Index Label", self)
        result_text = QLabel("Result Label", self)
        btn = QPushButton("Knopka", self)

        vbox = QVBoxLayout()
        vbox.addWidget(index_text)
        vbox.addWidget(result_text)
        vbox.addWidget(btn)

        self.setLayout(vbox)

    def set_appear(self):
        self.setWindowTitle('Test Window')
        self.setGeometry(0, 0, 240, 120)

app = QApplication([])
window = FinalWin()
app.exec()
