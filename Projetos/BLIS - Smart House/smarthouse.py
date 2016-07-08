import pygame, os
import time
from pygame import *
from pygame.locals import *
from sense_hat import SenseHat
from blinds import blinds

sense=SenseHat ()

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

#doors and windows
    #unlock
unlocked = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,w,w,e,
e,e,e,e,w,e,e,w,
e,e,e,e,w,e,e,w,
e,e,g,g,g,g,e,e,
e,e,g,g,g,g,e,e,
e,e,g,g,g,g,e,e,
e,e,e,e,e,e,e,e,
]
    #lock
locked = [
e,e,e,e,e,e,e,e,
e,e,e,w,w,e,e,e,
e,e,w,e,e,w,e,e,
e,e,w,e,e,w,e,e,
e,e,r,r,r,r,e,e,
e,e,r,r,r,r,e,e,
e,e,r,r,r,r,e,e,
e,e,e,e,e,e,e,e
]

#lights
    #off
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
    #on - dim
on1 = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]
    #on - bright
on2 = [
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
]
    #on - very bright
on3 = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

#blinds
  #0
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
    #1
one = [
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]
    #2
two = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]
    #3
three = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]
    #4
four = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]
    #5
five = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]
    #6
six = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #7
seven = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o
]
     #8
eight = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

#heating
        #sunless
sunless = [
y,e,e,y,e,e,e,y,
e,y,e,y,y,e,y,e,
e,e,y,y,y,y,e,e,
e,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,e,
e,e,y,y,y,y,e,e,
e,y,e,y,y,e,y,e,
y,e,e,e,y,e,e,y
]
    #sunmore
sunmore = [
o,e,e,o,e,e,e,o,
e,o,e,o,o,e,o,e,
e,e,o,o,o,o,e,e,
e,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,e,
e,e,o,o,o,o,e,e,
e,o,e,o,o,e,o,e,
o,e,e,e,o,e,e,o
]

    #snowflakeless
snowflakeless =[
w,e,w,e,e,w,e,w,
e,w,e,w,w,e,w,e,
w,e,w,e,e,w,e,w,
e,w,e,w,w,e,w,e,
e,w,e,w,w,e,w,e,
w,e,w,e,e,w,e,w,
e,w,e,w,w,e,w,e,
w,e,w,e,e,w,e,w,
]

  #snowflakemore
snowflakemore =[
b,e,b,e,e,b,e,b,
e,b,e,b,b,e,b,e,
b,e,b,e,e,b,e,b,
e,b,e,b,b,e,b,e,
e,b,e,b,b,e,b,e,
b,e,b,e,e,b,e,b,
e,b,e,b,b,e,b,e,
b,e,b,e,e,b,e,b,
]

#music
    #song 2
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
    #volume up
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
    #volume down
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

#tv
    #P-
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
    #P+
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
    #channel 4
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


#settings

#blinds
def blinds1():
    while True:
        choice = int(input("Choose how closed you want the blinds to be from 0 to 8: "))
        if choice==0:
            sense.set_pixels(zero)
            break

        elif choice==1:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            break

        elif choice==2:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            break

        elif choice==3:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            break

        elif choice==4:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            break

        elif choice==5:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            break

        elif choice==6:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            time.sleep(1)
            sense.set_pixels(six)
            break

        elif choice==7:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            time.sleep(1)
            sense.set_pixels(six)
            time.sleep(1)
            sense.set_pixels(seven)
            break

        elif choice==8:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            time.sleep(1)
            sense.set_pixels(six)
            time.sleep(1)
            sense.set_pixels(seven)
            time.sleep(1)
            sense.set_pixels(eight)
            break

        else:
            print("""Invalid Input

""")


#doors
def doors():
    choice = input("Lock or unlock doors? ")
    choice = choice.lower()
    while True:
        if choice == "lock":
    
            sense.set_pixels(locked)

            sense.set_rotation(0)
            break
        elif choice == "unlock":
    
            sense.set_pixels(unlocked)

            sense.set_rotation(0)
            break
        else:
            print("""Invalid Input

""")

#lights
def lights ():
    choice = str(input("Lights: On or Off? "))
    choice = choice.lower()
    if choice == "off":
        sense.set_pixels(off)
        sense.set_rotation(180)
    elif choice == "on":
        choice = str(input("How intense? Dim, bright or very bright? "))    
        choice = choice.lower()
        if choice == "dim":
            sense.set_pixels(on1)
            sense.set_rotation(180)
        elif choice == "bright":
            sense.set_pixels(on2)
            sense.set_rotation(180)
        elif choice == "very bright":
            sense.set_pixels(on3)
            sense.set_rotation(180)

#windows
def windows():
    choice = input("Lock or unlock windows? ")
    choice = choice.lower()
    while True:
        if choice == "lock":
            sense.set_pixels(locked)
            sense.set_rotation(0)
            break
        elif choice == "unlock":        
            sense.set_pixels(unlocked)
            sense.set_rotation(0)
            break



#heating
def heating ():
    t = sense.get_temperature()
    t = round(t, 1)
    print ("Current temperature: "+str(t))
    tmax = float(input('Select maximum temperature: '))
    tmin = float(input('Select minimum temperature: '))
    x = float(input('Select interval for maximum speed: '))
    t1 = tmin - x
    t2 = tmax + x
    if t<tmin and t>t1:
        sense.set_pixels(sunless)
    elif t<t1:
        sense.set_pixels(sunmore)
    elif t>tmax and t<t2:
        sense.set_pixels(snowflakeless)
    elif t>t2:
        sense.set_pixels(snowflakemore)
    else:
        sense.clear()

#music
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

#tv
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

#if
r = True
while r:
    user = str(input("""Set:
- Doors
- Lights
- Windows
- Blinds
- Temperature
- Music
- TV
- Quit
Type here: """))
    user = user.lower()

    if user == "doors":
        doors()
    elif user == "lights":
        lights()
    elif user == "windows":
        windows()
    elif user == "blinds":
        blinds()
    elif user == "temperature":
        heating()
    elif user == "music":
        music()
    elif user == "tv":
        tv()
    elif user == "quit":
        r=False
