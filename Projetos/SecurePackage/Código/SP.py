import csv
from sense_hat import SenseHat
import time
import pygame
sense=SenseHat()




def naofazdiferenca(a,b,m):
    global value1
    global value2
    global variable
    resultado=float(value1)*float(value2)*float(variable.get())
    return resultado

#Size
with open('a.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    rt=[]
    tr=[]
    for row in readCSV:
        op=row[1]
        po=row[0]

        rt.append(po)
        tr.append(op)
        

    global zxc
    global value1
    trex= tr.index(var2.get())
    value1=rt[trex]
              
#Materials

with open('materials.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    rt2=[]
    tr2=[]
    for row in readCSV:
        op2=row[1]
        po2=row[0]

        rt2.append(po2)
        tr2.append(op2)

       
    global value2    
    trex2= tr2.index(var1.get())
    value2=rt2[trex2]


def modulo(numero):
        if numero<0:
                numero=numero*-1
                return numero
        else:
                return numero
#Delta(v)

def v():
        x_anterior=0
        y_anterior=0
        z_anterior=0
        deltax2=0
        deltay2=0
        deltaz2=0
        
        while True:

                acceleration = sense.get_accelerometer_raw()
                x = acceleration['x']
                y = acceleration['y']
                z = acceleration['z']

                x=round(x, 0)
                y=round(y, 0)
                z=round(z, 0)


                deltax= int(x)-int(x_anterior)
                deltay=int(y)-int(y_anterior)
                deltaz=int(z)-int(z_anterior)
 
                vx=int(deltax)-int(deltax2)
                vy=int(deltay)-int(deltay2)
                vz=int(deltaz)-int(deltaz2)

                x_anterior=x
                y_anterior=y
                z_anterior=z
                deltax2=deltax
                deltay2=deltay
                deltaz2=deltaz

                v=[modulo(vx),modulo(vy),modulo(vz)]
                v1=int(modulo(vx))+int(modulo(vy))+int(modulo(vz))
                global value1
                global value2
                global variable
                upperlimt=naofazdiferenca(value1,value2,variable)

                if v1<upperlimt:
                        r = [255,0,0]
                        g = [0,255,0]
                        image=[
                        g,g,g,g,g,g,g,g,
                        g,n,n,n,n,n,n,g,
                        g,n,n,n,n,n,g,g,
                        g,n,n,n,n,g,n,g,
                        g,n,n,n,g,n,n,g,
                        g,g,n,g,n,n,n,g,
                        g,n,g,n,n,n,n,g,
                        g,g,g,g,g,g,g,g,
                        ]
                        sense.set_pixels(image)
                        time.sleep(0.1)
                else:
                        r = [255,0,0]
                        g = [0,255,0]
                        n = [0,0,0]
                        image=[
                        r,r,r,r,r,r,r,r,
                        r,r,n,n,n,n,r,r,
                        r,n,r,n,n,r,n,r,
                        r,n,n,r,r,n,n,r,
                        r,n,n,r,r,n,n,r,
                        r,n,r,n,n,r,n,r,
                        r,r,n,n,n,n,r,r,
                        r,r,r,r,r,r,r,r,
                        ]
                        sense.set_pixels(image)
                        time.sleep(10)

def giro():
    while True:
    
        orientation = sense.get_orientation()
        pitch = orientation['pitch']
        roll = orientation['roll']
        yaw = orientation['yaw']
        if ((roll > 50 and roll < 350 ) or (yaw > 200) or (pitch > 3.5 and pitch <352)):
            print("Package Turned")
            while True:
                pygame.init()
                pygame.mixer.music.load("sound.wav")
                pygame.mixer.music.play()
                sense.set_pixel(7, 3, [255, 0, 0])
                sense.set_pixel(0, 4, [255, 0, 0])
                sense.set_pixel(0, 5, [255, 0, 0])
                sense.set_pixel(0, 6, [255, 0, 0])
                sense.set_pixel(0, 7, [255, 0, 0])
                sense.set_pixel(7, 4, [255, 0, 0])
                sense.set_pixel(7, 5, [255, 0, 0])
                sense.set_pixel(7, 6, [255, 0, 0])
                sense.set_pixel(7, 7, [255, 0, 0])
                sense.set_pixel(0, 3, [255, 0, 0])
                sense.set_pixel(0, 2, [255, 0, 0])
                sense.set_pixel(0, 1, [255, 0, 0])
                sense.set_pixel(0, 0, [255, 0, 0])
                sense.set_pixel(7, 2, [255, 0, 0])
                sense.set_pixel(7, 1, [255, 0, 0])
                sense.set_pixel(7, 0, [255, 0, 0])
                sense.set_pixel(1, 0, [255, 0, 0])
                sense.set_pixel(2, 0, [255, 0, 0])
                sense.set_pixel(3, 0, [255, 0, 0])
                sense.set_pixel(4, 0, [255, 0, 0])
                sense.set_pixel(5, 0, [255, 0, 0])
                sense.set_pixel(6, 0, [255, 0, 0])
                sense.set_pixel(1, 7, [255, 0, 0])
                sense.set_pixel(2, 7, [255, 0, 0])
                sense.set_pixel(3, 7, [255, 0, 0])
                sense.set_pixel(4, 7, [255, 0, 0])
                sense.set_pixel(5, 7, [255, 0, 0])
                sense.set_pixel(6, 7, [255, 0, 0])
                sense.set_pixel(1, 1, [255, 0, 0])
                sense.set_pixel(6, 1, [255, 0, 0])
                sense.set_pixel(2, 2, [255, 0, 0])
                sense.set_pixel(5, 2, [255, 0, 0])
                sense.set_pixel(3, 3, [255, 0, 0])
                sense.set_pixel(4, 3, [255, 0, 0])
                time.sleep(0.6)
                sense.clear()
                time.sleep(0.3)                 
        else:

            while True:
                sense.set_pixel(7, 3, [0, 255, 0])
                sense.set_pixel(0, 4, [0, 255, 0])
                sense.set_pixel(0, 5, [0, 255, 0])
                sense.set_pixel(0, 6, [0, 255, 0])
                sense.set_pixel(0, 7, [0, 255, 0])
                sense.set_pixel(7, 4, [0, 255, 0])
                sense.set_pixel(7, 5, [0, 255, 0])
                sense.set_pixel(7, 6, [0, 255, 0])
                sense.set_pixel(7, 7, [0, 255, 0])
                sense.set_pixel(0, 3, [0, 255, 0])
                sense.set_pixel(0, 2, [0, 255, 0])
                sense.set_pixel(0, 1, [0, 255, 0])
                sense.set_pixel(0, 0, [0, 255, 0])
                sense.set_pixel(7, 2, [0, 255, 0])
                sense.set_pixel(7, 1, [0, 255, 0])
                sense.set_pixel(7, 0, [0, 255, 0])
                sense.set_pixel(1, 0, [0, 255, 0])
                sense.set_pixel(2, 0, [0, 255, 0])
                sense.set_pixel(3, 0, [0, 255, 0])
                sense.set_pixel(4, 0, [0, 255, 0])
                sense.set_pixel(5, 0, [0, 255, 0])
                sense.set_pixel(6, 0, [0, 255, 0])
                sense.set_pixel(1, 7, [0, 255, 0])
                sense.set_pixel(2, 7, [0, 255, 0])
                sense.set_pixel(3, 7, [0, 255, 0])
                sense.set_pixel(4, 7, [0, 255, 0])
                sense.set_pixel(5, 7, [0, 255, 0])
                sense.set_pixel(6, 7, [0, 255, 0])
                sense.set_pixel(1, 1, [0, 255, 0])
                sense.set_pixel(6, 1, [0, 255, 0])
                sense.set_pixel(2, 2, [0, 255, 0])
                sense.set_pixel(5, 2, [0, 255, 0])
                sense.set_pixel(3, 3, [0, 255, 0])
                sense.set_pixel(4, 3, [0, 255, 0])
                time.sleep(2)
                sense.clear()
                time.sleep(1)
                break





