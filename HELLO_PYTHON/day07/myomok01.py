import sys

from PyQt5 import uic, QtGui, QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("./myomok01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.state = 0
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        
        if(self.state == 0) :
            self.state = 1
        
        elif(self.state == 1) :
            self.state = 2
        
        elif(self.state == 2) :
            self.state = 0
        
        self.pb.setIcon(QtGui.QIcon("{}.png".format(self.state)))
        
        
        
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()