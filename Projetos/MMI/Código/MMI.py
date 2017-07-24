from guizero import App,Combo,Text,CheckBox,ButtonGroup,PushButton,info
from requests import get
import webbrowser
import folium
import os
import matplotlib.pyplot as plt
from dateutil import parser
import MySQLdb

db = MySQLdb.connect("localhost","root","","mmi")
curs =db.cursor()

listadeestacoes = [2278828,751328,519781,2512723]
listlats = [38.598677, 37.258796, 37.031846, 32.76608]
listlons = [-9.096835, -8.290331, -7.839955, -17.215484]
wsnames = ["Colegio Atlantico", "messines","weather-aeffl","weather station"]
with db:

    for ID in listadeestacoes:

        url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/'+str(ID)
        print(url)
        
        station_data = get(url).json()
        
        for impdata in station_data['items']:
            name = impdata['created_by']
            temp = impdata['ground_temp']
            pressure = impdata['air_pressure']
            humidity = impdata['humidity']
            date = impdata['created_on'].split("T")[0] ## não entendi, mas funciona com T, não com :
            
            try:
                curs.execute("INSERT INTO weather1 values(null, '"+str(date)+"', '"+name+"',"+str(temp)+","+str(pressure)+","+str(humidity)+")")
            except:
                pass
    
    curs.execute("""
    UPDATE weather1
    SET temperature = 20
    WHERE abs(temperature) >100
    """)

    

def Humidity_map():

    def colourgrad(minimum, maximum, value):
        minimum, maximum = float(minimum), float(maximum)
        try:
            ratio = 2 * (value-minimum) / (maximum - minimum)
        except:
            ratio = maximum
        l = [51, 255, 255]
        g = [0, 255, 0]
        b = [ 0, 0, 255]
        hexcolour = (0,0,0)
        if value < 70:
            hexcolour = '#%02x%02x%02x' % (g[0],g[1],g[2])

        elif value > 70 and value < 80:
            hexcolour = '#%02x%02x%02x' % (l[0],l[1],l[2])

        elif value > 80:
            hexcolour = '#%02x%02x%02x' % (b[0],b[1],b[2])

        return hexcolour

##
##    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'
##
##    station_data = get(url).json()
##    

    humidity = []
    hmax = 30
    hmin = 100
##    print (station_data)
##    lons = [data['weather_stn_long'] for data in station_data['items']]
##    lats = [data['weather_stn_lat'] for data in station_data['items']]
##    wsnames = [station['weather_stn_name'] for station in station_data['items']]
    for i in range (len(wsnames)):
        curs.execute ("SELECT humidity FROM weather1 WHERE name LIKE '" + wsnames[i] + "'")
        h = int(curs.fetchall()[0][0])
        if h > hmax:
            hmax = h
        if h < hmin:
            hmin = h

        else:
            p = 74
            
        humidity.append(str(h)) 
        
##    for hum in curs.fetchall():
##        h = int(hum[0])
##    
##        if h > hmax:
##            hmax = h
##        if h < hmin:
##            hmin = h
##
##        else:
##            p = 74
##
##        humidity.append(str(h))


    map_ws = folium.Map(location=[37,-8], zoom_start=6)
    for n in range(len(humidity)):
          hcol = colourgrad(hmin, hmax, float(humidity[n]))
          folium.CircleMarker([listlats[n],listlons[n]],
                            radius = 5,
                            popup = wsnames[n]+':'+humidity[n],
                            fill_color = hcol).add_to(map_ws)

    CWD = os.getcwd()
    print("here")
    map_ws.save('osm.html')
    webbrowser.open_new('file://'+CWD+'/'+'osm.html')
    


def Humidity_graphic():
        url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/2512723'


        weather = get(url).json()

        data = weather['items']

        pages = 1

        while 'next' in weather and pages < 9:
            url = weather['next']['$ref']
            print('Fetching{0}'.format(url))
            weather = get(url).json()
            data += weather['items']
            pages += 1

            
        humidity = [record['humidity'] for record in data]
        timestamps = [parser.parse(record['reading_timestamp']) for record in data]
         
        plt.plot(timestamps, humidity)
        plt.ylabel('humidity')
        plt.xlabel('date and time')
        plt.show()


def Temperature_map():
        def colourgrad(minimum, maximum, value):
            minimum, maximum = float(minimum), float(maximum)
            ratio = 2 * (value - minimum) / (maximum - minimum)
            b = [0, 0, 255]
            r = [255, 0, 0]
            y =[255, 255, 0]
        
            if value < 25:
                hexcolour = '#%02x%02x%02x' % (b[0],b[1],b[2])
            elif value > 25 and value < 30:
                hexcolour = '#%02x%02x%02x' % (y[0],y[1],y[2])
            elif value > 30:
                hexcolour = '#%02x%02x%02x' % (r[0],r[1],r[2])

            return hexcolour

##        url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'
##
##        station_data = get(url).json()

        temps = []
        tmax = -100.0
        tmin = 100.0
