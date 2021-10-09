import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication

form_class = uic.loadUiType("mygui05.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self):
        num = int(self.leDan.text())
        result = ""
        for i in range(1,10):
            #result += str(num) + "*" + str(i) + "=" + str(num*i) +"\n\n"
            result += "{}*{}={}\n\n".format(num,i,num*i)
        self.te.setText(result)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()