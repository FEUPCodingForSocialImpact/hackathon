import pygame
from pygame.locals import *
import datetime
import time
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((1,1))
sense = SenseHat()

sense.clear()

state = 0

global alarm_clock
alarm_clock = "00:00"

alarm_hour = "00"


alarm_minute = "00"


def alarme_show(state):
    if state == 0:
        current_time_hour = datetime.datetime.now().hour

        #converter horas para string
        hour = str(current_time_hour)
        sense.show_message(hour)

        alarme(state, hour)

    elif state == 1:
        current_time_minute = datetime.datetime.now().minute

        #converter minutos para string
        minutes = str(current_time_minute)
        sense.show_message(minutes)

        alarme(state, minutes)
        
    elif state == 2:
        current_time_hour = datetime.datetime.now().hour
        hour = str(current_time_hour)
        sense.clear(0, 255, 0)
        time.sleep(3)
        sense.clear()
        verificar()


def alarme(state, hour):
    hour_count = int(hour)
    minute_count = int(hour)
    while state == 0:
        for event in pygame.event.get():
            print(event)
            if event.type==KEYDOWN and event.key == K_DOWN:
                if hour_count == 0:
                    continue
                else:
                    hour_count -= 1
                    sense.show_message(str(hour_count), scroll_speed = 0.03)

            if event.type==KEYDOWN and event.key == K_UP:
                if hour_count == 24:
                    continue
                else:
                    hour_count += 1
                    
                    sense.show_message(str(hour_count), scroll_speed = 0.03)
                    
            if event.type==KEYDOWN and event.key == K_RETURN:
                state = 1
                sense.clear()
                sense.show_letter(":");
                global alarm_hour
                alarm_hour = str(hour_count)
                time.sleep(0.5)
                sense.clear()
                
                alarme_show(state)
            
    while state == 1:
        for event in pygame.event.get():
            print(event)

            if event.type==KEYDOWN and event.key == K_DOWN:
                if minute_count == 0:
                    continue
                else:
                    minute_count -= 1
                    sense.show_message(str(minute_count), scroll_speed = 0.03)

            if event.type==KEYDOWN and event.key == K_UP:
                if minute_count == 59:
                    minute_count = 0
                    sense.show_message(str(minute_count), scroll_speed = 0.03)
                else:
                    minute_count += 1
                    sense.show_message(str(minute_count), scroll_speed = 0.03)
                            
            if event.type==KEYDOWN and event.key == K_RETURN:
                state = 2
                sense.clear()
                global alarm_minute
                alarm_minute  = str(minute_count)
                global alarm_clock
                alarm_clock = alarm_hour + ":" + alarm_minute
                print (alarm_clock)
                time.sleep(0.5)
                alarme_show(state)

    
def verificar():
    while True:
        current_time_hour = datetime.datetime.now().hour
        hour = str(current_time_hour)

        current_time_minute = datetime.datetime.now().minute
        minutes = str(current_time_minute)

        despertador = hour + ":" + minutes

        if despertador != alarm_clock:
            
            print(despertador)
            print(alarm_clock)
            time.sleep(1)
        
        else:
            break;
        
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)

    pygame.mixer.init()
    pygame.mixer.music.load("Som de campainha   sinal   despertador.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
        
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)

    pygame.mixer.init()
    pygame.mixer.music.load("Som de campainha   sinal   despertador.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

        
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)


    pygame.mixer.init()
    pygame.mixer.music.load("Som de campainha   sinal   despertador.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)
    sense.clear(255, 0, 0)
    time.sleep(0.2)
    sense.clear(0, 0, 255)
    time.sleep(0.2)
    sense.clear(0, 255, 0)
    time.sleep(0.2)

    pygame.mixer.init()
    pygame.mixer.music.load("Som de campainha   sinal   despertador.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
           

alarme_show(state)
