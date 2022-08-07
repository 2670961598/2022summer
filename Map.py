from Road import *
import numpy as np


class Map(QLabel):

    crossRoad = './Image/CrossRoad.png'
    crossRoadDown = './Image/CrossRoadDown.png'
    crossRoadLeft = './Image/CrossRoadLeft.png'
    crossRoadRight = './Image/CrossRoadRight.png'
    crossRoadUp = './Image/CrossRoadUp.png'
    leftAndRight = './Image/LeftAndRight.png'
    upAndDown = './Image/UpAndDown.png'

    def __init__(self):
        super().__init__()
        self.baseMap = None
        self.paintFirstMap(10)
        self.initUI()

    def __init__(self,  width , height):
        super().__init__()
        self.width = width
        self.height = height
        self.baseMap = None
        self.data = read_file("data.xlsx",method="Excel")

    def paintFirstMap(self ,*args):

        '''
        This function is mainly for painting the map
        accept the data from the file and paint the map by the data from the file
        '''

        '''
        I think that the following code has the better performance than the following code but I am a lazy person
        So, If you have a lot of time, you can try to change the code
        '''

        self.baseTuple = np.array(args[0])
        print(self.baseTuple)
        if self.baseTuple.shape[0] > self.baseTuple.shape[1]:
            long = self.baseTuple.shape[0]
            short = self.baseTuple.shape[1]
            mid = 0
        elif self.baseTuple.shape[0] == self.baseTuple.shape[1]:
            long = self.baseTuple.shape[0]
            short = self.baseTuple.shape[1]
            mid = 2
        else:
            long = self.baseTuple.shape[1]
            short = self.baseTuple.shape[0]
            mid = 1

        print(self.baseTuple.shape[0], self.baseTuple.shape[1])
        self.baseMap = [ [Road(self ,i , j) for i in range(self.baseTuple.shape[1])] for j in range(self.baseTuple.shape[0]) ]

        for j in range(self.baseTuple.shape[0]):
            for i in range(self.baseTuple.shape[1]):
                self.paintRoad(j , i , self.baseTuple[j][i] ,mid , long , short)
                if self.baseTuple[j][i] == 1:
                    network.add_node((j,i))

        for j in range(self.baseTuple.shape[0]):
            for i in range(self.baseTuple.shape[1]):
                if self.baseTuple[j][i] == 1:
                    if j - 1 >= 0 and self.baseTuple[j - 1][i] == 1:
                        network.add_edge((j,i),(j - 1,i))
                    if j + 1 < self.baseTuple.shape[0] and self.baseTuple[j + 1][i] == 1:
                        network.add_edge((j,i),(j + 1,i))
                    if i - 1 >= 0 and self.baseTuple[j][i - 1] == 1:
                        network.add_edge((j,i),(j,i - 1))
                    if i + 1 < self.baseTuple.shape[1] and self.baseTuple[j][i + 1] == 1:
                        network.add_edge((j,i),(j,i + 1))




    def paintRoad(self , j , i , category , mid , long , short):
        if category == 1 and j - 1 >= 0 and i - 1 >= 0 and j + 1 < self.baseTuple.shape[0] and i + 1 < self.baseTuple.shape[1]:
            if self.baseTuple[j - 1][i] == 1:
                if self.baseTuple[j][i - 1] == 1:
                    if self.baseTuple[j + 1][i] == 1:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoad + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadLeft + ");}")
                    else:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadUp + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.upAndDown + ");}")
                else:
                    if self.baseTuple[j + 1][i] == 1:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadRight + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.upAndDown + ");}")
                    else:
                        if i + 1 < self.baseTuple.shape[1] and self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.leftAndRight + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadDown + ");}")
            else:
                if self.baseTuple[j][i - 1] == 1:
                    if self.baseTuple[j + 1][i] == 1:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadDown + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.leftAndRight + ");}")
                    else:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.leftAndRight + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadDown + ");}")
                else:
                    if self.baseTuple[j + 1][i] == 1:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.leftAndRight + ");}")
                        else:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadUp + ");}")
                    else:
                        if self.baseTuple[j][i + 1] == 1:
                            self.baseMap[j][i].setStyleSheet("QLabel{border-image: url(" + self.crossRoadLeft + ");}")

        if mid == 0:
            self.baseMap[j][i].move((i + (long - short) / 2) * self.height * (0.8 / long),
                                    j * self.height * (0.8 / long))
            self.baseMap[j][i].resize(self.height * (0.8 / long), self.height * (0.8 / long))
            self.baseMap[j][i].show()
        elif mid == 1:
            self.baseMap[j][i].move(i * self.height * (0.8 / long),
                                    + (j + (long - short) / 2) * self.height * (0.8 / long))
            self.baseMap[j][i].resize(self.height * (0.8 / long), self.height * (0.8 / long))
            self.baseMap[j][i].show()
        elif mid == 2:
            self.baseMap[j][i].move(i * self.height * (0.8 / long), + j * self.height * (0.8 / long))
            self.baseMap[j][i].resize(self.height * (0.8 / long), self.height * (0.8 / long))
            self.baseMap[j][i].show()