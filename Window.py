from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget , QApplication  , QPushButton  , QDesktopWidget
from PyQt5.QtGui import QIcon
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
        self.setWindowTitle("Cleaner Robots'behavior Display")
        self.setWindowIcon(QIcon('./Image/Icon.png'))


        #paint the road
        self.baseRoad = Map(self.width , self.height)
        self.baseRoad.setParent(self)
        #self.baseRoad.move(0, 0)
        self.baseRoad.resize(self.height*0.8, self.height*0.8)
        #Qt.setAlignment(Qt.AlignCenter)
        self.baseRoad.setText("This is the Map\n"
                              "You need to Create a Map that you want to use \n "
                              "Then press the Create button to show your Map")
        self.baseRoad.setStyleSheet("QLabel{font-size: 32px;font-weight: bold}")
        self.baseRoad.setAlignment(Qt.AlignCenter)

        # self.baseRoad.setStyleSheet("QLabel{background-color: #ff0000;}")
        #The button to start the program
        self.startButton = QPushButton('Start')
        self.startButton.setParent(self)
        self.startButton.move(self.width*0.475, self.height*0.65)
        self.startButton.resize(self.width*0.1, self.height*0.1)
        #self.startButton.setStyleSheet("QPushButton{background-color: #ff0000;}")

        self.paintButton = QPushButton('Paint')
        self.paintButton.setParent(self)
        self.paintButton.move(self.width*0.475, self.height*0.35)
        self.paintButton.resize(self.width*0.1, self.height*0.1)

        self.center()
        self.show()

    #center the window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def connectAction(self):
        self.paintButton.clicked.connect(self.paintMap)

    def paintMap(self):
        self.baseRoad.setText("")
        self.baseRoad.paintFirstMap(self.baseRoad.data)
        self.paintButton.clicked.disconnect(self.paintMap)
        self.paintButton.clicked.connect(self.test)

    def test(self):
        print(1)
