from Road import *
from File import *
import numpy as np
import random

class Map(QLabel):

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
        self.data = read_file("data.csv",method="CSV")
        self.initUI()

    def initUI(self):
        pass
        # self.label = QLabel(self)
        # self.label.move(0, 0)
        # self.label.resize(self.height()*0.1, self.height()*0.1)
        # self.label.setStyleSheet("QLabel{background-color: #00ff00;}")

    def paintFirstMap(self ,*args):

        # self.baseMap = [ [Road(self ,i , j) for i in range(map)] for j in range(map) ]
        # for i in range(map):
        #     for j in range(map):
        #         self.baseMap[i][j].move(i*self.height*(0.8/map), j*self.height*(0.8/map))
        #         self.baseMap[i][j].resize(self.height*(0.8/map), self.height*(0.8/map))
        #         self.baseMap[i][j].setStyleSheet("QLabel{background-color: #"
        #                                  + str(hex(random.randint(0, 255))[2:].upper())
        #                                  + str(hex(random.randint(0, 255))[2:].upper())
        #                                  + str(hex(random.randint(0, 255))[2:].upper()) + ";}")\
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
        if mid == 0:
            for j in range(self.baseTuple.shape[0]):
                for i in range(self.baseTuple.shape[1]):
                    self.baseMap[j][i].move((i + (long - short) / 2)*self.height*(0.8/long), j*self.height*(0.8/long))
                    self.baseMap[j][i].resize(self.height*(0.8/long), self.height*(0.8/long))
                    self.baseMap[j][i].setStyleSheet("QLabel{background-color: #"
                                                     + str(hex(random.randint(0, 255))[2:].upper())
                                                     + str(hex(random.randint(0, 255))[2:].upper())
                                                     + str(hex(random.randint(0, 255))[2:].upper()) + ";}")
                    self.baseMap[j][i].show()
        elif mid == 1:
            for j in range(self.baseTuple.shape[0]):
                for i in range(self.baseTuple.shape[1]):
                    self.baseMap[j][i].move(i*self.height*(0.8/long),  + (j + (long - short) / 2)*self.height*(0.8/long))
                    self.baseMap[j][i].resize(self.height*(0.8/long), self.height*(0.8/long))
                    self.baseMap[j][i].setStyleSheet("QLabel{background-color: #"
                                                     + str(hex(random.randint(0, 255))[2:].upper())
                                                     + str(hex(random.randint(0, 255))[2:].upper())
                                                     + str(hex(random.randint(0, 255))[2:].upper()) + ";}")
                    self.baseMap[j][i].show()
        else:
            for j in range(self.baseTuple.shape[0]):
                for i in range(self.baseTuple.shape[1]):
                    self.baseMap[j][i].move(i*self.height*(0.8/long),  + j*self.height*(0.8/long))
                    self.baseMap[j][i].resize(self.height*(0.8/long), self.height*(0.8/long))
                    self.baseMap[j][i].setStyleSheet("QLabel{background-color: #"
                                                     + str(hex(random.randint(0, 255))[2:].upper())
                                                     + str(hex(random.randint(0, 255))[2:].upper())
                                                     + str(hex(random.randint(0, 255))[2:].upper()) + ";}")
                    self.baseMap[j][i].show()
