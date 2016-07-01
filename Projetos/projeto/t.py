from sense_hat import SenseHat
import datetime
import time 

sense = SenseHat()
sense.clear()

#temperatura
t = sense.get_temperature()
t_celsius = round(t, 1)
t_celsius += 273.15
msg = "Temperature " + str(t_celsius)
verificar = 'true'    

while True:
    print(str(t_celsius))
