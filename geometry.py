import vector




class Geometry:
    pos =  None
    vel =  None
    size=  None

    def __init__(self,pos,size,vel = vector.Vector(0,0)):
        self.isVector(pos)
        self.isVector(vel)
        self.isInt(size)
        self.pos = pos
        self.size= size
        self.vel = vel
    @staticmethod
    def isVector(value):
        propType = type(vector.Vector(0,0))
        if type(value) != propType:
            raise TypeError(f"{value} is type {type(value)} when it should be type {propType}")
    @staticmethod
    def isInt(value):
        propType = type(1)
        if type(value) != propType:
            raise TypeError(f"{value} is type {type(value)} when it should be type {propType}")
    def changePos(self,pos):
        self.isVector(pos)
        self.pos = pos
    def changeSize(self,size):
        self.isInt(size)
        self.size = size
    def changeVel(self,vel):
        self.isVector(vel)
        self.vel = vel
    def calculateVel(self,adjustVal,dt):
        self.vel = self.vel.sum(adjustVal.mult(dt))
    def calculatePos(self,dt):
        self.pos = self.pos.sum(self.vel.mult(dt))
