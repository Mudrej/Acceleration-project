# -*- coding: cp1251 -*-

import sys
from typing import Container
import PyQt6.QtWidgets as qw
import PyQt6.QtCore as qc
import excel_processing

class MainWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Средняя зарплата в районах Рязанской области")
        self.resize(500,200)

        self.label = qw.QLabel("Укажите путь к файлу с опросом")

        self.lineEdit = qw.QLineEdit()
        self.lineEdit.setFixedSize(200,20) 

        self.button = qw.QPushButton("Далее")
        self.button.setFixedSize(70,20)
        self.button.clicked.connect(self.pressing_button)

        layout = qw.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)
        
        container = qw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def pressing_button(self):
        excel_processing.data_preparation(self.lineEdit.displayText())

app = qw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()