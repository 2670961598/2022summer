from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal



class Road(QLabel):

    mylabelSig = pyqtSignal(str)
    mylabelDoubleClickSig = pyqtSignal(str)

    def __init__(self , parent):
        super().__init__(parent)
        self.x = 0
        self.y = 0

    def __init__(self, parent ,x , y):
        super().__init__(parent)
        self.x = x
        self.y = y

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        print("鼠标抬起事件", self.x, self.y)


    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动事件", self.x, self.y)

    def mouseDoubleClickEvent(self, e):  # 双击
        print("双击事件", self.x, self.y , self.objectName() ,e)
        sigContent = self.objectName()
        self.mylabelDoubleClickSig.emit(sigContent)

    def mousePressEvent(self, e):  # 单击
        print("单击事件" , self.x, self.y)
        # self.setStyleSheet("QLabel{background-color: #"
        #                    + str(random.randint(0, 255))
        #                    + str(random.randint(0, 255))
        #                    + str(random.randint(0, 255)) + ";}")
        sigContent = self.objectName()
        self.mylabelSig.emit(sigContent)


    def leaveEvent(self, e):  # 鼠标离开label
        # self.setStyleSheet("QLabel{background-color: #"
        #                                  + str(hex(random.randint(0, 255))[2:].upper())
        #                                  + str(hex(random.randint(0, 255))[2:].upper())
        #                                  + str(hex(random.randint(0, 255))[2:].upper()) + ";}")
        print("鼠标离开事件" , self.x, self.y)

    def enterEvent(self, e):  # 鼠标移入label
        # self.setStyleSheet("QLabel{background-color: #"
        #                                  + str(hex(random.randint(0, 255))[2:].upper())
        #                                  + str(hex(random.randint(0, 255))[2:].upper())
        #                                  + str(hex(random.randint(0, 255))[2:].upper()) + ";}")
        print("鼠标进入事件", self.x, self.y)