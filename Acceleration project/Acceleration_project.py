# -*- coding: cp1251 -*-

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import excel_processing
import hist_processing


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 440)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(570, 440))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.WShow = QtWidgets.QWidget(self.centralwidget)
        self.WShow.setGeometry(QtCore.QRect(0, 0, 16777215, 16777215))
        self.WShow.setObjectName("WShow")

        self.textEdit = QtWidgets.QTextEdit(self.WShow)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 16777215, 16777215))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.WOpen = QtWidgets.QWidget(self.centralwidget)
        self.WOpen.setGeometry(QtCore.QRect(0, 0, 16777215, 16777215))
        self.WOpen.setObjectName("WOpen")

        self.label = QtWidgets.QLabel(self.WOpen)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 100, 191, 21))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.WOpen)
        self.pushButton.setGeometry(QtCore.QRect(240, 210, 65, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)

        self.lineEdit = QtWidgets.QLineEdit(self.WOpen)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 291, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.toolButton = QtWidgets.QToolButton(self.WOpen)
        self.toolButton.setGeometry(QtCore.QRect(510, 100, 23, 19))
        self.toolButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.open_dialog)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 560, 17))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)

        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.file = QtWidgets.QMenu(self.menuBar)

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)

        self.file.setFont(font)
        self.file.setObjectName("file")
        self.hist = QtWidgets.QMenu(self.menuBar)
        self.hist.setEnabled(False)
        self.hist.setGeometry(QtCore.QRect(399, 109, 146, 36))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)

        self.hist.setFont(font)
        self.hist.setObjectName("hist")

        self.show = QtGui.QAction(MainWindow)
        self.show.setObjectName("show")
        self.show.triggered.connect(self.hist_visible)

        self.hist.addAction(self.show)

        MainWindow.setMenuBar(self.menuBar)

        self.action_Excel = QtGui.QAction(MainWindow)

        font = QtGui.QFont()
        font.setKerning(True)

        self.action_Excel.setFont(font)
        self.action_Excel.setAutoRepeat(False)
        self.action_Excel.setObjectName("action_Excel")
        self.action_Excel.triggered.connect(self.open_excel)

        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(self.open)

        self.save = QtGui.QAction(MainWindow)
        self.save.setEnabled(False)
        self.save.setVisible(True)
        self.save.setObjectName("save")
        self.save.triggered.connect(self.save_dialog)

        #self.saveas = QtGui.QAction(MainWindow)
        #self.saveas.setEnabled(False)
        #self.saveas.setVisible(True)
        #self.saveas.setObjectName("saveas")
        #self.saveas.triggered.connect(self.saveas_dialog)

        self.file.addAction(self.action_Excel)
        self.file.addAction(self.action)
        self.file.addSeparator()
        self.file.addAction(self.save)
        #self.file.addAction(self.saveas)

        self.menuBar.addAction(self.file.menuAction())
        self.menuBar.addAction(self.hist.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        data = dict()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Средняя зарплата в районах Рязанской области"))
        self.label.setText(_translate("MainWindow", "Укажите путь к файлу с опросом"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.file.setTitle(_translate("MainWindow", "Файл"))
        self.hist.setTitle(_translate("MainWindow", "Гистограмма"))
        self.action_Excel.setText(_translate("MainWindow", "Импорт из Excel"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        #self.saveas.setText(_translate("MainWindow", "Сохранить как"))
        self.show.setText(_translate("MainWindow", "Отобразить гистограмму"))

    def calculate(self):
        self.data = excel_processing.data_preparation(self.lineEdit.displayText())
        hist_processing.hist(self.data)
        self.hist.setEnabled(True)
        self.WOpen.setVisible(False)
        self.WShow.setVisible(True)
        self.textEdit.clear()
        for i in self.data:
            self.textEdit.append(f'{i}: опрошено {self.data[i][1]}, средняя зарплата {self.data[i][0]}')
        self.save.setEnabled(True)

    def hist_visible(self):
        hist_processing.hist(self.data)

    def open_dialog(self):
        path = QFileDialog.getOpenFileName(parent = None, caption = 'Open file', directory = None, filter = "Excel File (*.xlsx)")[0]
        self.lineEdit.setText(path)

    def open_excel(self):
        path = QFileDialog.getOpenFileName(parent = None, caption = 'Open file', directory = None, filter = "Excel File (*.xlsx)")[0]
        self.data = excel_processing.data_preparation(path)
        hist_processing.hist(self.data)
        self.hist.setEnabled(True)
        self.WOpen.setVisible(False)
        self.textEdit.clear()
        for i in self.data:
            self.textEdit.append(f'{i}: опрошено {self.data[i][1]} человек, средняя зарплата {self.data[i][0]} рублей')
        self.save.setEnabled(True)

    def open(self):
        self.WShow.setVisible(False)
        self.WOpen.setVisible(True)
        path = QFileDialog.getOpenFileName(parent = None, caption = 'Open file', directory = None, filter = "Excel File (*.xlsx)")[0]
        self.lineEdit.setText(path)

    def save_dialog(self):
        path = QFileDialog.getSaveFileName(parent = None, caption = 'Open file', directory = None, filter = "Text File (*.txt)")[0]
        with open(path,'w') as file:
            file.write(str(self.data).replace(",","\n").replace("'","").replace("{"," ").replace("}",""))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
