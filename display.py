import vector
import colorama
import time
import msvcrt
#import curses



HEIGHT,WIDTH = 32,32
display      = [None]  * (HEIGHT*WIDTH)
FPS          = 10



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
    x = vector2.x
    y = vector2.y
    while y <= vector1.y:
        while x <= vector1.x:
            if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
                display[(y*WIDTH) + x] = "Q"
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
def move (y, x):
    print("\033[%d;%dH" % (y, x))

def show():
    startRow,endRow = 0,WIDTH
    for y in range(HEIGHT):
        print("".join(display[startRow:endRow]))
        startRow += WIDTH
        endRow   += WIDTH

if __name__ == "__main__":
    colorama.init()
    filler="*"
    boxC = vector.Vector(5,0)
    vel  = vector.Vector(0,1)
    size = 2
    quit = False
    char = None

    fill(filler)
    box(boxC,size)
    show()
    #while not quit:
    #    char = msvcrt.getch()
    #    if char == "q":
    #        quit = True
    #    print(char)
        #C = boxC.sum(vel)
        #box(boxC,size)
        #show()
        #time.sleep(1/FPS)