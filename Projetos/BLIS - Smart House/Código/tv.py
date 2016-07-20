import pygame
from pygame.locals import *
from sense_hat import SenseHat

#colours
r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 150]
i = [75, 0, 130]
v = [159, 0, 255]
e = [0, 0, 0]
w = [150, 150, 150]
z = [224,255,255]

zero = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

volumedown = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,w,e,e,e,e,
e,w,w,w,e,e,e,e,
w,w,w,w,e,v,v,v,
e,w,w,w,e,e,e,e,
e,e,w,w,e,e,e,e,
e,e,e,e,e,e,e,e
]

volumeup = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,w,e,e,e,e,
e,w,w,w,e,e,v,e,
w,w,w,w,e,v,v,v,
e,w,w,w,e,e,v,e,
e,e,w,w,e,e,e,e,
e,e,e,e,e,e,e,e
]

channel4 = [
e,e,e,z,z,e,e,e,
e,e,e,z,z,e,z,e,
e,z,z,z,z,z,z,e,
e,z,e,z,z,e,e,e,
e,e,e,z,z,z,e,e,
e,e,e,z,e,z,e,e,
e,e,z,z,e,z,z,e,
e,e,z,e,e,e,e,e
]

channel5 = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,y,y,y,b,b,
b,b,b,w,y,w,b,b,
g,g,g,y,y,y,g,g,
g,g,g,e,r,e,g,g,
g,g,g,e,r,e,g,g,
g,g,g,e,r,e,g,g,
]

fw = [
e,e,e,e,e,e,e,e,
e,w,w,w,e,e,e,e,
e,w,e,e,w,e,e,e,
e,w,e,e,w,e,v,e,
e,w,w,w,e,v,v,v,
e,w,e,e,e,e,v,e,
e,w,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

bw = [
e,e,e,e,e,e,e,e,
e,w,w,w,e,e,e,e,
e,w,e,e,w,e,e,e,
e,w,e,e,w,e,e,e,
e,w,w,w,e,v,v,v,
e,w,e,e,e,e,e,e,
e,w,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]


def tv():
    sense = SenseHat()
    sense.clear()
    pygame.init()
    pygame.display.set_mode((640, 480))
    state = "Off"
    done=True
    while done:
        for event in pygame.event.get():

            
            if event.type == KEYDOWN:
                if event.key == K_RETURN and state == "On":
                    sense.clear()
                    state = "Off"
                    done=False
                    
                elif event.key == K_RETURN and state == "Off":
                    sense.set_pixels(channel4)
                    state = "On"
                elif event.key == K_DOWN:
                    sense.set_pixels(volumedown)
                elif event.key == K_UP:
                    sense.set_pixels(volumeup)
                elif event.key == K_LEFT:
                    sense.set_pixels(bw)
                elif event.key == K_RIGHT:
                    sense.set_pixels(fw)              
    pygame.quit()
            
                
tv()                    

