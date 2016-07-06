from sense_hat import SenseHat
import time
import datetime
sense = SenseHat()
# File: datetime-example-1.py
import pygame
import datetime

now = datetime.datetime(2016, 6, 29, 21, 00, 00)

print now
print repr(now)
print type(now)
print now.year, now.month, now.day
print now.hour, now.minute, now.second
print now.microsecond
type("datetime.datetime")

testing_mode = False
    


sense = SenseHat()
sense.clear()

p = [0,0,0]
b = [255,255,255]

meio = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,

]

fechado = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

fechado1 = [
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

fechado2 = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

 
fechado3 = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]


aberto = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
]

aberto1 = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

aberto2 = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]


aberto3 = [
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
b,b,b,b,b,b,b,b,

]

def opening_half_animation():
    sense.set_pixels(fechado)
    time.sleep(0.5)
    sense.set_pixels(fechado1)
    time.sleep(0.5)
    sense.set_pixels(fechado2)
    time.sleep(0.5)
    sense.set_pixels(fechado3)
    time.sleep(0.5)
    sense.set_pixels(meio)

def opening_animation():
    sense.set_pixels(fechado)
    time.sleep(0.5)
    sense.set_pixels(fechado1)
    time.sleep(0.5)
    sense.set_pixels(fechado2)
    time.sleep(0.5)
    sense.set_pixels(fechado3)
    time.sleep(0.5)
    sense.set_pixels(meio)
    time.sleep(0.5)
    sense.set_pixels(aberto1)
    time.sleep(0.5)
    sense.set_pixels(aberto2)
    time.sleep(0.5)
    sense.set_pixels(aberto3)
    time.sleep(0.5)
    sense.set_pixels(aberto)
    time.sleep(0.5)


def opening_half_2_animation():
    sense.set_pixels(meio)
    time.sleep(0.5)
    sense.set_pixels(aberto1)
    time.sleep(0.5)
    sense.set_pixels(aberto2)
    time.sleep(0.5)
    sense.set_pixels(aberto3)
    time.sleep(0.5)
    sense.set_pixels(aberto)
    time.sleep(0.5)

def closing_half_animation():
    sense.set_pixels(aberto)
    time.sleep(0.5)
    sense.set_pixels(aberto3)
    time.sleep(0.5)
    sense.set_pixels(aberto2)
    time.sleep(0.5)
    sense.set_pixels(aberto1)
    time.sleep(0.5)
    sense.set_pixels(meio)
    time.sleep(0.5)

def closing_animation():
    sense.set_pixels(aberto)
    time.sleep(0.5)
    sense.set_pixels(aberto3)
    time.sleep(0.5)
    sense.set_pixels(aberto2)
    time.sleep(0.5)
    sense.set_pixels(aberto1)
    time.sleep(0.5)
    sense.set_pixels(meio)
    time.sleep(0.5)
    sense.set_pixels(fechado3)
    time.sleep(0.5)
    sense.set_pixels(fechado2)
    time.sleep(0.5)
    sense.set_pixels(fechado1)
    time.sleep(0.5)
    sense.set_pixels(fechado)
    time.sleep(0.5)

def closing_half_2_animation():
    sense.set_pixels(meio)
    time.sleep(0.5)
    sense.set_pixels(fechado3)
    time.sleep(0.5)
    sense.set_pixels(fechado2)
    time.sleep(0.5)
    sense.set_pixels(fechado1)
    time.sleep(0.5)
    sense.set_pixels(fechado)
    time.sleep(0.5)


