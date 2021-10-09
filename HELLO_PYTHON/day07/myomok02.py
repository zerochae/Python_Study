import sys

from PyQt5 import uic, QtGui, QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton


form_class = uic.loadUiType("./myomok02.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
        
        for i in range(24) :
            for j in range(24) :
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(40 * i,40 * j,40,40))
        
    def btnClick(self):
        
        pass
         
        # if(self.state == 0) :
        #     self.state = 1
        #
        # elif(self.state == 1) :
        #     self.state = 2
        #
        # elif(self.state == 2) :
        #     self.state = 0
        #
        # self.pb.setIcon(QtGui.QIcon("{}.png".format(self.state)))
        #

        
        
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()