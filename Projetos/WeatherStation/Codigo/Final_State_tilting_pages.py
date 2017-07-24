
#Preparação do Script

from sense_hat import SenseHat
from time import sleep
from datetime import datetime
from guizero import App,Text,TextBox,PushButton,Slider,Picture, Combo, CheckBox, ButtonGroup, info
sense = SenseHat()

from requests import get
import json
from pprint import pprint
from threading import Thread
from time import sleep

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):

    #converter graus em radianos
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    dlon = lon2 - lon1 
    dlat = lat2 - lat1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance = 2 * asin(sqrt(a)) * 6371 #6371 is the radius of the Earth
    return distance
now = datetime.now()





   
horas= ('{0}:{1} {2}/{3}/{4}'.format(now.hour, now.minute,now.day, now.month, now.year))

#CORES RGB
b =[255, 255, 255] #branco
a=[0,51,102] #azul escuro
c= [0,0,205] #azul claro
y=[255,215,0] #amarelo
l=[210,105,30] #laranja
v=[255,51,51] #vermelho
r=[125,0,0] #vermelho escuro
z=[105,105,105]#cinza

#MATRIZES DE DIGITOS
digitos=[]



#Digito 0
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,b,z,b,z,
b,z,b,z,b,z,b,z,
b,z,b,z,b,z,b,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

#Digito1
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,z,z,b,z,
b,z,b,z,z,b,b,z,
b,z,b,z,z,z,b,z,
b,z,b,z,z,z,b,z,
b,b,b,z,z,z,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])



#Digito2
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,z,b,z,b,b,b,z,
b,z,b,z,b,z,z,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

#Digito3
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,z,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])


#Digito4
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,z,b,z,
b,z,b,z,b,z,b,z,
b,z,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,b,b,z,z,z,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

#Digito5
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,b,z,z,z,
b,z,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

