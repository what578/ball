import vector
import colorama
import time



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
def box(center,size):
    vector1 = center.sum(vector.Vector(size,size))
    vector2 = center.sub(vector.Vector(size,size))
    #print(f"center is {center.x} {center.y}")
    #print(f"x for 1 and 2 ={vector1.x} {vector2.x} ")
    #print(f"y for 1 and 2 ={vector1.y} {vector2.y}")
    for x in range(vector1.x - vector2.x +1):
        for y in range(vector1.y -vector2.y +1):
            value = (x+vector2.x) + ((y+vector2.y)*WIDTH)
            value1= x+vector2.x
            value2= (y+vector2.y)*WIDTH
            #if value1 >31 or value1 < 0:
            #
            #if value2 >31 or value2 < 0:
            #    continue
            if 0 <= value and value <= HEIGHT*WIDTH:
                display[value] = "Q"





def fill():
    for x in range(WIDTH*HEIGHT):
        display[x] = " "

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
    move(0,0)

if __name__ == "__main__":
    colorama.init()
    boxC = vector.Vector(5,2)
    vel  = vector.Vector(0,1)
    size = 2
    quit = False
    while not quit:
        fill()
        if boxC.y >= HEIGHT -size*2:
            vel.setY(vel.y*-.9)
            boxC = boxC.sum(vel)
        #elif boxC.y <= HEIGHT - size:
        #    vel.setY(vel.y*-1)
        #    boxC = boxC.sum(vel)
        elif boxC.y <= 0 :
            vel.setY(vel.y*-1)
            boxC = boxC.sum(vel)


        else:
            boxC = boxC.sum(vel)


        box(boxC,size)
        show()
        time.sleep(1/FPS)
