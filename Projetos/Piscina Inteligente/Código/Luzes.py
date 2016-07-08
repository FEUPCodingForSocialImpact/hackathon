import pygame
import datetime
import time


from sense_hat import SenseHat
from pygame.locals import *
from sense_hat import SenseHat


pygame.init()
pygame.display.set_mode((1,1))

sense = SenseHat()


g = [0, 255,0]
o = [255, 0, 0]

luzes_ligadas= [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g
]

luzes_desligadas= [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o

]

def ligado():
    sense.set_pixels(luzes_ligadas)
    time.sleep(1)
   

def desligado():
    sense.set_pixels(luzes_desligadas)
    time.sleep(1)
  


def luzes():
    desligado()
    button = 1
    while True:
        t = time
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_UP): 
                ligado()
                button = 0
                print ("LUZES LIGADAS!")
                
                

            elif (event.type == KEYDOWN and event.key == K_RETURN): 
                desligado()
                print ("LUZES DESLIGADAS!")
                

          
            while button == 1:
                if (t>=20 or t<=7): 
                    print ("LUZES LIGADAS!")
                    ligado()
                    button = 0
                    
                    
                


luzes()


