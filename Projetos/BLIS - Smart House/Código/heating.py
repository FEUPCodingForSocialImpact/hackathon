from sense_hat import SenseHat

sense = SenseHat()
#heating
t = sense.get_temperature()
t = round(t, 1)
print ("Current temperature: "+str(t))
tmax = float(input('Select maximum temperature: '))
tmin = float(input('Select minimum temperature: '))
x = float(input('Select interval for maximum speed: '))
t1 = tmin - x
t2 = tmax + x

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


    #settings
def heating ():
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
heating()
