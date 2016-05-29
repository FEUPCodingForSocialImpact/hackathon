import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import pygame, os
import time
from pygame import *
from pygame.locals import *
from sense_hat import SenseHat
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



#commands
    #doors
def db():
    dr = tkinter.Tk()
    dr.geometry("100x50")
    dr.wm_title("Doors")
    d1 = ttk.Button(dr, text = "Unlock", command = doorsopen)
    d2 = ttk.Button(dr, text = "Lock", command = doorsclosed)
    d1.pack()
    d2.pack()

def doorsclosed():
    sense.set_pixels(locked)
    sense.set_rotation(0)

def doorsopen():
    sense.set_pixels(unlocked)
    sense.set_rotation(0)


    #lights
def lb():
    lg = tkinter.Tk()
    lg.geometry('150x100')
    lg.wm_title("Lights")
    l1 = ttk.Button(lg, text = "Dim", command = lightdim)
    l2 = ttk.Button(lg, text = "Bright", command = lightbright)
    l3 = ttk.Button(lg, text = "Very Bright", command = lightvb)
    l4 = ttk.Button(lg, text = "Off", command = lightoff)
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()

def lightoff():
    sense.set_pixels(off)
        
def lightdim():
    sense.set_pixels(on1)

def lightbright():      
    sense.set_pixels(on2)
           
def lightvb():
    sense.set_pixels(on3)

    #windows
def wb():
    wr = tkinter.Tk()
    wr.geometry("100x50")
    w1 = ttk.Button(wr, text = "Unlock", command = unlockwindows)
    w2 = ttk.Button(wr, text = "Lock", command = lockwindows)
    w1.pack()
    w2.pack()    

def lockwindows():
    sense.set_pixels(locked)
def unlockwindows():    
    sense.set_pixels(unlocked)

    #blinds
def bb():
    global br
    br = tkinter.Tk()
    br.geometry("100x300")
    br.wm_title("Blinds")
    b0 = ttk.Button(br, text = "0", command = b00)
    b1 = ttk.Button(br, text = "1", command = b10)
    b2 = ttk.Button(br, text = "2", command = b20)
    b3 = ttk.Button(br, text = "3", command = b30)
    b4 = ttk.Button(br, text = "4", command = b40)
    b5 = ttk.Button(br, text = "5", command = b50)
    b6 = ttk.Button(br, text = "6", command = b60)
    b7 = ttk.Button(br, text = "7", command = b70)
    b8 = ttk.Button(br, text = "8", command = b80)

    b0.pack()
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    b6.pack()
    b7.pack()
    b8.pack()
    
def b00():
    sense.set_pixels(zero)

def b10():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)

def b20():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)

def b30():   
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)
    br.after(1000)
    sense.set_pixels(three)

def b40():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)
    br.after(1000)
    sense.set_pixels(three)
    br.after(1000)
    sense.set_pixels(four)

def b50():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)
    br.after(1000)
    sense.set_pixels(three)
    br.after(1000)
    sense.set_pixels(four)
    br.after(1000)
    sense.set_pixels(five)

def b60():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)
    br.after(1000)
    sense.set_pixels(three)
    br.after(1000)
    sense.set_pixels(four)
    br.after(1000)
    sense.set_pixels(five)
    br.after(1000)
    sense.set_pixels(six)

def b70():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)
    br.after(1000)
    sense.set_pixels(three)
    br.after(1000)
    sense.set_pixels(four)
    br.after(1000)
    sense.set_pixels(five)
    br.after(1000)
    sense.set_pixels(six)
    br.after(1000)
    sense.set_pixels(seven)

def b80():
    global br
    sense.set_pixels(zero)
    br.after(1000)
    sense.set_pixels(one)
    br.after(1000)
    sense.set_pixels(two)
    br.after(1000)
    sense.set_pixels(three)
    br.after(1000)
    sense.set_pixels(four)
    br.after(1000)
    sense.set_pixels(five)
    br.after(1000)
    sense.set_pixels(six)
    br.after(1000)
    sense.set_pixels(seven)
    br.after(1000)
    sense.set_pixels(eight)

