import matplotlib.pyplot as plt
import numpy as np
import random

class Dice():
    '''class of dice rolled'''
    def __init__(self,n):
        self.max = n
        self.value = 0
        self.corner = "tr"

    def roll(self):
        self.value = random.randint(1,(self.max+1))
        return self.value

    def cornerl(self):
        self.value = random.randint(1,(self.max+1))
        if self.value == 1 or self.value == 2:
            self.corner = "top"
        elif self.value == 3 or self.value == 4:
            self.corner = "left"
        elif self.value == 5 or self.value == 6:
            self.corner = "right"
        return self.corner

class mainPoint():
    '''class of main point'''
    def __init__(self):
        self.x = random.randint(0,1001)
        self.y = random.randint(0,1001)
        self.val = self.x + self.y
        while self.val > 1000:
            self.x = random.randint(0,1001)
            self.y = random.randint(0,1001)
            self.val = self.x + self.y

    def pointx(self):
        return self.x

    def pointy(self):
        return self.y

    def move(self,corner):
        if corner == "top":
            distx = 0 - self.x
            halfx = distx / 2
            self.x = self.x + halfx
            disty = 1000 - self.y
            halfy = disty / 2
            self.y = self.y + halfy
        elif corner == "right":
            distx = 1000 - self.x
            halfx = distx / 2
            self.x = self.x + halfx
            disty = 0 - self.y
            halfy = disty / 2
            self.y = self.y + halfy
        elif corner == "left":
            distx = 0 - self.x
            halfx = distx / 2
            self.x = self.x + halfx
            disty = 0 - self.y
            halfy = disty / 2
            self.y = self.y + halfy

    def printPoints(self):
        return str(self.x),str(self.y)
            

xlm = [0,0,1000]
ylm = [0,1000,0]

plt.ion()
plt.plot(xlm,ylm,'ro')

dice = Dice(6)

mp = mainPoint()

plt.plot(mp.pointx(),mp.pointy(),'k.')

for a in range(1000000000):
    corner = dice.cornerl()
    mp.move(corner)
    plt.plot(mp.pointx(),mp.pointy(),'k.')
    plt.pause(0.00000000000000000000000000000000000000000000000000000001)



    
##    plt.clf()

##plt.plot(x,y,'k.')
##plt.draw()
##plt.pause(1)
##plt.clf()
##
##x.append(4)
##y.append(2)
##
##plt.plot(x,y,'k.')
##plt.draw()
