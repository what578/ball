import vector
import colorama
import time
import msvcrt
import math
import geometry
#import curses



HEIGHT,WIDTH = 32,64
display      = [None]  * (HEIGHT*WIDTH)
FPS          = 10
DT           = 1/FPS
GRAVITY      = 5
WALLDAMPER   = -1.0


class Display:
    fps         = None
    #store as vector
    dt          = None
    height      = None
    width       = None
    #
    display     = None
    #dictionary of environment variable
    environmentVariable = None
    geometry    = []

    def __init__(self,fps,height,width,dt,environmentVariable = {},geometry = [] ):
        colorama.init()
        self.fps        = fps
        self.height     = height
        self.width      = width
        self.display    = [None] *(height*width)
        self.dt         = dt
        self.environmentVariable = environmentVariable
        self.geometry   = geometry
    def fill(self):
        filler = " "
        try:
            filler = self.environmentVariable["filler"]
        except:
            print("")

        for row in range(self.height):
            for column in range(self.width):
                self.display[row*self.width + column] = filler
    def renderGeom(self,geom):
        geom.render(self.display,self.height,self.width)

    def moveCursor(self):
        print("\033[H")
        #print("\033[%dA;%dD" % (0,0))
        #print("\033[%d;%dH" % (self.height, self.width))



    def show(self):
        startRow,endRow = 0,self.width
        for row in range(self.height):
            print("".join(self.display[startRow:endRow]))
            startRow += self.width
            endRow   += self.width
    def run(self):
        quit = False
        while not quit:
            self.fill()
            self.moveCursor()
            self.renderGeom(self.geometry[0])
            self.show()
            time.sleep(1/self.fps)

    def wallCollision(self,geom):
        return
    def leftWallColl(self,geom):
        return
    def righWallColl(self,geom):
        return
    def topWallColl(self,geom):
        return
    def botWallColl(self,geom):
        wallResponse = None
        try:
            wallResponse = self.environmentVariable["wallDamper"]
        except:
            wallResponse = 1.0
        if geom.y > self.height - geom.size:
            geom.y = self.height - geom.size
            geom.vel.y *= wallResponse
        return


#------------
#---HHH------
#---HCH------
#---HHH-----
#------------
#size = 1
#center = (2,2)
#topLeft= (1,1)
#bottomR= (3,3)

#vector1= (3,3)
#vector2= (1,1)

#size   = 2
#center = (2,2)
#vector1= (0,0)
#vector2= (4,4)
#topLeft= ()
#bottomR= (4,)
#def box(center,size):
#    vector2 = center.sub(vector.Vector(size,size))
#    vector1 = center.sum(vector.Vector(size,size))
#    #print(f"center is {center.x} {center.y}")
#    #print(f"x for 1 and 2 ={vector1.x} {vector2.x} ")
#    #print(f"y for 1 and 2 ={vector1.y} {vector2.y}")
#    for x in range(vector1.x - vector2.x):
#        for y in range(vector1.y -vector2.y):
#            value = (x+vector2.x) + ((y+vector2.y)*WIDTH)
#            value1= x+vector2.x
#            value2= (y+vector2.y)*WIDTH
#            if 0 <= value and value <= HEIGHT*WIDTH:
#                display[value] = "Q"
#
def box(center,size):
    vector2 = center.sub(vector.Vector(size,size))
    vector1 = center.sum(vector.Vector(size,size))
    vector2.floor()
    vector1.ceil()
    x = vector2.x
    y = vector2.y
    while y <= vector1.y:
        while x <= vector1.x:
            if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
                display[y*WIDTH + x] = "Q"
            x += 1
        y += 1
        x = vector2.x





def fill(filler):
    for x in range(WIDTH*HEIGHT):
        display[x] =  filler

def dot():
    x = 31
    y = 31
    y*WIDTH + x
    display[y*WIDTH + x] = "*"
def moveCursor():
    print("\033[H")
    #print("\033[%d;%dH" % (x, y))

def show():
    startRow,endRow = 0,WIDTH
    for y in range(HEIGHT):
        print("".join(display[startRow:endRow]))
        startRow += WIDTH
        endRow   += WIDTH

if __name__ == "__main__":
    #def __init__(self,fps,height,width,dt,environmentVariable = None):
    environmentVariables = {
        "filler":"*",
        "gravity": 5,
        "wallDamper": -0.9
        }
#    def __init__(self,pos,size,vel = vector.Vector(0,0)):

    geometry = [geometry.Square(vector.Vector(5,5),2)]

    dis         =Display(10,32,32,vector.Vector(1/10,1/10),environmentVariables,geometry)
    dis.run()
    #colorama.init()
    #filler="*"
    #pos = vector.Vector(WIDTH/2,3)
    #size = 2

    #vel  = vector.Vector(5,5)
    #gravity = vector.Vector(0,GRAVITY)
    #dtV = vector.Vector(DT)
    #quit = False
    #while not quit:
    #    vel = vel.sum(gravity.mult(dtV))
    #    pos = pos.sum(vel.mult(dtV))

    #    if pos.y > HEIGHT - (size+1):
    #        pos.y = HEIGHT - (size+1)
    #        vel.y *= WALLDAMPER
    #    elif pos.y < 0 + size +1:
    #        pos.y = 0 + (size+1)
    #        vel.y *= WALLDAMPER
    #    if pos.x > WIDTH - (size+1):
    #        pos.x = WIDTH - (size+1)
    #        vel.x *= WALLDAMPER
    #    elif pos.x < 0 + size + 1:
    #        pos.x = 0 + (size +1)
    #        vel.x *= WALLDAMPER





    #    fill(filler)
    #    moveCursor()
    #    box(pos,size)
    #    show()
    #    time.sleep(1/FPS)
        #move(1,1)

    #while not quit:
    #    char = msvcrt.getch()
    #    if char == "q":
    #        quit = True
    #    print(char)
        #C = boxC.sum(vel)
        #box(boxC,size)
        #show()
        #time.sleep(1/FPS)
