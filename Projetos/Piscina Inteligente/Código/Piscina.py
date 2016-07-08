import pygame
import time


from sense_hat import SenseHat
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.mixer.music.load("alarme.mp3")

pygame.init()
pygame.display.set_mode((1,1))

sense = SenseHat()


o = [255, 0, 0]
b = [0, 0, 255]

image_fechada= [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_1= [
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_2= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_3= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_4= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_5= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_6= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

image_7= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
o,o,o,o,o,o,o,o
]

image_aberta= [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b
]


def abrir():
    sense.set_pixels(image_fechada)
    time.sleep(1)
    sense.set_pixels(image_1)
    time.sleep(1)
    sense.set_pixels(image_2)
    time.sleep(1)
    sense.set_pixels(image_3)
    time.sleep(1)
    sense.set_pixels(image_4)
    time.sleep(1)
    sense.set_pixels(image_5)
    time.sleep(1)
    sense.set_pixels(image_6)
    time.sleep(1)
    sense.set_pixels(image_7)
    time.sleep(1)
    sense.set_pixels(image_aberta)

def fechar():
    sense.set_pixels(image_aberta)
    time.sleep(1)
    sense.set_pixels(image_7)
    time.sleep(1)
    sense.set_pixels(image_6)
    time.sleep(1)
    sense.set_pixels(image_5)
    time.sleep(1)
    sense.set_pixels(image_4)
    time.sleep(1)
    sense.set_pixels(image_3)
    time.sleep(1)
    sense.set_pixels(image_2)
    time.sleep(1)
    sense.set_pixels(image_1)
    time.sleep(1)
    sense.set_pixels(image_fechada)

sense.clear()

sense.set_pixels(image_aberta)




def openclose():
    state = "open"
    while True:
        if state == "close":
            for event in pygame.event.get():
                
                if (event.type == KEYDOWN and event.key == K_LEFT):
                    print ("A ABRIR")
                    abrir()
                    print ("ABERTA")
                    state = "open"
                    print (state)
                    break
                
                if (event.type == KEYDOWN and event.key == K_DOWN):
                    print ("ALARME")
                    pygame.mixer.music.play()
                    break

                      
        elif state == "open":
            for event in pygame.event.get():
                seconds = 0
                time_start = time.time()
                
                if(event.type == KEYDOWN and event.key == K_RIGHT):
                    print ("A FECHAR")
                    fechar()
                    print ("FECHADA")
                    state = "close"
                    print (state)
                    break
                
                while True:     
                    if seconds < 5:
                        seconds = round(seconds,0)
                        time.sleep(1)
                        seconds = time.time() - time_start
                        sense.set_pixels(image_aberta)
                        

                        
                    else:
                        print ("A FECHAR")
                        fechar()
                        print ("FECHADA")
                        state="close"
                        button=0
                        break
                


openclose()

