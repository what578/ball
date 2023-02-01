import vector
import colorama
import time
import msvcrt
import math
#import curses



HEIGHT,WIDTH = 32,64
display      = [None]  * (HEIGHT*WIDTH)
FPS          = 10
DT           = 1/FPS
GRAVITY      = 5
WALLDAMPER   = -1.0



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
    colorama.init()
    filler="*"
    pos = vector.Vector(WIDTH/2,3)
    size = 2

    vel  = vector.Vector(5,5)
    gravity = vector.Vector(0,GRAVITY)
    dtV = vector.Vector(DT)
    quit = False
    while not quit:
        vel = vel.sum(gravity.mult(dtV))
        pos = pos.sum(vel.mult(dtV))

        if pos.y > HEIGHT - (size+1):
            pos.y = HEIGHT - (size+1)
            vel.y *= WALLDAMPER
        elif pos.y < 0 + size +1:
            pos.y = 0 + (size+1)
            vel.y *= WALLDAMPER
        if pos.x > WIDTH - (size+1):
            pos.x = WIDTH - (size+1)
            vel.x *= WALLDAMPER
        elif pos.x < 0 + size + 1:
            pos.x = 0 + (size +1)
            vel.x *= WALLDAMPER





        fill(filler)
        moveCursor()
        box(pos,size)
        show()
        time.sleep(1/FPS)
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
