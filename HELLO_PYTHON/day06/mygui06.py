import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import random

form_class = uic.loadUiType("mygui06.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self):
       
        num = random.random()
        print(num)
        com = ""
        if num > 0.5 : 
            print(num)
            com = "홀"
        else : 
            print(num)
            com = "짝"
            
        mine = self.leMine.text()
        self.leCom.setText(com)
        result = ""
        
        if mine == com : 
            result = "이김"
        else : 
            result = "졌다"
            
        self.leResult.setText(result)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()