def manual_mode():
    global current_state
    current_state=0
    
    while True:     
        manual_mode = raw_input("definir estado de abertura:")
        if manual_mode == "abre metade" and current_state == 3:
            current_state = 2
            print ("abrindo metade...")
            pygame.mixer.init()
            pygame.mixer.music.load("abrindo_as_persianas.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            opening_half_animation()
        elif manual_mode == "abre" and current_state == 3:
            current_state = 0
            print ("abrindo...")
            pygame.mixer.init()
            pygame.mixer.music.load("abrindo_as_persianas.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            opening_animation()
        elif manual_mode == "abre" and current_state == 2:
            
            current_state = 0
            print ("abrindo...")
            pygame.mixer.init()
            pygame.mixer.music.load("abrindo_as_persianas.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
            opening_half_2_animation()
        elif manual_mode == "fecha metade" and current_state == 0:
            current_state = 2
            print ("fechando metade...")
            pygame.mixer.init()
            pygame.mixer.music.load("fechando_as_persianas.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            closing_half_animation()
        elif manual_mode == "fecha" and current_state == 0:
            current_state = 3
            print ("fechando...")
            pygame.mixer.init()
            pygame.mixer.music.load("fechando_as_persianas.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            closing_animation()
        elif manual_mode == "fecha" and current_state == 2:
            current_state = 3
            print ("fechando...")
            pygame.mixer.init()
            pygame.mixer.music.load("fechando_as_persianas.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            closing_half_2_animation()
        elif manual_mode == "back":
            hub()
        else:
            print ("erro")

        
def humidade():
    humidity = sense.get_humidity()
    humidity = round(humidity, 1)

    msg = "Humidity = %s" %(humidity)

    print (msg)

def ler_temperatura():
    temperature = round(sense.get_temperature(), 1)
    print ("Temperatura = %s" %(temperature))
    hub()

def get_datetime():
    #print (testing_mode)
    if testing_mode: 
        hh = raw_input("hora:")
        if hh == "back":
            hub()
        else:
            d = datetime.datetime(2016, 6, 29, int(hh), 00, 00)
    else:
        d = datetime.datetime.now()

    return d


def ambiente_mode():
    temp = round(sense.get_temperature(), 1)
    global current_state
    current_state=3
    print temp
    
    while True:
        #temperature=raw_input("Defina temperatura:")
        d = get_datetime()
        hh = d.time().hour
        mm = d.time().minute

        if  hh>=7 and hh<=21:
            print current_state

            if current_state == 3:
                if temp <=18:
                    current_state =0
                    print ("abrindo...")
                    pygame.mixer.init()
                    pygame.mixer.music.load("abrindo_as_persianas.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    opening_animation()
                elif temp > 18 and temp < 24:
                    current_state = 2
                    print ("abrindo metade...")
                    pygame.mixer.init()
                    pygame.mixer.music.load("abrindo_as_persianas.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    opening_half_animation()
                elif temp >= 24:
                    print "já está fechado"
                    current_state = 3             

            elif current_state == 2:
                if temp <= 18:
                    current_state = 0
                    print "abrindo metade..."
                    pygame.mixer.init()
                    pygame.mixer.music.load("abrindo_as_persianas.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    opening_half_2_animation()
                elif temp >18 and temp <24:
                    current_state = 2
                    print "ja esá meio aberto"
                elif temp >= 24:
                    current_state = 3
                    print "fechando..."
                    pygame.mixer.init()
                    pygame.mixer.music.load("fechando_as_persianas.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    closing_half_2_animation()

            elif current_state == 0:
                if temp <= 18:
                    current_state = 0
                    print "já está aberto"
                elif temp >18 and temp <24:
                    current_state = 2
                    print "fechando metade..."
                    pygame.mixer.init()
                    pygame.mixer.music.load("fechando_as_persianas.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    closing_half_animation()
                elif temp >= 24:
                    current_state = 3
                    print ("fechando...")
                    pygame.mixer.init()
                    pygame.mixer.music.load("fechando_as_persianas.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    closing_animation()
                    

            print current_state
            temp=raw_input("defina temperatura:")
            temp=int(temp)

           
            

def hub():
    global testing_mode
    
    print "Selecione o comando pretendido"
    print "Temperatura- mostra a temperatura atual"
    print "Manual- define as persianas para modo manual"
    print "Automático- define as persianas para modo automático"
    menu = raw_input("Comando:")
    if menu == "manual":
        manual_mode()
    elif menu == "automático":
        testing_mode = False #lê hora do sistema
        ambiente_mode()
    elif menu == "temperatura":
        ler_temperatura()
    elif menu == "godmode":
        print "godmode on!"
    elif menu == "relógio":
        testing_mode = True
        ambiente_mode()
    else :
        print "erro"
        hub()

hub()
