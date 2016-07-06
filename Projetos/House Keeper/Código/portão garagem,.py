from sense_hat import SenseHat
import time
import pygame
from pygame.locals import *
sense = SenseHat()

pygame.init()
pygame.display.set_mode((640, 480))
sense.clear()

q = [0,0,255]
b = [0,0,0]

image = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,]





image2 = [
    b,b,b,b,b,b,b,b,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q
    ]





image3 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,]



image4 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        ]



image5 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        ]



image6 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        ]



image7 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        q,q,q,q,q,q,q,q,
        q,q,q,q,q,q,q,q,
        ]



image8 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        q,q,q,q,q,q,q,q,
        ]



image9 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]



image10 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]
    
image11 = [
    q,q,q,q,q,q,q,q,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]



image12 = [
q,q,q,q,q,q,q,q,
q,q,q,q,q,q,q,q,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,]



image13 = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]



image14 = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]



image15 = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]



image16 = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,]



image17 = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    b,b,b,b,b,b,b,b,]



image18 = [
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,
    q,q,q,q,q,q,q,q,]


def open_animation ():
        sense.set_pixels(image)
        time.sleep (0.5)
        sense.set_pixels(image2)
        time.sleep (0.5)
        sense.set_pixels(image3)
        time.sleep (0.5)
        sense.set_pixels(image4)
        time.sleep (0.5)
        sense.set_pixels(image5)
        time.sleep (0.5)
        sense.set_pixels(image6)
        time.sleep (0.5)
        sense.set_pixels(image7)
        time.sleep (0.5)
        sense.set_pixels(image8)
        time.sleep (0.5)
        sense.set_pixels(image9)
        time.sleep (0.5)



def closing_animation():
        sense.set_pixels(image9)
        time.sleep (0.5)
        sense.set_pixels(image8)
        time.sleep (0.5)
        sense.set_pixels(image7)
        time.sleep (0.5)
        sense.set_pixels(image6)
        time.sleep (0.5)
        sense.set_pixels(image5)
        time.sleep (0.5)
        sense.set_pixels(image4)
        time.sleep (0.5)
        sense.set_pixels(image3)
        time.sleep (0.5)
        sense.set_pixels(image2)
        time.sleep (0.5)
        sense.set_pixels(image)
        time.sleep (0.5)




def open_state() :
    open_state = raw_input("estado do portão:")
    if open_state == "fechar":
        print "fechando o portão"
        opening_animation()
    elif open_state == "abrir":
        print "abrindo o portão"
        closing_animation()
        
    else:
        print "erro"        

def joystik ():
        portao = 1
        while True:
                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_DOWN and portao == 0 :
                                        portao = 1
                                        print('opening...')
                                        open_animation()          
                                elif event.key == K_UP and portao == 0:
                                        print ("O portão já está fechado ")
                                elif event.key == K_UP and portao == 1:
                                        portao = 0 
                                        print('closing...')
                                        closing_animation()
                                elif event.key == K_DOWN and portao == 1:
                                        print ("O portão já está aberto")
                                        
                                        
#1-aberto
#2-fechado                                        






joystik()
                               


      