def tmpb():
    top = tkinter.Tk()
    top.wm_title("Temperature")
    l1 = Label(top, text="Minimum temperature:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Maximim temperature:")
    l2.pack()
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    l3 = Label(top, text="Maximum speed interval:")
    l3.pack()
    global e3
    e3 = Entry(top, bd =5)
    e3.pack()
    b1 = Button(top, text = 'Set', command = temp)
    b1.pack()
    top.mainloop()

def temp():
    global e1
    global e2
    global e3
    t = sense.get_temperature()
    t = round(t, 1)
    tmin = float(e1.get())
    tmax = float(e2.get())
    t1 = tmin - float(e3.get())
    t2 = tmax + float(e3.get())
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

def music():
    root = tkinter.Tk()
    root.geometry("150x150")
    root.wm_title("Music")
    b1 = ttk.Button(root, text = 'V+', command = vdown)
    b2 = ttk.Button(root, text = 'V-', command = vup)
    b3 = ttk.Button(root, text = 'Next', command = nextm)
    b4 = ttk.Button(root, text = 'Previous', command = previousm)
    b5 = ttk.Button(root, text = 'On/Off', command = moff)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    sense = SenseHat()
    sense.clear()
    pygame.init()
    pygame.display.set_mode((15, 15))
    mixer.init()
    #music
    global path
    path = "/home/pi/Desktop/Smart House/Music"
    global mfiles
    mfiles = [f for f in os.listdir(path) if f.endswith('.mp3')]
    global abc
    abc = 2
    global state
    state = "Off"
    
def moff():
    global state
    global path
    global mfiles
    global abc
    if state == "On":
        sense.clear()
        state = "Off"
        mixer.music.stop()
        pygame.quit()
    elif state == "Off":
        sense.set_pixels(song2)
        state = "On"
        mixer.music.load(path + '/' + mfiles[abc])
        mixer.music.play()


def vup():
    sense.set_pixels(volumedown)

def vdown():
    sense.set_pixels(volumeup)

def previousm():
    sense.set_pixels(song2) 
    global abc
    if abc>0:
        abc = abc-1
    else:
        abc= len(mfiles)-1
    mixer.music.load(path + '/' + mfiles[abc])
    mixer.music.play()

def nextm():
    sense.set_pixels(song2) 
    global abc
    if abc<(len(mfiles)-1):
        abc = abc+1
    else:
        abc = 0
    mixer.music.load(path + '/' + mfiles[abc])
    mixer.music.play()

def tv():
    root = tkinter.Tk()
    root.geometry("150x150")
    root.wm_title("Tv")
    b1 = ttk.Button(root, text = 'V+', command = vdown)
    b2 = ttk.Button(root, text = 'V-', command = vup)
    b3 = ttk.Button(root, text = 'P+', command = nexttv)
    b4 = ttk.Button(root, text = 'P-', command = prevtv)
    b5 = ttk.Button(root, text = 'On/Off', command = tvoff)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    sense = SenseHat()
    sense.clear()
    pygame.init()
    pygame.display.set_mode((15,15))
    global state2
    state2 = "Off"

def tvoff():
    global state2
    if state2 == "On":
        sense.clear()
        state2 = "Off"

    elif state2 == "Off":
        sense.set_pixels(channel4)
        state2 = "On"
def prevtv():
    sense.set_pixels(bw)
def nexttv():
    sense.set_pixels(fw)
    
    

#init
root = tkinter.Tk()
root.geometry("150x200")
root.wm_title("Smart House")
b1 = ttk.Button(root, text = 'Doors', command = db)
b2 = ttk.Button(root, text = 'Lights', command = lb)
b3 = ttk.Button(root, text = 'Windows', command = wb)
b4 = ttk.Button(root, text = 'Blinds', command = bb)
b5 = ttk.Button(root, text = 'Temp', command = tmpb)
b6 = ttk.Button(root, text = 'Music', command = music)
b7 = ttk.Button(root, text = 'Tv', command = tv)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

