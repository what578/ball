import math

class Vector:

    x       = 0.0
    y       = 0.0

    def __init__(self,x,y =None):
        if y == None:
            self.x      = x
            self.y      = x
        else:
            self.x      = x
            self.y      = y

    def setX(self,num):
        self.x = num
    def setY(self,num):
        self.y = num
    def sum(self,vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    def sub(self,vector):
        return Vector(self.x - vector.x, self.y - vector.y)
    def mult(self,vector):
        return Vector(self.x * vector.x,self.y * vector.y)
    def floor(self):
        self.x = math.floor(self.x)
        self.y = math.floor(self.y)
    def ceil(self):
        self.x = math.ceil(self.x)
        self.y = math.ceil(self.y)
        
