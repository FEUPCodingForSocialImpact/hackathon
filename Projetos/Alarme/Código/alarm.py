from sense_hat import SenseHat
import pygame
from pygame.locals import *
import time
from espeak import espeak
from Tkinter import *
import pyespeak

e = pyespeak.eSpeak("en")

pygame.init()
pygame.display.set_mode((640, 480))

sense=SenseHat()

p = [159,95,159]
b = [0,0,0]
w = [150, 150, 150]
r = [255,0,0]

normal = [
b,b,b,b,p,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,p,b,b,b,
b,b,b,b,p,b,b,b,
p,b,p,p,p,b,b,b,
b,b,b,b,p,p,b,p,
b,b,b,b,b,b,b,b,
b,b,b,b,p,b,b,b,
]

alarme3 = [
w,w,w,w,p,r,r,r,
w,w,w,w,r,r,r,r,
w,w,w,w,p,r,r,r,
w,w,w,w,p,r,r,r,
p,w,p,p,p,r,r,r,
w,w,w,w,p,p,r,p,
w,w,w,w,w,w,w,w,
w,w,w,w,p,w,w,w,
]

alarme4 = [
w,w,w,w,p,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,p,w,w,w,
w,w,w,w,p,w,w,w,
p,w,p,p,p,w,w,w,
w,w,w,w,p,p,r,p,
w,w,w,w,r,r,r,r,
w,w,w,w,p,r,r,r,
]

alarme1 = [
w,w,w,w,p,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,p,w,w,w,
w,w,w,w,p,w,w,w,
p,r,p,p,p,w,w,w,
r,r,r,r,p,p,w,p,
r,r,r,r,r,w,w,w,
r,r,r,r,p,w,w,w,
]

alarme2 = [
r,r,r,r,p,w,w,w,
r,r,r,r,r,w,w,w,
r,r,r,r,p,w,w,w,
r,r,r,r,p,w,w,w,
p,r,p,p,p,w,w,w,
w,w,w,w,p,p,w,p,
w,w,w,w,w,w,w,w,
w,w,w,w,p,w,w,w,
]

global alarme_1
global alarme_2
global alarme_3
global alarme_4
global alarme_x
global running
global x

alarme_1=False
alarme_2=False
alarme_3=False
alarme_4=False
alarme_x=False
running=False

def off():
    global alarme_1
    global alarme_2
    global alarme_3
    global alarme_4
    global alarme_x
    global running

    alarme_1=False
    alarme_2=False
    alarme_3=False
    alarme_4=False
    alarme_x=False
    sense.set_pixels(normal)
    print("Alarm off")
    e.say("Alarm off")
    
def on():
    global alarme_1
    global alarme_2
    global alarme_3
    global alarme_4
    global alarme_x
    print("Alarm on")
    e.say("Alarm on")
    if alarme_1==True:
        print("Zone 1 locked. Calling the police.")
        sense.set_pixels(alarme1)
        e.say("I am going to give you an advice RUN AWAY The police is on your way and I am picking on my shotgun as well. See you in five")
    elif alarme_2==True:
        print("Zone 2 locked. Calling the police.")
        sense.set_pixels(alarme2)
        e.say("I am going to give you an advice RUN AWAY The police is on your way and I am picking on my shotgun as well. See you in five")
    elif alarme_3==True:
        print("Zone 3 locked. Calling the police.")
        sense.set_pixels(alarme3)
        e.say("I am going to give you an advice RUN AWAY The police is on your way and I am picking on my shotgun as well. See you in five")
    elif alarme_4==True:
        print("Zone 4 locked. Calling the police.")
        sense.set_pixels(alarme4)
        e.say("I am going to give you an advice RUN AWAY The police is on your way and I am picking on my shotgun as well. See you in five")
    elif alarme_x==True:
        print("Zone %s locked. Calling the police."%x)
        sense.set_pixels(normal)
        e.say("I am going to give you an advice RUN AWAY The police is on your way and I am picking on my shotgun as well. See you in five")
    elif event.key == K_UP:
        off()

def on2():
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        global alarme_x
        global x
        print("Alarm on")
        e.say("Alarm on")
        if alarme_1==True:
            print("Zone 1 locked. Calling the police.")
            sense.set_pixels(alarme1)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_2==True:
            print("Zone 2 locked. Calling the police.")
            sense.set_pixels(alarme2)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_3==True:
            print("Zone 3 locked. Calling the police.")
            sense.set_pixels(alarme3)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_4==True:
            print("Zone 4 locked. Calling the police.")
            sense.set_pixels(alarme4)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_x==True:
            print("Zone %s locked. Calling the police."%x)
            sense.set_pixels(normal)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")

