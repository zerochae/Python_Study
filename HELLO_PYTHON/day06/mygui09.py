import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
from PyQt5.uic.Compiler.qtproxies import QtWidgets

form_class = uic.loadUiType("mygui09.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(self.pbFunction)
        self.pb1.clicked.connect(self.pbFunction)
        self.pb2.clicked.connect(self.pbFunction)
        self.pb3.clicked.connect(self.pbFunction)
        self.pb4.clicked.connect(self.pbFunction)
        self.pb5.clicked.connect(self.pbFunction)
        self.pb6.clicked.connect(self.pbFunction)
        self.pb7.clicked.connect(self.pbFunction)
        self.pb8.clicked.connect(self.pbFunction)
        self.pb9.clicked.connect(self.pbFunction)
        self.pbCall.clicked.connect(self.pbCallFunction)
        
    def pbFunction(self):
        str_old = self.le.text()
        str_new = self.sender().text()
        self.le.setText(str_old+str_new)
    
    def pbCallFunction(self):
        self.QtWidgets.QMessageBox.about(self,"calling",self.le.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()