##        lons = [data['weather_stn_long'] for data in station_data['items']]
##        lats = [data['weather_stn_lat'] for data in station_data['items']]
##        wsnames = [data['weather_stn_name'] for data in station_data['items']]
        for i in range (len(wsnames)):
            curs.execute ("SELECT temperature FROM weather1 WHERE name LIKE '" + wsnames[i] + "'")
            t = int(curs.fetchall()[0][0])
            if t > tmax:
                    tmax = t
            if t < tmin:
                    tmin = t

            else:
                t = 20

            temps.append(str(t))


        map_ws = folium.Map(location=[37,-8], zoom_start=6)
        for n in range(len(temps)):
            hcol = colourgrad(tmin, tmax, float(temps[n]))
            folium.CircleMarker([listlats[n],listlons[n]],
                                radius = 5,
                               popup = wsnames[n]+':'+temps[n],
                               fill_color = hcol).add_to(map_ws)

        CWD = os.getcwd()
        map_ws.save('osm.html')
        webbrowser.open_new('file://'+CWD+'/'+'osm.html')



def Temperature_graphic():
        url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/2512723'


        weather = get(url).json()

        data = weather['items']

        pages = 1

        while 'next' in weather and pages < 9:
            url = weather['next']['$ref']
            print('Fetching{0}'.format(url))
            weather = get(url).json()
            data += weather['items']
            pages += 1

            
        temperatures = [record['ambient_temp'] for record in data]
        timestamps = [parser.parse(record['reading_timestamp']) for record in data]
         
        plt.plot(timestamps, temperatures)
        plt.ylabel('Temperature')
        plt.xlabel('date and time')
        plt.show()



def Pressure_map():
    def colourgrad(minimum, maximum, value):
        minimum, maximum = float(minimum), float(maximum)
        ratio = 2 * (value-minimum) / (maximum - minimum)
        r = [255, 0, 0]
        w = [255, 255, 255]
        b = [ 0, 0, 255]
        hexcolour = (0,0,0)
        if value < 1010:
            hexcolour = '#%02x%02x%02x' % (r[0],r[1],r[2])
            
        elif value >1010 and value < 1015:
            hexcolour = '#%02x%02x%02x' % (b[0],b[1],b[2])
        
        elif value > 1015:
            hexcolour = '#%02x%02x%02x' % (w[0],w[1],w[2])

        return hexcolour


    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'

    station_data = get(url).json()

    pressure = []
    pmax = 900
    pmin = 1100
    lons = [data['weather_stn_long'] for data in station_data['items']]
    lats = [data['weather_stn_lat'] for data in station_data['items']]
    wsnames = [station['weather_stn_name'] for station in station_data['items']]

    for data in station_data['items']:
        if 'air_pressure' in data:
            p = data['air_pressure']
            if p > 1020 or p < 1000:
                p = 1013
            if p > pmax:
                pmax = p
            if p < pmin:
                pmin = p

        else:
            p = 1013

        pressure.append(str(p))




    map_ws = folium.Map(location=[37,-8], zoom_start=6)
    for n in range(len(lons)):
          hcol = colourgrad(pmin, pmax, float(pressure[n]))
          folium.CircleMarker([lats[n],lons[n]],
                            radius = 5,
                            popup = wsnames[n]+':'+pressure[n],
                            fill_color = hcol).add_to(map_ws)

    CWD = os.getcwd()
    map_ws.save('osm.html')
    webbrowser.open_new('file://'+CWD+'/'+'osm.html')
        



def Pressure_graphic():
    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/2512723'


    weather = get(url).json()

    data = weather['items']

    pages = 1

    while 'next' in weather and pages < 9:
        url = weather['next']['$ref']
        print('Fetching{0}'.format(url))
        weather = get(url).json()
        data += weather['items']
        pages += 1

        
    pressure = [record['air_pressure'] for record in data]
    timestamps = [parser.parse(record['reading_timestamp']) for record in data]
     
    plt.plot(timestamps, pressure)
    plt.ylabel('pressure')
    plt.xlabel('date and time')
    plt.show()





    


def do_booking():
    info("Booking", "Loading")
    print( measure_choice.get() )
    print( map_option.get_value() )
    print( graphic_option.get_value() )
    if measure_choice.get()=="Humidity" and map_option.get_value()==True:
        Humidity_map()
    if measure_choice.get()=="Humidity" and graphic_option.get_value()==True:
        Humidity_graphic()
    if measure_choice.get()=="Temperature" and graphic_option.get_value()==True:
        Temperature_graphic()
    if measure_choice.get()=="Temperature" and map_option.get_value()==True:
        Temperature_map()
    if measure_choice.get()=="Pressure" and graphic_option.get_value()==True:
        Pressure_graphic()
    if measure_choice.get()=="Pressure" and map_option.get_value()==True:
        Pressure_map()
        
   

app = App(title="MMI", width=300, height=200, layout="grid")
measure_choice = Combo(app, options=["Pressure", "Humidity", "Temperature"], grid=[0,1], align="left")
film_description = Text(app, text="Which measure?", grid=[0,0], align="left")
map_option = CheckBox(app, text="Map", grid=[1,1], align="left")
graphic_option = CheckBox(app, text="Graphic", grid=[1,2], align="left")

confirmation_button = PushButton(app, command=do_booking, text="confirm", grid=[3,1], align="left")


app.display()