def off2():
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        global alarme_x

        alarme_1=False
        alarme_2=False
        alarme_3=False
        alarme_4=False
        alarme_x=False
        sense.set_pixels(normal)
        print("Alarm off")
        e.say("Alarm off")

sense.set_pixels(normal)

class App(Frame):
    def on2(self):
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        global alarme_x
        global x
        print("Alarm on")
        e.say("Alarm on")
        if alarme_1==True:
            print("Zone 1 locked. Calling the police.")
            sense.set_pixels(alarme1)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_2==True:
            print("Zone 2 locked. Calling the police.")
            sense.set_pixels(alarme2)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_3==True:
            print("Zone 3 locked. Calling the police.")
            sense.set_pixels(alarme3)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_4==True:
            print("Zone 4 locked. Calling the police.")
            sense.set_pixels(alarme4)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
        elif alarme_x==True:
            print("Zone %s locked. Calling the police."%x)
            sense.set_pixels(normal)
            e.say("I am going to give you an advice RUN AWAY. The police is on your way and I am picking on my shotgun as well. See you in five")
    def plus(self):
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        global alarme_x
        global x
        x = x+1
        print ("Trigger alarm in room %s?"%x)
        e.say("Trigger alarm in room %s?"%x)
    def minus(self):
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        global alarme_x
        global x
        if x>1:
            x = x-1
            print ("Trigger alarm in room %s?"%x)
            e.say("Trigger alarm in room %s?"%x)
    def ok(self):
        global alarme_x
        global x
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        if x == 1:
            alarme_1=True
            on2()
        elif x == 2:
            alarme_2=True
            on2()
        elif x == 3:
            alarme_3=True
            on2()
        elif x == 4:
            alarme_4=True
            on2()
        else:
            alarme_x=True 
            on2()
        
    def off2(self):
        global alarme_1
        global alarme_2
        global alarme_3
        global alarme_4
        global alarme_x

        alarme_1=False
        alarme_2=False
        alarme_3=False
        alarme_4=False
        alarme_x=False
        sense.set_pixels(normal)
        print("Alarm off")
        e.say("Alarm off")
    def createWidgets(self):
        self.ON = Button(self)
        self.ON["text"] = "ON"
        self.ON["command"] =  self.on2
        self.ON["width"] = 15
        self.ON["height"] = 9
        self.ON.pack({"side": "top"})

        self.OFF = Button(self)
        self.OFF["text"] = "OFF"
        self.OFF["command"] =  self.off2
        self.OFF["width"] = 15
        self.OFF["height"] = 9
        self.OFF.pack({"side": "bottom"})

        self.MINUS = Button(self)
        self.MINUS["text"] = "-"
        self.MINUS["command"] =  self.minus
        self.MINUS["width"] = 15
        self.MINUS["height"] = 9
        self.MINUS.pack({"side": "left"})

        self.PLUS = Button(self)
        self.PLUS["text"] = "+"
        self.PLUS["command"] =  self.plus
        self.PLUS["width"] = 15
        self.PLUS["height"] = 9
        self.PLUS.pack({"side": "right"})

        self.OK = Button(self)
        self.OK["text"] = "OK"
        self.OK["command"] =  self.ok
        self.OK["width"] = 15
        self.OK["height"] = 9
        self.OK.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        x=1
        self.pack()
        self.createWidgets()

myapp = App()
myapp.master.title("System interface")
mode = raw_input("Joystick or interface?").lower()

if mode == "interface":
    print("Interface selected")
    e.say("Interface selected")
    global x
    x=1
    myapp.mainloop()
if mode == "joystick":
    print("Joystick selected")
    e.say("Joystick selected")
    print("Up-turn on the alarm.\nDown-turn off the alarm.\nLeft&Right-choose the room to trigger the alarm.\nClick to confirm.")
    global x
    x=1
    running =True


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                on()
            elif event.key == K_UP:  
                off()               
            elif event.key == K_RIGHT and x>1:
                x = x-1
                print ("Trigger alarm in room %s?"%x)
                e.say("Trigger alarm in room %s?"%x)
            elif event.key == K_LEFT:
                x = x+1
                print ("Trigger alarm in room %s?"%x)
                e.say("Trigger alarm in room %s?"%x)
            elif event.key == K_RETURN:
                if x == 1:
                    alarme_1=True
                    on()
                elif x == 2:
                    alarme_2=True
                    on()
                elif x == 3:
                    alarme_3=True
                    on()
                elif x == 4:
                    alarme_4=True
                    on()
                else:
                    alarme_x=True 
                    on()

root.destroy()

