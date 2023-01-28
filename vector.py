

class Vector:

    x       = 0.0
    y       = 0.0

    def __init__(self,x,y):
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
