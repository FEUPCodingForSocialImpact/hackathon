from sense_hat import SenseHat
import datetime
import time
from pygame.locals import *
import pygame
import threading
import thread

sense = SenseHat()
sense.clear()

pygame.init()
pygame.display.set_mode((1,1))

#temperatura
t = sense.get_temperature()
t_celsius = round(t, 1)
t_celsius += 185
msg = "Temperature " + str(t_celsius)
state = 0
verificar = False



def horas():
    while True:
            current_time_hour = datetime.datetime.now().hour
            current_time_minute = datetime.datetime.now().minute

            #converter horas e minutos para string
            global hour
            hour = str(current_time_hour)

            
            global minutes
            minutes = str(current_time_minute)
            
            #se minutos <10 acrescentar 0

            """
            if current_time_hour < 10:
                hour = "0" + str(current_time_hour)
            """

            if current_time_minute < 10:
                minutes = "0" + str(current_time_minute)    


            sense.show_message(hour +":" + minutes)
            time.sleep(1)
                        
            #relação temperaturas
            if t_celsius > 15:
                e = [0, 255, 0]
                sense.show_message(str(t_celsius), scroll_speed = 0.1, text_colour = e)
                        
                        
            if t_celsius < 15:
                e = [0, 0, 255]
                sense.show_message(str(t_celsius), scroll_speed = 0.1, text_colour = e)
                sense.clear()
     
      
horas()

