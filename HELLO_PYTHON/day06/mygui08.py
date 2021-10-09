import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import random

form_class = uic.loadUiType("mygui08.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self):
       
        comArr = ["가위" , "바위" , "보"]
        com = random.choice(comArr)
        self.leCom.setText(com)
            
        mine = self.leMine.text()
        result = ""
        
        if mine == com : 
            result = "비김"
        elif (mine=="가위" and com =="바위") or (mine=="바위" and com =="보") or (mine=="보" and com =="가위") : 
            result = "졌다"
        else :
            result = "이겼다"
            
        self.leResult.setText(result)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()