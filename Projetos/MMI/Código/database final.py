from requests import get
import MySQLdb
import webbrowser
import folium
import os

db = MySQLdb.connect("localhost","root","","temperature")
curs =db.cursor()

listadeestacoes = [2278828,751328,519781,2512723]

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
                curs.execute("INSERT INTO weather values(null, '"+str(date)+"', '"+name+"',"+str(temp)+","+str(pressure)+","+str(humidity)+")")
            except:
                pass
    curs.execute("""
            UPDATE weather
            SET temperature = 20
            WHERE abs(temperature) >100
            """)
##            i += 1
##            print(str(i) +nome + " " + str(temp) + " " + str(pressure) + " " + str(humidity) + " ")
i = 0
curs.execute ("SELECT * FROM weather")
for reading in curs.fetchall():
    i += 1
    print(str(i)+" "+str(reading[0])+" "+str(reading[1])+" "+str(reading[2])+" "+str(reading[3])+" "+str(reading[4]))
        
db.close()
                




    

 
