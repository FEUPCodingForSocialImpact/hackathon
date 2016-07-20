from sense_hat import SenseHat
import os, pygame
from pygame import *

sense = SenseHat()
sense.clear()
o = [255,127,0]
y = [255,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
w = [150,150,150]

off = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e

]

music = [
e,e,e,e,e,e,e,e,
e,e,w,w,w,e,e,e,
e,w,w,w,w,w,e,e,
e,w,w,e,w,w,e,e,
e,w,w,w,w,w,e,e,
e,e,w,w,w,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

song1 = [
b,b,b,b,b,b,b,b,
b,b,y,y,y,b,b,b,
b,y,y,y,y,y,b,b,
b,y,y,b,y,y,b,b,
b,y,y,y,y,y,b,b,
b,b,y,y,y,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

song2 = [
o,o,o,o,o,o,o,o,
o,o,v,v,v,o,o,o,
o,v,v,v,v,v,o,o,
o,v,v,o,v,v,o,o,
o,v,v,v,v,v,o,o,
o,o,v,v,v,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
]

volumeup = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,w,e,e,e,e,
e,w,w,w,e,e,i,e,
w,w,w,w,e,i,i,i,
e,w,w,w,e,e,i,e,
e,e,w,w,e,e,e,e,
e,e,e,e,e,e,e,e
]

volumedown = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,w,e,e,e,e,
e,w,w,w,e,e,e,e,
w,w,w,w,e,i,i,i,
e,w,w,w,e,e,e,e,
e,e,w,w,e,e,e,e,
e,e,e,e,e,e,e,e
]

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

    
def music():
    sense = SenseHat()
    sense.clear()
    pygame.init()
    pygame.display.set_mode((640, 480))
    mixer.init()
    #music
    path = "/home/pi/Desktop/Smart House/Music"
    mfiles = [f for f in os.listdir(path) if f.endswith('.mp3')]
    abc = 2
    state = "Off"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN and state == "On":
                    sense.clear()
                    state = "Off"
                    mixer.music.stop()
                    running = False
                elif event.key == K_RETURN and state == "Off":
                    sense.set_pixels(song2)
                    state = "On"
                    
                    mixer.music.load(path + '/' + mfiles[abc])
                    mixer.music.play()
                elif event.key == K_DOWN:
                     sense.set_pixels(volumedown)
                elif event.key == K_UP:
                     sense.set_pixels(volumeup)
                elif event.key == K_LEFT:
                    sense.set_pixels(song2) 
                    if abc>0:
                        abc = abc-1
                    else:
                        abc= len(mfiles)-1
                    mixer.music.load(path + '/' + mfiles[abc])
                    mixer.music.play()
                                             
                elif event.key == K_RIGHT:
                    sense.set_pixels(song2)
                    if abc<(len(mfiles)-1):
                         abc = abc+1
                    else:
                         abc = 0
                    mixer.music.load(path + '/' + mfiles[abc])
                    mixer.music.play()
                    
            
    pygame.quit()

music()