#Digito65
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,b,z,z,z,
b,z,b,z,b,b,b,z,
b,z,b,z,b,z,b,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])
#Digito7
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,z,b,z,z,z,b,z,
b,z,b,z,z,z,b,z,
b,b,b,z,z,z,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])
#Digito8
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,b,z,b,z,
b,z,b,z,b,b,b,z,
b,z,b,z,b,z,b,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])
#Digito9
digitos.append([
z,z,z,z,z,z,z,z,
b,b,b,z,b,b,b,z,
b,z,b,z,b,z,b,z,
b,z,b,z,b,b,b,z,
b,z,b,z,z,z,b,z,
b,b,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])
#Digito10
digitos.append([
z,z,z,z,z,z,z,z,
z,z,b,z,b,b,b,z,
z,b,b,z,b,z,b,z,
z,z,b,z,b,z,b,z,
z,z,b,z,b,z,b,z,
z,z,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

#Digito 11
digitos.append([
z,z,z,z,z,z,z,z,
z,z,b,z,z,z,b,z,
z,b,b,z,z,b,b,z,
z,z,b,z,z,z,b,z,
z,z,b,z,z,z,b,z,
z,z,b,z,z,z,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

#Digito 12
digitos.append([
z,z,z,z,z,z,z,z,
z,z,b,z,b,b,b,z,
z,b,b,z,z,z,b,z,
z,z,b,z,b,b,b,z,
z,z,b,z,b,z,z,z,
z,z,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])




#Digito 13
digitos.append([
z,z,z,z,z,z,z,z,
z,z,b,z,b,b,b,z,
z,b,b,z,z,z,b,z,
z,z,b,z,b,b,b,z,
z,z,b,z,z,z,b,z,
z,z,b,z,b,b,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])

# Digito 14
digitos.append([
z,z,z,z,z,z,z,z,
z,z,b,z,b,z,b,z,
z,b,b,z,b,z,b,z,
z,z,b,z,b,b,b,z,
z,z,b,z,z,z,b,z,
z,z,b,z,z,z,b,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z
])


# Digito 15
digitos.append([
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,a,a,
a,a,b,a,b,b,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
])

# Digito 16
digitos.append([
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,a,a,
a,a,b,a,b,b,b,a,
a,a,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
])

# Digito 17
digitos.append([
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,a,a,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,a,a,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
])

# Digito 18
digitos.append([
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
])

# Digito 19
digitos.append([
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
])

# Digito 20
digitos.append([
c,c,c,c,c,c,c,c,
b,b,b,c,b,b,b,c,
c,c,b,c,b,c,b,c,
b,b,b,c,b,c,b,c,
b,c,c,c,b,c,b,c,
b,b,b,c,b,b,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
])

# Digito 21
digitos.append([
c,c,c,c,c,c,c,c,
b,b,b,c,c,c,b,c,
c,c,b,c,c,b,b,c,
b,b,b,c,c,c,b,c,
b,c,c,c,c,c,b,c,
b,b,b,c,c,c,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
])
       
# Digito 22
digitos.append([
c,c,c,c,c,c,c,c,
b,b,b,c,b,b,b,c,
c,c,b,c,c,c,b,c,
b,b,b,c,b,b,b,c,
b,c,c,c,b,c,c,c,
b,b,b,c,b,b,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
])
    
# Digito 23
digitos.append([
c,c,c,c,c,c,c,c,
b,b,b,c,b,b,b,c,
c,c,b,c,c,c,b,c,
b,b,b,c,b,b,b,c,
b,c,c,c,c,c,b,c,
b,b,b,c,b,b,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
])   

# Digito 24
digitos.append([
c,c,c,c,c,c,c,c,
b,b,b,c,b,c,b,c,
c,c,b,c,b,c,b,c,
b,b,b,c,b,b,b,c,
b,c,c,c,c,c,b,c,
b,b,b,c,c,c,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
])
    
# Digito 25
digitos.append([
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,y,y,
b,b,b,y,b,b,b,y,
b,y,y,y,y,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
])

# Digito 26
digitos.append([
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,y,y,
b,b,b,y,b,b,b,y,
b,y,y,y,b,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
])

# Digito 27
digitos.append([
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,y,y,b,y,
b,b,b,y,y,y,b,y,
b,y,y,y,y,y,b,y,
b,b,b,y,y,y,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
])

# Digito 28
digitos.append([
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,b,y,
b,b,b,y,b,b,b,y,
b,y,y,y,b,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
])

# Digito 29
digitos.append([
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,b,y,
b,b,b,y,b,b,b,y,
b,y,y,y,y,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
])

# Digito 30
digitos.append([
l,l,l,l,l,l,l,l,
b,b,b,l,b,b,b,l,
l,l,b,l,b,l,b,l,
b,b,b,l,b,l,b,l,
l,l,b,l,b,l,b,l,
b,b,b,l,b,b,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
])

# Digito 31
digitos.append([
l,l,l,l,l,l,l,l,
b,b,b,l,l,l,b,l,
l,l,b,l,l,b,b,l,
b,b,b,l,l,l,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,l,l,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
])

# Digito 32
digitos.append([
l,l,l,l,l,l,l,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,b,b,b,l,
l,l,b,l,b,l,l,l,
b,b,b,l,b,b,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
])

# Digito 33
digitos.append([
l,l,l,l,l,l,l,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,b,b,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
])


# Digito 34
digitos.append([
l,l,l,l,l,l,l,l,
b,b,b,l,b,l,b,l,
l,l,b,l,b,l,b,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,l,l,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
])

# Digito 35
digitos.append([
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
])

# Digito 36
digitos.append([
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
])

# Digito 37
digitos.append([
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,v,v,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,v,v,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
])

# Digito 38
digitos.append([
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
])

# Digito 39
digitos.append([
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
])

# Digito 40
digitos.append([
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,b,r,b,r,
b,b,b,r,b,r,b,r,
r,r,b,r,b,r,b,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
])

# Digito 41
digitos.append([
r,r,r,r,r,r,r,r,
b,r,b,r,r,r,b,r,
b,r,b,r,r,b,b,r,
b,b,b,r,r,r,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,r,r,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
])

# Digito 42
digitos.append([
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,r,r,b,r,
b,b,b,r,b,b,b,r,
r,r,b,r,b,r,r,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
])

# Digito 43
digitos.append([
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,r,r,b,r,
b,b,b,r,b,b,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
])

# Digito 44
digitos.append([
r,r,r,r,r,r,r,r,
b,r,b,r,b,r,b,r,
b,r,b,r,b,r,b,r,
b,b,b,r,b,b,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,r,r,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
])

# Digito 45
digitos.append([
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,b,r,r,r,
b,b,b,r,b,b,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
])


 



my_lat = 41.1496100	
my_lon = -8.6109900

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

all_stations = get(stations).json()['items']

#Encontrar a estação mais próxima para obter dados precisos RGB


def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
            
    return closest_station
closest_stn = find_closest()
weather = weather + str(closest_stn)
my_weather = get(weather).json()['items']


#WINDSPEED 3
g=wind_speed = my_weather[0]['wind_speed']

#HUMIDITY 4
d=humidity = my_weather[0]['humidity']

#RAINFALL 5
e=rainfall = my_weather[0]['rainfall']

#AIRPRESSURE 6
a=air_pressure = my_weather[0]['air_pressure']

#GROUNDTEMP 1
c=ground_temp = my_weather[0]['ground_temp']

#AMBIENTTEMP 2
b=ambient_temp = my_weather[0]['ambient_temp']

f=((sense.get_temperature_from_humidity()+sense.get_temperature_from_pressure())/2)

i=0

def move_left (event):
    if event.action=='pressed':
        global i
        i = i-1
        print(i)
        print(event)

def move_right (event):
    if event.action=='pressed':
        global i
        i = i+1
        print(i)
        print(event)

sense.stick.direction_right = move_right
sense.stick.direction_left = move_left




#nao esquecer zero e -1
def show_weather():
    selected_value = weather_options.get()
    print(selected_value)
    result = []
    if selected_value == "Air pressure":
        info("Weather",'                                                         '+str(int(round(a,0)))+str(' hPa'))

    elif selected_value == "Ambient Temperature":
        if b<= 15:
            warning= "Warning: Wear warm clothes"
        elif b< 30:
            warning= "Wear normal clothes"
        else:
            warning= "Warning: Use sunscreen"
        info("Weather",'                                                         '+str(int(round(b,0)))+str(' ºC' ) + "\n"+ warning)
        
    elif selected_value == "Ground Temperature":
        if c<= 15:
            warning= "Warning: Wear warm clothes"
        elif c< 30:
            warning= "Wear normal clothes"
        else:
            warning= "Warning: Use sunscreen"
        info("Weather","                                                         "+str(int(round(c,0)))+str(' ºC') + "\n"+ warning)
        
    elif selected_value == "Humidity":
        info("Weather",'                                                         '+str(int(round(d,0)))+str(' %'))
        
    elif selected_value == "Rainfall":
        if e<= 1:
            warning= "Don't worry about the rain"
        elif e< 20:
            warning= "Warning: Be prepared for some rain today"
        else:
            warning= "Warning: Heavy rain! Be prepared"
        info("Weather",'                                                         '+str(int(round(e,0)))+str(' mm') + "\n"+ warning)
        
    elif selected_value == "Room Temperature":
        info("Weather",'                                                         '+str(int(round(f,0)))+str(' ºC'))
        
    elif selected_value == "Wind Speed":
        if g<=15 :
            warning= "Don't worry about the wind"
        elif g< 40:
            warning= "Warning: The wind is a bit strong"
        else:
            warning= "Warning: Don't fly away!"
        info("Weather",'                                                         '+str(int(round(g,0)))+str(' Km/H') + "\n"+ warning)

welcome_message= 0

def threaded_function2():
    global app
    app = App(title="MSHD - Metereologic Sense Hat Device", height= 900, width = 1440)
    global welcome_message

    welcome_message = Text(app, text="Know the weather", size=25, font="Times New Roman", color="blue")

    text_size = Slider(app, command=change_text_size, start=30, end=100)

    weather = Picture(app, image="screen.gif")

    global weather_options
    weather_options = Combo(app, options=["Air pressure", "Ambient Temperature", "Ground Temperature", "Humidity", "Rainfall", "Room Temperature", "Wind Speed"], grid=[0,1], align="left") 

    Run_app = PushButton(app, show_weather, text="select", grid=[3,1], align="left")
    app.display()


def change_text_size(slider_value):
    global welcome_message
    welcome_message.font_size(slider_value)

def threaded_function():
    while True:
        global i
        if i==-1:
            i=6

        if i==7:
            i=0

        while i==0:

            sense.show_message(str(horas))

            t = ((sense.get_temperature_from_humidity()+sense.get_temperature_from_pressure())/2)
            temperatura=int(round(t,0))
            sense.show_message('Room Temp')
            sense.set_pixels(digitos[temperatura])
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']
            
            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0) 
            sleep (5)
            

        while i==1:
            sense.show_message("Ground Temp")
            sense.set_pixels(digitos[int(round(ground_temp,0))])
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']

            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)

            sleep (5)
                

        while i==2:
            sense.show_message("Ambient Temp")
            sense.set_pixels(digitos[int(round(ambient_temp,0))])
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']

            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)

            sleep (5)
           
        
            
        while i==3:
            sense.show_message("Wind Speed")
        
            if wind_speed< 46:
                
                sense.set_pixels(digitos[int(round(wind_speed,0))])
                sleep(5)
            elif wind_speed>45:
                sense.show_message(str(int(round(wind_speed,0))))
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']

            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)

        while i==4:
            sense.show_message("Humidity")
            sense.show_message(str(int(round(humidity,0))))
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']

            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)
              

        while i==5:
            sense.show_message("Rainfall")
        
            if wind_speed< 46:
                
                sense.set_pixels(digitos[int(round(rainfall,0))])
                sleep(5)
            elif wind_speed>45:
                sense.show_message(str(int(round(rainfall,0))))
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']

            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)

        while i==6:
            sense.show_message("Air Pressure")
            sense.show_message(str(int(round(air_pressure,0))))
            x = sense.get_accelerometer_raw()['x']
            y = sense.get_accelerometer_raw()['y']
            z = sense.get_accelerometer_raw()['z']

            x = round(x, 0)
            y = round(y, 0)
            print(y)

            if y == -1:
                sense.set_rotation(180)
                print("rodou")
            elif x == -1:
                sense.set_rotation(90)
            elif x == 1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)
            sleep(1)

        


t1 = Thread(target=threaded_function, args=[])
t2 = Thread(target=threaded_function2, args=[])
t1.start()
t2.start()











   

    

            
        

    
   
        

       
    
        

