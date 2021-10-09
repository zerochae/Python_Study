import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication

form_class = uic.loadUiType("mygui04.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self):
        a = int(self.leA.text())
        b = int(self.leB.text())
        c = int(self.leC.text())
        sum = 0
        
        for i in range(a,b+1):
            if i % c == 0 :
                sum += i
        self.leD.setText(str(sum))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()