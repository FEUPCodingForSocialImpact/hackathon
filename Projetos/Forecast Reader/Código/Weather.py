
import pyowm
import serial
from sense_hat import SenseHat
import time
KEY = 'dbb06758ffbd044908ba7488e58457a6'

location = 'Porto,pt'

bl = (51,153,255)
r = (255,0,0)
wh = (255,255,255)
y = (255,255,51)
g = (0,65,0)
o = (255,115,0)
p =(255,102,229)
v = (153,51,255)
x = (0,0,0)

sense = SenseHat()

owm = pyowm.OWM(KEY)
fc = owm.three_hours_forecast(location)
f = fc.get_forecast()
icons = [weather.get_weather_icon_name() for weather in f]
obs = owm.weather_at_place(location)
w = obs.get_weather()

PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.readline()
icon = 0

sense.set_rotation(180)
rainbow = [r, r, r, r, r, r, r, r,
           r, o, o, o, o, o, o, o,
           r, o, y, y, y, y, y, y,
           r, o, y, g, g, g, g, g,
           r, o, y, g, bl, bl, bl, bl,
           r, o, y, g, bl, v, v, v,
           r, o, y, g, bl, v, p, p,
           r, o, y, g, bl, v, p, x
           ]

sense.set_pixels(rainbow)
while True:
    s.write(icons[icon%len(icons)].encode('utf-8'))
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split(' ')
    try:
        a,b = data_list
        if a == 'True' and b == 'True':
            sense.show_message("Temp.")
            sense.show_message("Min. "+str(w.get_temperature(unit='celsius')['temp_min'])+" C",text_colour=bl)
            sense.show_message("Max. "+str(w.get_temperature(unit='celsius')['temp_max'])+" C",text_colour=r)
            sense.show_message("Atual "+str(w.get_temperature(unit='celsius')['temp'])+" C",text_colour=y)
            sense.show_message("Humidade "+str(w.get_humidity())+"%",text_colour=g)
            sense.show_message("Pressao "+str(w.get_pressure()['press'])+" mBar",text_colour=o)
            sense.set_pixels(rainbow)
        elif b == 'True':
            icon += 1
            print(icon%len(icons))
        elif a == 'True':
            icon -= 1
            print(icon%len(icons))
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == "middle":
                    if len(str(time.localtime().tm_min)) < 2:
                        sense.show_message(str(time.localtime().tm_hour)+":0"+str(time.localtime().tm_min)+' '+str(time.localtime().tm_mday)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_year))
                        sense.set_pixels(rainbow)
                    else :
                        sense.show_message(str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+' '+str(time.localtime().tm_mday)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_year))
                        sense.set_pixels(rainbow)
                

    except:
        pass

s.close()
