import sys

from PyQt5 import uic, QtGui, QtCore, QtWidgets  
from PyQt5.Qt import QPushButton, QMessageBox, QApplication, QMainWindow

form_class = uic.loadUiType("./myomok04.ui")[0]

 
class WindowClass(QMainWindow, form_class): 

    def __init__(self): 
        super().__init__() 
        self.flag_Bw = True 
        self.flag_Over = False
        
        self.arr2D = [[0 for i in range(19)] for j in range(19)] 
        self.pb2D = []
        self.setupUi(self) 
        for i in range(19):
            line = []
            for j in range(19):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40, 40))
                btn.setGeometry(QtCore.QRect(40 * j, 40 * i, 40, 40))
                btn.setToolTip("{},{}".format(i, j))
                btn.clicked.connect(self.btnClick)
                line.append(btn)
            self.pb2D.append(line)
            
        self.pb.clicked.connect(self.myReset)
        self.myrender()
        
    def myReset(self):
        self.flag_Over = False
        self.flag_Bw = True
        for i in range(19) :
            for j in range(19) :
                self.arr2D[i][j] = 0
        
        self.myrender()
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))
                elif self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))

    def btnClick(self):
        
        if self.flag_Over :
            return
        
        i = int(self.sender().toolTip().split(",")[0])
        j = int(self.sender().toolTip().split(",")[1])
        
        if self.arr2D[i][j] != 0:
            return
        
        stone = -1
        
        if self.flag_Bw:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        
        self.myrender()
        
        up = self.checkUp(i, j, stone)
        dw = self.checkDown(i, j, stone)
        right = self.checkRight(i, j, stone)
        left = self.checkLeft(i, j, stone)
        UR = self.checkUR(i, j, stone)
        UL = self.checkUL(i, j, stone)
        DR = self.checkDR(i, j, stone)
        DL = self.checkDL(i, j, stone)
        
        turn = ""
        
        if (self.flag_Bw):
            turn = "white"
        else:
            turn = "black"
        
        print(turn, "의 차례")
        print("up", up)
        print("down", dw)
        print("right", right)
        print("left", left)
        print("UR", UR)
        print("UL", UL)
        print("DR", DR)
        print("DL", DL)
        
        if up + dw + 1 == 5 or right + left + 1 == 5 or UR + DL + 1 == 5 or UL + DR + 1 == 5:
            QMessageBox.about(self,"result",turn + " win")
            self.flag_Over = True
        
        self.flag_Bw = not self.flag_Bw
        
    def checkUp(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                i -= 1
                if i < 0: return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkDown(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                i += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkRight(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                j += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkLeft(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                j -= 1
                if j < 0: return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkUR(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                i -= 1
                j += 1
                if i < 0: 
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkUL(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                i -= 1
                j -= 1
                if j < 0 or i < 0: 
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkDR(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                i += 1
                j += 1
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def checkDL(self, i, j, stone):
        cnt = 0
        try: 
            while True:
                i += 1
                j -= 1
                if j < 0: return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
