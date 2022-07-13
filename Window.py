
from PyQt5.QtWidgets import QWidget , QApplication  , QPushButton  , QDesktopWidget
from Map import Map

#create a new windows by PyQt5
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connectAction()


    def initUI(self):
        #set the size of the window
        self.desktop = QApplication.desktop()
        self.width = self.desktop.width()
        self.height = self.desktop.height()
        self.setFixedSize(self.width*0.6, self.height*0.8)

        #paint the road
        self.baseRoad = Map(self.width , self.height)
        self.baseRoad.setParent(self)
        self.baseRoad.move(0, 0)
        self.baseRoad.resize(self.height*0.8, self.height*0.8)

        # self.baseRoad.setStyleSheet("QLabel{background-color: #ff0000;}")

        self.startButton = QPushButton('Start')
        self.startButton.setParent(self)
        self.startButton.move(self.width*0.475, self.height*0.65)
        self.startButton.resize(self.width*0.1, self.height*0.1)
        #self.startButton.setStyleSheet("QPushButton{background-color: #ff0000;}")

        self.setWindowTitle("Cleaner Robots'behavior Display")
        self.center()

        self.show()


    #center the window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def connectAction(self):
        self.startButton.clicked.connect(self.paintMap)

    def paintMap(self):
        self.baseRoad.paintFirstMap(self.baseRoad.data)
        self.startButton.clicked.disconnect(self.paintMap)
        self.startButton.clicked.connect(self.test)

    def test(self):
        print(1)