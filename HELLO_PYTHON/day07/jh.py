import sys

from PyQt5 import uic, QtCore, QtGui
from PyQt5.Qt import QMainWindow, QApplication, QPushButton

form_class = uic.loadUiType("myomok03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flagWb = True
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,]
        ] # 얘를 렌더링하기 (이대로 화면에 보여주기)
        self.pb2D = []
        self.setupUi(self)
        
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QtCore.QSize(40, 40))
                btn.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                btn.setToolTip("{},{}".format(i, j))
                btn.clicked.connect(self.myBtnClick)
                line.append(btn) # 10개씩 들어감
            self.pb2D.append(line) # 1줄씩 들어감
            
        self.pb.clicked.connect(self.myPbClick)
        self.myRender()
        
    def myRender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                else:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
        
    def myBtnClick(self):
        a = int(self.sender().toolTip().split(',')[0])
        b = int(self.sender().toolTip().split(',')[1])
        
        stone = -1
        
        if self.arr2D[a][b] == 0:
            if self.flagWb:
                self.arr2D[a][b] = 1
                stone = 1
            else:
                self.arr2D[a][b] = 2
                stone = 2
            
        up = self.checkUP(a, b, stone)
        dw = self.checkDW(a, b, stone)
        ri = self.checkRI(a, b, stone)
        le = self.checkLE(a, b, stone)
        print("up", up)
        print("down", dw)
        print("right", ri)
        print("left", le, "\n")
        
        self.myRender()
        self.flagWb = not self.flagWb
        
    def checkUP(self, a, b, stone): # 파라미터는 3개
        cnt = 0
        try:
            while True:
                a += -1
                # if a < 0:
                #     return cnt
                if self.arr2D[a][b] == stone:
                    cnt += 1
                else:
                    return cnt
        except: # 지금은 IndexError
            return cnt
            
    def checkDW(self, a, b, stone):
        cnt = 0
        try:
            while True:
                a += 1
                # if a < 0:
                #     return cnt
                if self.arr2D[a][b] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRI(self, a, b, stone):
        cnt = 0
        try:
            while True:
                b += 1
                # if b < 0:
                #     return cnt
                if self.arr2D[a][b] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLE(self, a, b, stone):
        cnt = 0
        try:
            while True:
                b += -1
                # if b < 0:
                #     return cnt
                if self.arr2D[a][b] == stone:
                    cnt += 1
                else:
                    return cnt
        except: # 지금은 IndexError
            return cnt
            
    def myPbClick(self):
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv) # QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = MyWindow()
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 작동시키는 코드