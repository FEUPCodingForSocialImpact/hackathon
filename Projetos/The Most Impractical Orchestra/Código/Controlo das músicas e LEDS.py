import serial
from sense_hat import SenseHat

sense = SenseHat()

w= [255,255,255]
g=[0,255,0]
e = [0,0,0]
r = [255,0,0]
a= [0,128,255]
o = [255,127,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
c = [102,51,0]
cp = [255,204,153]
ae= [51,153,255]
grey = [220,220,220]
c1 = [143,227,143]
c2 = [15,128,15]
c3 = [13,181,13]
c4 = [96,158,96]
c5 = [0,69,0]
cast= [102,51,0]
cc=[204,102,0]
Red = (255,0,0)
Wite = (255,255,255)
db = [0,76,153]
dy = [255,188,0]
r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [64,64,64]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
w = [255,255,255]
db = [0,76,153]
dy = [255,188,0]
c = [204,102,0]
p = [255,204,153]
t = [51,25,0]
l=[153,255,255]

PORT0 = "/dev/ttyACM0"
PORT1 = "/dev/ttyACM3"
PORT2 = "/dev/ttyACM4"

BAUD = 115200

s0 = serial.Serial(PORT0)
s0.baudrate = BAUD
s0.parity   = serial.PARITY_NONE
s0.databits = serial.EIGHTBITS
s0.stopbits = serial.STOPBITS_ONE

s1 = serial.Serial(PORT1)
s1.baudrate = BAUD
s1.parity   = serial.PARITY_NONE
s1.databits = serial.EIGHTBITS
s1.stopbits = serial.STOPBITS_ONE

s2 = serial.Serial(PORT2)
s2.baudrate = BAUD
s2.parity   = serial.PARITY_NONE
s2.databits = serial.EIGHTBITS
s2.stopbits = serial.STOPBITS_ONE


print("1) B*** Lasagna (PewDiePie);") 
print("2) Crash Bandicoot theme;")
print("3) Despacito (Luis Fonsi);")
print("4) Fortnite (Default Dance);")
print("5) Mario Theme")
print("6) Megalovania (Undertale);")
print("7) Minecraft (Menu Theme);")
print("8) Old Town Road (Lil Nas X);")
print("9) Pokémon (Opening);")
print("10) Pokémon (Viridian City);")
print("11) Tetris;")

u = input("Digite o número da música que quer reproduzir: ")


if u=='1':
    lasagna = [
    w,r,r,r,r,r,r,w,
    w,r,w,w,w,w,r,w,
    w,r,w,w,w,w,r,w,
    w,r,r,w,w,r,r,w,
    w,r,r,w,w,r,r,w,
    w,r,r,w,w,r,r,w,
    w,r,r,w,w,r,r,w,
    w,r,r,r,r,r,r,w,
    ]
    sense.set_pixels(lasagna)

elif u=='2':
    crash= [
        e,e,e,g,e,e,e,e,
        e,r,r,g,r,r,r,e,
        r,r,r,r,r,r,r,r,
        r,w,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        e,r,r,r,r,r,r,e,
        e,e,r,r,r,r,e,e,
        ]
    sense.set_pixels (crash)

elif u=='4':
    fortnite= [
        a,a,a,a,a,a,a,a,
        a,a,w,w,w,w,a,a,
        a,a,w,w,w,w,a,a,
        a,a,w,w,a,a,a,a,
        a,a,w,w,w,w,a,a,
        a,a,w,w,w,w,a,a,
        a,a,w,w,a,a,a,a,
        a,a,w,w,a,a,a,a,
        ]

    sense.set_pixels (fortnite)
elif u=='5':
    mario = [
        e,e,e,r,r,r,w,e,
        e,e,e,r,r,r,r,r,
        e,e,c,cp,c,e,cp,e,
        e,e,c,cp,cp,c,c,e,
        e,e,e,c,cp,cp,cp,e,
        e,r,r,y,b,b,y,e,
        w,e,b,b,b,b,b,w,
        e,e,c,e,e,e,c,e
        ]
    
    sense.set_pixels (mario)
elif u=='6':

    megalovania= [
        e, e, w, w, w, w, e, e,
        e, w, w, w, w, w, w, e,
        w,g, g, w, w, ae, ae, w,
        w, g, e, w, w, e, ae, w,
        w, w, w, w, w, w, w, w,
        e, w, w, w, w, w, w, e,
        e, e, w, w, w, w, e, e,
        e, e, w, w, w, w, e, e,
        ]
    sense.set_pixels (megalovania)

elif u=='7':
    creeper = [
        grey,c3,c4,c3,grey,g,c3,c5,
        c5,c2,c2,g,c5,c4,g,grey,
        c3,e,e,c4,g,e,e,grey,
        g,e,e,g,c3,e,e,c5,
        c3,c5,g,e,e,grey,g,g,
        g,c3,e,e,e,e,c3,grey,
        grey,c5,e,e,e,e,g,c4,
        c2,c3,e,c2,grey,e,c5,c2
        ]
    sense.set_pixels(creeper)
elif u=='8':
    old_town_road= [
        e,e,e,e,e,e,e,e,
        e,e,cast,cast,cast,cast,e,e,
        e,e,cast,cc,cc,cast,e,e,
        cast,e,c,cast,cast,cast,e,cast,
        cast,cast,cast,cast,cast,cast,cast,cast,
        cast,cast,cast,cast,cast,cast,cast,cast,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        ]
    sense.set_pixels (old_town_road)
elif u=='9':
    pokebola= [
        e, e, Red, Red, Red, Red, e, e,
        e, Red, Red,Red,Red,Red,Red, e,
        Red, Red,Red,Red,Red,Red,Red,Red,
        Red, Red,Red,Wite,Wite,Red,Red,Red,
        Red, Red,Red,Wite,Wite,Red,Red,Red,
        Wite, Wite,Wite,Wite,Wite,Wite,Wite,Wite,
        e, Wite,Wite,Wite,Wite,Wite,Wite,e,
        e,e,Wite,Wite,Wite,Wite,e,e,
        ]
    sense.set_pixels(pokebola)
elif u=='10':
    pikachu1 = [
        e,db,db,e,e,e,e,db,
        e,e,y,dy,e,e,e,dy,
        e,e,e,y,y,y,y,dy,
        dy,dy,e,y,e,dy,dy,e,
        dy,dy,e,r,y,y,y,dy,
        e,dy,e,y,dy,dy,dy,e,
        e,dy,y,dy,y,dy,y,e,
        e,e,y,dy,cc,cc,dy,e,
        ]
    sense.set_pixels(pikachu1)
elif u=='11':
    tetris=[
        b,b,l,b,b,b,b,b,
        b,b,l,b,b,b,b,b,
        b,b,l,b,b,b,b,b,
        b,b,l,b,o,b,b,b,
        r,b,b,p,o,o,o,b,
        r,r,b,p,p,g,g,r,
        y,r,b,p,g,g,r,r,
        y,y,l,l,l,l,r,b,
        ]

    sense.set_pixels(tetris)
elif u=='3':
    despacito = [
        w,w,t,t,t,t,t,t,
        w,w,t,p,p,p,p,p,
        w,w,t,e,e,e,e,e,
        w,p,p,e,e,p,e,e,
        w,p,p,p,p,p,p,p,
        w,w,b,p,r,r,p,b,
        w,w,b,p,p,p,p,b,
        w,w,b,b,b,b,b,b
        ]
    sense.set_pixels(despacito)

s0.write('{}\n'.format(u).encode('UTF-8'))
s1.write('{}\n'.format(u).encode('UTF-8'))
s2.write('{}\n'.format(u).encode('UTF-8'))