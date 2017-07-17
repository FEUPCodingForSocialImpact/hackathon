from sense_hat import SenseHat
from time import sleep
from random import randint
from guizero import App
from guizero import Combo
from guizero import Text
from guizero import CheckBox
from guizero import ButtonGroup
from guizero import PushButton
from guizero import info
from guizero import TextBox
from guizero import Slider
from datetime import datetime, timedelta
from pynput import keyboard


sense = SenseHat()

r = (255, 0, 0) #vermelho
o = (255, 127, 0) #laranja
y = (255, 255, 0) #amarelo
g = (0, 255, 0) #verde
b = (0, 0, 255) #azul
b1=(0,127,255) 
b2=(35,107,142)
b3=(50,153,204)
u = (75, 0, 130) #roxo
p = (159, 0, 255) #rosa
e = (0, 0, 0) #preto
a = (67,66,31) #castanho?
c = (255,255,255) #branco
h = (234,134,86) #rosa estranho


#taça vazia
image1 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
c,c,c,c,c,c,c,c,
c,e,e,e,e,e,e,c,
e,c,e,e,e,e,c,e,
e,e,c,c,c,c,e,e,
e,e,e,e,e,e,e,e,
]

#taça meio cheia
image2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
c,c,c,c,c,c,c,c,
c,e,e,e,e,e,e,c,
e,c,b,b,b,b,c,e,
e,e,c,c,c,c,e,e,
e,e,e,e,e,e,e,e,
]

#taça cheia
image3 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
c,c,c,c,c,c,c,c,
c,b,b,b,b,b,b,c,
e,c,b,b,b,b,c,e,
e,e,c,c,c,c,e,e,
e,e,e,e,e,e,e,e,
]

#taça porca
image4 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
c,c,c,c,c,c,c,c,
c,a,a,a,a,a,a,c,
e,c,a,a,a,a,c,e,
e,e,c,c,c,c,e,e,
e,e,e,e,e,e,e,e,
]

#perigo
image5 = [
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
]

#perigo azul
image6 = [
e,e,e,b,b,e,e,e,
e,e,e,b,b,e,e,e,
e,e,e,b,b,e,e,e,
e,e,e,b,b,e,e,e,
e,e,e,b,b,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,b,b,e,e,e,
e,e,e,b,b,e,e,e,
]

#perigo laranja
image7 = [
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,o,o,e,e,e,
e,e,e,o,o,e,e,e,
]

#perigo verde
image8 = [
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
]

#nada
nada = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

#cruz hospital
cruz = [
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

#certo
certo = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,g,
e,e,e,e,e,e,g,e,
e,e,e,e,e,g,e,e,
g,e,e,e,g,e,e,e,
e,g,e,g,e,e,e,e,
e,e,g,e,e,e,e,e
]

#seta a subir
setacima = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,r,r,r,r,r,e,
r,r,r,r,r,r,r,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

#seta a descer
setabaixo = [
e,e,e,p,p,e,e,e,
e,e,e,p,p,e,e,e,
e,e,e,p,p,e,e,e,
e,e,e,p,p,e,e,e,
p,p,p,p,p,p,p,p,
e,p,p,p,p,p,p,e,
e,e,p,p,p,p,e,e,
e,e,e,p,p,e,e,e
]

#errado
errado = [
r,e,e,e,e,e,e,r,
e,r,e,e,e,e,r,e,
e,e,r,e,e,r,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,r,e,e,r,e,e,
e,r,e,e,e,e,r,e,
r,e,e,e,e,e,e,r
]

#sadsmile
sadsmile = [
e,e,e,e,e,e,e,e,
e,e,e,b,e,b,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,p,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,p,p,p,e,e,
e,e,p,e,e,e,p,e,
e,e,e,e,e,e,e,e,
]

#bed
bed = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,o,o,o,e,
e,c,c,c,c,c,c,e, 
e,c,c,c,c,c,c,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

#quadrado
ball= [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,c,c,c,c,e,e,
    e,e,c,c,c,c,e,e,
    e,e,c,c,c,c,e,e,
    e,e,c,c,c,c,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
]

#água a cair
water = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,b,e,e,e,
    e,e,e,b,e,b,e,e,
    e,e,b,e,e,e,b,e,
    e,e,b,e,e,e,b,e,
    e,e,b,e,e,e,b,e,
    e,e,e,b,b,b,e,e,
    e,e,e,e,e,e,e,e,
    ]

image10 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image11 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,h,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image12 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,h,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image13= [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,h,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image14 =[
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,h,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image15 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,h,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image16 =[
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,h,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image17=[
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,h,e,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image18 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  h,e,e,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image19 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,h,
  e,e,e,e,e,e,e,h,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image20 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,h,e,
  e,e,e,e,e,e,h,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image21= [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,h,e,e,
  e,e,e,e,e,h,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image22 =[
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,h,e,e,e,
  e,e,e,e,h,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image23= [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,h,e,e,e,e,
  e,e,e,h,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image24=[
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,h,e,e,e,e,e,
  e,e,h,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image25=[
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,h,e,e,e,e,e,e,
  e,h,e,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]
image26 = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  h,e,e,e,e,e,e,e,
  h,e,e,e,e,e,e,e,
  h,h,h,h,h,h,h,h,
  h,h,h,h,h,h,h,h,
  ]  

w = [
e,e,e,e,e,e,e,b,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

w1 = [
e,e,e,e,e,e,e,b1,
e,e,e,e,b1,e,b,e,
e,e,e,e,e,b,e,e,
e,e,e,e,e,e,b2,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

w2 = [
e,e,e,e,e,e,e,b3,
e,e,e,e,e,b,b1,e,
e,e,e,e,e,e,b1,e,
e,e,e,b,e,b2,e,e,
e,e,e,e,b,e,b2,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

w3 = [
e,e,e,e,e,e,e,b2,
e,e,e,e,e,e,b2,e,
e,e,e,e,e,b,e,e,
e,e,e,b,e,e,e,e,
e,e,e,e,b2,e,b3,e,
e,e,e,b,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

w4 = [
e,e,e,e,e,e,e,b,
e,e,e,e,b1,e,b3,e,
e,e,e,e,e,e,b,e,
e,e,e,e,b2,e,e,e,
e,e,b1,e,b,e,b1,e,
e,b,e,b,e,e,e,e,
e,e,e,e,b3,e,e,e,
b1,b,e,b,e,e,e,e,
]

w5 = [
e,e,e,e,e,e,e,b,
e,e,e,e,b,e,b,e,
e,e,e,e,e,e,b1,e,
e,e,e,e,b2,e,e,e,
e,e,b,e,b,e,b1,e,
e,b2,e,e,e,e,e,e,
e,e,b,e,e,b2,e,e,
b,b2,e,b3,e,e,e,e,
]


sleep(1)
def game():


    rest = input('Press Enter to start.')
    global t
    t = randint(14,21) #temperatura
    global rt
    rt = randint(1,28)
    global pu
    pu = randint(2,5) #pureza
    global rpu
    rpu = randint(1,7)
    global q
    q = randint(2,7) #quantidade de água
    global rq
    rq = randint(1,7)
    global h
    h = randint(2,5) #higiene
    global rh
    rh = randint(1,7)
    global e
    e = randint(2,5) #exercise
    global re
    re = randint(1,9)
    global f
    f = randint(2,6) #food
    global rf
    rf = randint(1,7)
    sleep(1)
    global score
    score = 0
    global stop
    stop=False

    
    while True:
        print('Your current score is ' + str(score))
        sleep(.5)
        print("PET MENU:")
        if t < 16:
            temp = ' (cold)'
        elif t < 20 and t > 15:
            temp= ' (normal)'
        elif t > 19:
            temp = ' (warm)'
        elif t < 13 or t > 22:
            stop = False

            lis = keyboard.Listener(on_press=on_press)
            lis.start()

            while not stop:
                r1 = randint(0,255)
                r2 = randint(0,255)
                r3 = randint(0,255)
                sense.show_message('Game Over :(  ', text_colour=(r1,r2,r3), scroll_speed = 0.07)
            game()
            
        print("A) Water Temperature: " + str(t) + 'ºC ' + temp)
        if pu == 5 or pu== 4:
            purity = ' clean'
        elif pu == 3 or pu==2:
            purity = ' dirty'
        elif pu==1:
            purity = ' nasty'
        elif pu == 0:
            stop = False

            lis = keyboard.Listener(on_press=on_press)
            lis.start()

            while not stop:
                r1 = randint(0,255)
                r2 = randint(0,255)
                r3 = randint(0,255)
                sense.show_message('Game Over :(  ', text_colour=(r1,r2,r3), scroll_speed = 0.07)

            restartanswer = input('If you wish to play again please write "restart". Otherwise, write "end".')
            if restartanswer == 'restart' or restartanswer == 'r':
                print('Welcome once again, ' + name.get())
                game()
            elif restartanswer == 'end' or restartanswer == 'e':
                print('Thank you for playing. I hope you had a pleasant time.')
                print('Please close this window.')
                # ----------------------------------------------------------------------------
            else:
                while restartanswer != 'restar' or restartanswer != 'end' or restartanswer != 'e' or restartanswer != 'r' or restartanswer != 'I love you':
                    print('I am afraid that is not a valid option.')
                    restartanswer = input('Please choose either "restart" or "end"')
                    if restartanswer == 'restart' or restartanswer == 'r' or restartanswer == 'I love you':
                        print('Welcome once again, ' + name.get())
                        game()
                    elif restartanswer == 'end' or restartanswer == 'e':
                        print('Thank you for playing. I hope you had a pleasant time.')
                        print('Please close this window.')
                        # ----------------------------------------------------------------------------
                    
                    
            
        sleep(.5)
        print("B) Water Purity: " + purity)
        sleep(.5)
        if q == 7 or q==6:
            fullness = ' full'
        elif q == 5 or q==4 or q == 3:
            fullness = ' half full - half empty'
        elif q == 1 or q == 2:
            fullness = ' empty :('
        elif q == 0:
            stop = False

            lis = keyboard.Listener(on_press=on_press)
            lis.start()

            while not stop:
                r1 = randint(0,255)
                r2 = randint(0,255)
                r3 = randint(0,255)
                sense.show_message('Game Over :(  ', text_colour=(r1,r2,r3), scroll_speed = 0.07)
            restartanswer = input('If you wish to play again please write "restart". Otherwise, write "end".')
            if restartanswer == 'restart' or restartanswer == 'r':
                print('Welcome once again, ' + name.get())
                game()
            elif restartanswer == 'end' or restartanswer == 'e':
                print('Thank you for playing. I hope you had a pleasant time.')
                print('Please close this window.')
                # ----------------------------------------------------------------------------
            else:
                while restartanswer != 'restar' or restartanswer != 'end' or restartanswer != 'e' or restartanswer != 'r' or restartanswer != 'I love you':
                    print('I am afraid that is not a valid option.')
                    restartanswer = input('Please choose either "restart" or "end"')
                    if restartanswer == 'restart' or restartanswer == 'r' or restartanswer == 'I love you':
                        print('Welcome once again, ' + name.get())
                        game()
                    elif restartanswer == 'end' or restartanswer == 'e':
                        print('Thank you for playing. I hope you had a pleasant time.')
                        print('Please close this window.')
                        # ----------------------------------------------------------------------------
        print("C) Water Quantity: " + fullness)
        sleep(.5)

        if h == 5:
            hy = ' perfect'
        elif h == 3 or h == 4:
            hy = ' okay'
        elif h == 2:
            hy= ' needing a bath...'
        elif h == 1:
            hy = 'ew, what is this smell?'
        elif h == 0:
            stop = False

            lis = keyboard.Listener(on_press=on_press)
            lis.start()

            while not stop:
                r1 = randint(0,255)
                r2 = randint(0,255)
                r3 = randint(0,255)
                sense.show_message('Game Over :(  ', text_colour=(r1,r2,r3), scroll_speed = 0.07)
            restartanswer = input('If you wish to play again please write "restart". Otherwise, write "end".')
            if restartanswer == 'restart' or restartanswer == 'r':
                print('Welcome once again, ' + name.get())
                game()
            elif restartanswer == 'end' or restartanswer == 'e':
                print('Thank you for playing. I hope you had a pleasant time.')
                print('Please close this window.')
                # ----------------------------------------------------------------------------
            else:
                while restartanswer != 'restar' or restartanswer != 'end' or restartanswer != 'e' or restartanswer != 'r' or restartanswer != 'I love you':
                    print('I am afraid that is not a valid option.')
                    restartanswer = input('Please choose either "restart" or "end"')
                    if restartanswer == 'restart' or restartanswer == 'r' or restartanswer == 'I love you':
                        print('Welcome once again, ' + name.get())
                        game()
                    elif restartanswer == 'end' or restartanswer == 'e':
                        print('Thank you for playing. I hope you had a pleasant time.')
                        print('Please close this window.')
                        # ----------------------------------------------------------------------------
        print ('D) Hygiene: ' + hy)
        sleep(.5)

        if e == 5 or e == 4:
            ex = ' well exercised'
        elif e == 3 or e == 2:
            ex = ' maybe is time to go for a walk?'
        elif e == 1:
            ex = ' extreme need of exercise'
        elif e == 0:
            stop = False

            lis = keyboard.Listener(on_press=on_press)
            lis.start()

            while not stop:
                r1 = randint(0,255)
                r2 = randint(0,255)
                r3 = randint(0,255)
                sense.show_message('Game Over :(  ', text_colour=(r1,r2,r3), scroll_speed = 0.07)
            restartanswer = input('If you wish to play again please write "restart". Otherwise, write "end".')
            if restartanswer == 'restart' or restartanswer == 'r':
                print('Welcome once again, ' + name.get())
                game()
            elif restartanswer == 'end' or restartanswer == 'e':
                print('Thank you for playing. I hope you had a pleasant time.')
                print('Please close this window.')
                # ----------------------------------------------------------------------------
            else:
                while restartanswer != 'restar' or restartanswer != 'end' or restartanswer != 'e' or restartanswer != 'r' or restartanswer != 'I love you':
                    print('I am afraid that is not a valid option.')
                    restartanswer = input('Please choose either "restart" or "end"')
                    if restartanswer == 'restart' or restartanswer == 'r' or restartanswer == 'I love you':
                        print('Welcome once again, ' + name.get())
                        game()
                    elif restartanswer == 'end' or restartanswer == 'e':
                        print('Thank you for playing. I hope you had a pleasant time.')
                        print('Please close this window.')
                        # ----------------------------------------------------------------------------


        print('E) Exercise: ' + ex)
        sleep(.5)
        
        if f == 6 or f == 5:
            fo = ' full'
        elif f == 4 or f == 3:
            fo = ' satisfied'
        elif f == 2 or f == 1:
            fo = ' hungry'
        elif f == 0:
            
            stop = False

            lis = keyboard.Listener(on_press=on_press)
            lis.start()

            while not stop:
                r1 = randint(0,255)
                r2 = randint(0,255)
                r3 = randint(0,255)
                sense.show_message('Game Over :(  ', text_colour=(r1,r2,r3), scroll_speed = 0.07)
            restartanswer = input('If you wish to play again please write "restart". Otherwise, write "end".')
            if restartanswer == 'restart' or restartanswer == 'r':
                print('Welcome once again, ' + name.get())
                game()
            elif restartanswer == 'end' or restartanswer == 'e':
                print('Thank you for playing. I hope you had a pleasant time.')
                print('Please close this window.')
                # ----------------------------------------------------------------------------
            else:
                while restartanswer != 'restar' or restartanswer != 'end' or restartanswer != 'e' or restartanswer != 'r' or restartanswer != 'I love you':
                    print('I am afraid that is not a valid option.')
                    restartanswer = input('Please choose either "restart" or "end"')
                    if restartanswer == 'restart' or restartanswer == 'r' or restartanswer == 'I love you':
                        print('Welcome once again, ' + name.get())
                        game()
                    elif restartanswer == 'end' or restartanswer == 'e':
                        print('Thank you for playing. I hope you had a pleasant time.')
                        print('Please close this window.')
                        # ----------------------------------------------------------------------------


        print('F) Food: ' + fo)
        sleep(.5)
    
    

        action = input("Please choose between A, B, C, D, E and F: ")
        sleep(.5)
        if action == 'A' or action == 'a':
            temperature()

        elif action == 'b' or action == 'B':
            purityfunction()
            
        elif action == 'c' or action == 'C':
            quantityfunction()
            
        elif action == 'D' or action == 'd':
            hygienefunction()

        elif action == 'e' or action == 'E':
            exercisefunction()
            
        elif action == 'f' or action == 'F':
            foodmuffin()
        
        else:
            print('I am afraid that is not a valid answer. Please try again.')

        if t > 19:
            q -= 1
            h -= 1

        if action != 'A' or action != 'a':
            if rt < 10:
                t = t - 1
            elif 9 < rt < 20:
                t = t + 1
            elif 22 < t < 26:
                t = t + 2
            elif 25 < rt < 29:
                t = t - 2

        if action != 'B' or action != 'b' or action == 'a' or action == 'A' or action == 'D' or action == 'd' or action == 'e' or action == 'E':
            if rpu > 4:
                pu -= 1

        if action != 'c' or action != 'C' or action == 'e' or action == 'E' or action == 'f' or action == 'F':
            if rq > 4:
                q -= 1

        if action != 'D' or action != 'd' or action == 'e' or action == 'E':
            if rh > 4:
                h -= 1

        if action != 'e' or action != 'E' or action == 'f' or action == 'F':
            if re > 5:
                e -= 1

        if action != 'f' or action != 'F' or action == 'e' or action == 'E':
            if rf > 4:
                f -= 1


        sleep(2)
        sense.set_pixels(nada)
        print('')

    sense.set_pixels(nada)

def temperature():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop
  

    sleep(1)
    if t < 17:   
        sleep(2)
        sense.show_message("Increasing Temperature", scroll_speed=0.09, text_colour = p)
        setasubindo = [setacima, nada, setacima, nada, setacima, nada, setacima, nada]
        n = 0
        while n <= 7:
            sense.set_pixels(setasubindo[n])
            sleep(.5)
            n += 1
            
        sleep(1)
        sense.set_pixels(certo)
        t = 18
        sleep(3)
        score += 2

        
    elif t < 21 and t > 16: 
        anst = input('The temperature is perfect. However, do you wish to increase or decrease the water\'s temperature? ')
        if anst == 'increase' or anst == 'decrease':
            anst2 = input('How much do you want to ' + anst + ' the water\'s temperature? ')
            if anst2.isdigit():
                if anst == 'increase':
                    sleep(2)
                    sense.show_message("Increasing Temperature", scroll_speed=0.09, text_colour = p)
                    setasubindo = [setacima, nada, setacima, nada, setacima, nada, setacima, nada]
                    n = 0
                    while n <= 7:
                        sense.set_pixels(setasubindo[n])
                        sleep(.5)
                        n += 1
                        
                    sleep(1)
                    sense.set_pixels(certo)
                    t = t + int(anst2)
                    sleep(3)
                    
                elif anst == 'decrease':
                    sleep(2)
                    sense.show_message("Decreasing Temperature", scroll_speed=0.09, text_colour= p)
                    setadescendo = [setabaixo, nada, setabaixo, nada, setabaixo, nada, setabaixo, nada]
                    n = 0
                    while n <= 7:
                        sense.set_pixels(setadescendo[n])
                        sleep(.5)
                        n += 1
                        
                    sleep(1)
                    sense.set_pixels(certo)
                    t = t - int(anst2)
                    sleep(3)
            else:
                while anst2.isdigit() == False:
                    anst2 = input('Please write a number like 2: ')
                    if anst2.isdigit():
                        if anst == 'increase':
                            sleep(2)
                            sense.show_message("Increasing Temperature", scroll_speed=0.09, text_colour = p)
                            setasubindo = [setacima, nada, setacima, nada, setacima, nada, setacima, nada]
                            n = 0
                            while n <= 7:
                                sense.set_pixels(setasubindo[n])
                                sleep(.5)
                                n += 1
                                
                            sleep(1)
                            sense.set_pixels(certo)
                            t = t + int(anst2)
                            sleep(3)
                            
                        elif anst == 'decrease':
                            sleep(2)
                            sense.show_message("Decreasing Temperature", scroll_speed=0.09, text_colour= p)
                            setadescendo = [setabaixo, nada, setabaixo, nada, setabaixo, nada, setabaixo, nada]
                            n = 0
                            while n <= 7:
                                sense.set_pixels(setadescendo[n])
                                sleep(.5)
                                n += 1
                                
                            sleep(1)
                            sense.set_pixels(certo)
                            t = t + int(anst2)
                            sleep(3)
        else:
            while anst != 'increase' or anst != 'decrease':
                anst = input ('Please answer either "increase" or "decrease": ')
                if anst == 'increase' or anst == 'decrease':
                    anst2 = input('How much do you want to ' + anst + ' the water\'s temperature? ')

                    if anst2.isdigit():
                        if anst == 'increase':
                            sleep(2)
                            sense.show_message("Increasing Temperature", scroll_speed=0.09, text_colour = p)
                            setasubindo = [setacima, nada, setacima, nada, setacima, nada, setacima, nada]
                            n = 0
                            while n <= 7:
                                sense.set_pixels(setasubindo[n])
                                sleep(.5)
                                n += 1
                                
                            sleep(1)
                            sense.set_pixels(certo)
                            t = t + int(anst2)
                            sleep(3)
                            
                        elif anst == 'decrease':
                            sleep(2)
                            sense.show_message("Decreasing Temperature", scroll_speed=0.09, text_colour= p)
                            setadescendo = [setabaixo, nada, setabaixo, nada, setabaixo, nada, setabaixo, nada]
                            n = 0
                            while n <= 7:
                                sense.set_pixels(setadescendo[n])
                                sleep(.5)
                                n += 1
                                
                            sleep(1)
                            sense.set_pixels(certo)
                            t = t + int(anst2)
                            sleep(3)
                    else:
                        while anst2.isdigit() == False:
                            anst2 = input('Please write a number like 2: ')
                            if anst2.isdigit():
                                if anst == 'increase':
                                    sleep(2)
                                    sense.show_message("Increasing Temperature", scroll_speed=0.09, text_colour = p)
                                    setasubindo = [setacima, nada, setacima, nada, setacima, nada, setacima, nada]
                                    n = 0
                                    while n <= 7:
                                        sense.set_pixels(setasubindo[n])
                                        sleep(.5)
                                        n += 1
                                        
                                    sleep(1)
                                    sense.set_pixels(certo)
                                    t = t + int(anst2)
                                    sleep(3)
                                    
                                elif anst == 'decrease':
                                    sleep(2)
                                    sense.show_message("Decreasing Temperature", scroll_speed=0.09, text_colour= p)
                                    setadescendo = [setabaixo, nada, setabaixo, nada, setabaixo, nada, setabaixo, nada]
                                    n = 0
                                    while n <= 7:
                                        sense.set_pixels(setadescendo[n])
                                        sleep(.5)
                                        n += 1
                                        
                                    sleep(1)
                                    sense.set_pixels(certo)
                                    t = t + int(anst2)
                                    sleep(3)

        score += 1
                
        
       
    elif t > 20: 
        sleep(2)
        sense.show_message("Decreasing Temperature", scroll_speed=0.09, text_colour= p)
        setadescendo = [setabaixo, nada, setabaixo, nada, setabaixo, nada, setabaixo, nada]
        n = 0
        while n <= 7:
            sense.set_pixels(setadescendo[n])
            sleep(.5)
            n += 1
            
        sleep(1)
        sense.set_pixels(certo)
        t = 18
        sleep(3)
        if rpu < 5:
            pu= pu - 1
        score += 2

        
    
    
    

    

def purityfunction():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop
    if pu == 5 or pu==4:
        print('The water is clean.')
        

    elif pu == 3 or pu ==2 or pu==1:
        sense.set_pixels(image4)
        sleep(3)
        sense.show_message("Cleaning Water", scroll_speed=0.09, text_colour=[20,150,200])
        images = [image4, image3, image4, image3, image4, image3]
        n=0
        while n <= 5:
            sense.set_pixels(images[n])
            sleep(.5)
            n = n + 1

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)
        pu = 5
        score += 1
        

def quantityfunction():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop


    if q == 7 or q==6:
        print('The bowl is already full.')

    elif q == 4 or q==3 or q == 5:
        ansq = input('The bowl is half full. Do you still want to fill it? ' )
        sense.set_pixels(image2)
        sleep(3)

        if ansq == 'yes' or ansq == 'Yes' or ansq == 'sim' or ansq == 'Sim':
            sense.show_message("Filling Bowl", scroll_speed=0.09, text_colour=[20,250,100])
            images = [image2, image3, image2, image3, image2, image3]
            n=0
            while n <= 5:
                sense.set_pixels(images[n])
                sleep(.5)
                n = n + 1

            sleep(1)
            sense.set_pixels(certo)
            sleep(3)
            q = 7
            score += 1

        elif ansq == 'no' or ansq == 'No' or ansq == 'não' or ansq == 'Não' or ansq == 'nao' or ansq == 'Nao':
            print("Okay. Returning to the menu.") 

        else:
            while ansq != 'yes' or ansq != 'no' or ansq != 'No' or ansq != 'Yes':
                print("Please answer either 'yes' or 'no'")
                if ansq == 'yes' or ansq == 'Yes':
                    sense.show_message("Filling Bowl", scroll_speed=0.09, text_colour=[20,250,100])
                    images = [image2, image3, image2, image3, image2, image3]
                    n=0
                    while n <= 5:
                        sense.set_pixels(images[n])
                        sleep(.5)
                        n = n + 1

                    sleep(1)
                    sense.set_pixels(certo)
                    sleep(3)
                    q = 7
                    score += 1
                

                elif answerqq == 'no':
                    print("I'm gonna fill it anyway") 
                    images = [image2, image3, image2, image3, image2, image3]
                    n=0
                    while n <= 5:
                        sense.set_pixels(images[n])
                        sleep(.5)
                        n = n + 1

                    sleep(1)
                    sense.set_pixels(certo)
                    sleep(3)
                    q = 7

    elif q == 1 or q == 2:
        sense.set_pixels(image1)
        sleep(3)
        sense.show_message("Filling Bowl", scroll_speed=0.09, text_colour=[20,250,100])
        images = [image1, image2, image3, image1, image2, image3, image1, image2, image3]
        n=0
        while n <= 8:
            sense.set_pixels(images[n])
            sleep(.5)
            n = n + 1

        q = 7
        sleep(1)
        sense.set_pixels(certo)
        sleep(3)
        score += 2

def hygienefunction():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop
    if h == 5:
        print('I don\'t think I really need another bath...')
    elif h == 4:
        bath = input('Are you sure that i already need another bath? ')
        if bath == 'yes' or bath == 'Yes':
            print('Okay. Here are the rules:')
            print('Firstly, tilt me to the left to turn on the water.')
            print('Then shake me to rub')
            print('Finally, turn on the water again')
            input('When ready, press Enter.')
            print('Please go to the raspberry pi.')
            sleep(3)
            nwater = 0
            while nwater < 15:
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                if 50 < pitch < 90:
                    orientation = sense.get_orientation()
                    pitch = orientation['pitch']
                    waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                    n=0
                    while 50 < pitch < 90 and nwater < 15:
                        orientation = sense.get_orientation()
                        pitch = orientation['pitch']

                        sense.set_pixels(waterfell[n])
                        sleep(0.1)
                        n+=1 
                        nwater = nwater + 1

                else:
                         sense.set_pixels(nada)

            sleep(1)
            sense.set_pixels(certo)
            sleep(3)

            

            acceleration =sense.get_accelerometer_raw()
            x=acceleration["x"]
            y=acceleration['y']
            z=acceleration['z']

            x=abs(x)
            y=abs(y)
            z=abs(z)


            na=0

            while na<15:
                acceleration =sense.get_accelerometer_raw()
                x=acceleration["x"]
                y=acceleration['y']
                z=acceleration['z']

                x=abs(x)
                y=abs(y)
                z=abs(z)

                while (x>1 or y>1 or z>1) and na<15 :
                    acceleration =sense.get_accelerometer_raw()
                    x=acceleration["x"]
                    y=acceleration['y']
                    z=acceleration['z']

                    x=abs(x)
                    y=abs(y)
                    z=abs(z)
                    
                    sense.set_pixels(ball)
                    sleep(0.2)
                    sense.set_pixels(nada)
                    sleep(0.2)
                    na = na + 1

            sleep(1)
            sense.set_pixels(certo)
            sleep(3)


            nwater = 0
            while nwater < 15:
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                if 50 < pitch < 90:
                    orientation = sense.get_orientation()
                    pitch = orientation['pitch']
                    waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                    n=0
                    while 50 < pitch < 90 and nwater < 15:
                        orientation = sense.get_orientation()
                        pitch = orientation['pitch']

                        sense.set_pixels(waterfell[n])
                        sleep(0.1)
                        n+=1 
                        nwater = nwater + 1

                else:
                         sense.set_pixels(nada)

            sleep(1)
            sense.set_pixels(certo)
            sleep(3)
            h = 5
            score += 2
            

        elif bath == 'no' or bath == 'No':
            print('You lazy human...')
            if rpu < 5:
                pu= pu - 1
        else:
            while bath != 'yes' or bath != 'Yes' or bath != 'no' or bath != 'No':
                bath = input('Please write either "yes" or "no": ')
                if bath == 'yes' or bath == 'Yes':
                    print('Okay. Here are the rules: ')
                    print('Firstly, tilt me to the left to turn on the water.')
                    print('Then shake me to rub')
                    print('Finally, turn on the water again')
                    input('When ready, press Enter.')
                    print('Please go to the raspberry pi.')
                    sleep(3)
                    nwater = 0
                    while nwater < 15:
                        orientation = sense.get_orientation()
                        pitch = orientation['pitch']
                        if 50 < pitch < 90:
                            orientation = sense.get_orientation()
                            pitch = orientation['pitch']
                            waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                            n=0
                            while 50 < pitch < 90 and nwater < 15:
                                orientation = sense.get_orientation()
                                pitch = orientation['pitch']

                                sense.set_pixels(waterfell[n])
                                sleep(0.1)
                                n+=1 
                                nwater = nwater + 1

                        else:
                                 sense.set_pixels(nada)

                    sleep(1)
                    sense.set_pixels(certo)
                    sleep(3)

                    

                    acceleration =sense.get_accelerometer_raw()
                    x=acceleration["x"]
                    y=acceleration['y']
                    z=acceleration['z']

                    x=abs(x)
                    y=abs(y)
                    z=abs(z)


                    na=0

                    while na<20:
                        acceleration =sense.get_accelerometer_raw()
                        x=acceleration["x"]
                        y=acceleration['y']
                        z=acceleration['z']

                        x=abs(x)
                        y=abs(y)
                        z=abs(z)

                        while (x>1 or y>1 or z>1) and na<20 :
                            acceleration =sense.get_accelerometer_raw()
                            x=acceleration["x"]
                            y=acceleration['y']
                            z=acceleration['z']

                            x=abs(x)
                            y=abs(y)
                            z=abs(z)
                            
                            sense.set_pixels(ball)
                            sleep(0.2)
                            sense.set_pixels(nada)
                            sleep(0.2)
                            na = na + 1

                    sleep(1)
                    sense.set_pixels(certo)
                    sleep(3)


                    nwater = 0
                    while nwater < 15:
                        orientation = sense.get_orientation()
                        pitch = orientation['pitch']
                        if 50 < pitch < 90:
                            orientation = sense.get_orientation()
                            pitch = orientation['pitch']
                            waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                            n=0
                            while 50 < pitch < 90 and nwater < 15:
                                orientation = sense.get_orientation()
                                pitch = orientation['pitch']

                                sense.set_pixels(waterfell[n])
                                sleep(0.1)
                                n+=1 
                                nwater = nwater + 1

                        else:
                                 sense.set_pixels(nada)

                    sleep(1)
                    sense.set_pixels(certo)
                    sleep(3)
                    h = 5
                    score += 2

                elif bath == 'no' or bath == 'No':
                    print('You lazy human...')
                   
                    if rpu < 5:
                        pu= pu - 1
                        
    elif h == 3 or h == 2:
        print('Okay. Here are the rules:')
        print('Firstly, tilt me to the left to turn on the water.')
        print('Then shake me to rub')
        print('Finally, turn on the water again')
        input('When ready, press Enter.')
        print('Please go to the raspberry pi.')
        nwater = 0
        while nwater < 15:
            orientation = sense.get_orientation()
            pitch = orientation['pitch']
            if 50 < pitch < 90:
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                n=0
                while 50 < pitch < 90 and nwater < 15:
                    orientation = sense.get_orientation()
                    pitch = orientation['pitch']

                    sense.set_pixels(waterfell[n])
                    sleep(0.1)
                    n+=1 
                    nwater = nwater + 1

            else:
                     sense.set_pixels(nada)

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)

        

        acceleration =sense.get_accelerometer_raw()
        x=acceleration["x"]
        y=acceleration['y']
        z=acceleration['z']

        x=abs(x)
        y=abs(y)
        z=abs(z)


        na=0

        while na<30:
            acceleration =sense.get_accelerometer_raw()
            x=acceleration["x"]
            y=acceleration['y']
            z=acceleration['z']

            x=abs(x)
            y=abs(y)
            z=abs(z)

            while (x>1 or y>1 or z>1) and na<30 :
                acceleration =sense.get_accelerometer_raw()
                x=acceleration["x"]
                y=acceleration['y']
                z=acceleration['z']

                x=abs(x)
                y=abs(y)
                z=abs(z)
                
                sense.set_pixels(ball)
                sleep(0.2)
                sense.set_pixels(nada)
                sleep(0.2)
                na = na + 1

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)
        


        nwater = 0
        while nwater < 15:
            orientation = sense.get_orientation()
            pitch = orientation['pitch']
            if 50 < pitch < 90:
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                n=0
                while 50 < pitch < 90 and nwater < 15:
                    orientation = sense.get_orientation()
                    pitch = orientation['pitch']

                    sense.set_pixels(waterfell[n])
                    sleep(0.1)
                    n+=1 
                    nwater = nwater + 1

            else:
                     sense.set_pixels(nada)

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)

        if rpu < 5:
            pu= pu - 1
        h = 5
        score += 3

    elif h == 1:
        nwater = 0
        while nwater < 20:
            orientation = sense.get_orientation()
            pitch = orientation['pitch']
            if 50 < pitch < 90:
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                n=0
                while 50 < pitch < 90 and nwater < 20:
                    orientation = sense.get_orientation()
                    pitch = orientation['pitch']

                    sense.set_pixels(waterfell[n])
                    sleep(0.1)
                    n+=1 
                    nwater = nwater + 1

            else:
                     sense.set_pixels(nada)

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)

        

        acceleration =sense.get_accelerometer_raw()
        x=acceleration["x"]
        y=acceleration['y']
        z=acceleration['z']

        x=abs(x)
        y=abs(y)
        z=abs(z)


        na=0

        while na<40:
            acceleration =sense.get_accelerometer_raw()
            x=acceleration["x"]
            y=acceleration['y']
            z=acceleration['z']

            x=abs(x)
            y=abs(y)
            z=abs(z)

            while (x>1 or y>1 or z>1) and na<40 :
                acceleration =sense.get_accelerometer_raw()
                x=acceleration["x"]
                y=acceleration['y']
                z=acceleration['z']

                x=abs(x)
                y=abs(y)
                z=abs(z)
                
                sense.set_pixels(ball)
                sleep(0.2)
                sense.set_pixels(nada)
                sleep(0.2)
                na = na + 1

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)


        nwater = 0
        while nwater < 20:
            orientation = sense.get_orientation()
            pitch = orientation['pitch']
            if 50 < pitch < 90:
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                waterfell = [w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4,w,w1,w2,w3,w4]
                n=0
                while 50 < pitch < 90 and nwater < 20:
                    orientation = sense.get_orientation()
                    pitch = orientation['pitch']

                    sense.set_pixels(waterfell[n])
                    sleep(0.1)
                    n+=1 
                    nwater = nwater + 1

            else:
                     sense.set_pixels(nada)

        sleep(1)
        sense.set_pixels(certo)
        sleep(3)


        h = 5
        if rpu < 5:
            pu= pu - 1

        score += 4

def exercisefunction():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop
    if e == 5 or e == 4:
        print('I\'m to tired to go for a walk again.')
    elif e == 3 or e == 2:
        print('Again? okay... ')
        sleep(1)
        print('You are playing this game because I am getting fat, and I do not like to be fat.')
        sleep(1)
        print('Therefore, you better move that joystick upwards to make me jump all the obstacles until I am slim again.')
        sleep(1)
        print('The more obstacles you jump, the bigger the score you get.')
        sleep(1)
        input('Press Enter when ready')
        print('Now go to the raspberry pi.')
        
        sleep(3)
        
        jogoexercise()

        if rpu < 5:
            pu= pu - 1
        q -= 1
        if rh < 5:
            h -= 1
        if rf < 5:
            f -= 1

        

    elif e == 1:
        print('Let\'s go!')
        sleep(1)
        print('You are playing this game because I am getting fat, and I do not like to be fat.')
        sleep(1)
        print('Therefore, you better move that joystick upwards to make me jump all the obstacles until I am slim again.')
        sleep(1)
        print('The more obstacles you jump, the bigger the score you get.')
        sleep(1)
        input('Press Enter when ready')
        print('Now go to the raspberry pi.')
        
        
        sleep(3)
        jogoexercise()
        
        

        if rpu < 5:
            pu= pu - 1
        q -= 2
        if rh < 5:
            h -= 2
        elif rh > 4:
            h -= 1

        if rf < 5:
            f -= 2
        elif rf > 4:
            f -= 1

        

def foodmuffin():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop
    x, y = 0, 0
    if f == 6:
        print('Oh! I can\'t eat anything!')
    elif f == 4 or f == 5:
        print('I am ready to eat!')
        sleep(1)
        print('In this game you will have to use the joystick to move around the white pixel and catch all the food (red dots).')
        sleep(1)
        print('You will have to play until I am satisfied. The faster you are catching all the food, the better.')
        sleep(1)
        input('Press Enter when ready and go to the raspberry pi.')

        foodfunction()
        
        q -= 1
        if rh > 4:
            h -= 1
        
        
          
    elif f == 2 or f == 3:
        print('I am ready to eat!')
        sleep(1)
        print('In this game you will have to use the joystick to move around the white pixel and catch all the food (red dots).')
        sleep(1)
        print('You will have to play until I am satisfied. The faster you are catching all the food, the better.')
        sleep(1)
        input('Press Enter when ready and go to the raspberry pi.')
        
        foodfunction()
        
        q -= 1
        h -= 1
        if re > 4:
            e -= 1

        
        
    elif f == 1:
        print('yeahh! I was soooo hungry!')
        sleep(1)
        print('In this game you will have to use the joystick to move around the white pixel and catch all the food (red dots).')
        sleep(1)
        print('You will have to play until I am satisfied. The faster you are catching all the food, the better.')
        sleep(1)
        input('Press Enter when ready and go to the raspberry pi.')

        foodfunction()

        q -= 2
        if rh < 5:
            h -= 2
        elif rh > 4:
            h -= 1

        if re < 6:
            e -= 1

        

def jogoexercise():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global score
    global stop
    x, y = 2, 5 
    x1 = 7
    sense.set_pixels(image10)
    sense.set_pixel(x, y, (255,255,255))
    jump=0
    maxjumps = 20
    numjumps = 1


    while numjumps <= maxjumps:
        if numjumps % 5 == 0:
            y1 = randint(4,5)
            for event in sense.stick.get_events():
                sense.set_pixel(x, y, (255,255,255))
                
                if event.action == 'pressed' and event.direction == 'up':
                  if y > 0:
                    y -= 1
                    sense.set_pixel(x, y + 1, (0,0,0))
                   
                elif event.action == 'pressed' and event.direction == 'down':
                  if y < 5:
                    y += 1
                    sense.set_pixel(x, y - 1, (0,0,0))
                    

               
            if y1==5:
                obstaculobaixo = [image11,image12,image13,image14,image15,image16,image17,image18]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculobaixo[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y-1, (0,0,0))

                    sleep(0.11)
                    n = n + 1
                    if y == 4 and n == 5:
                        jump += 1
                        
                    if n == 6:
                        y=5

            
                        
            elif y1 == 4:
                obstaculoalto = [image19,image20,image21,image22,image23,image24,image25,image26]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculoalto[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y - 1, (0,0,0))

                    sleep(0.25)
                    n = n +1
                    if y==3 and n==5:
                        jump += 1
                    if n==6:
                        y=5

            numjumps += 1

        elif  numjumps % 2 == 0:
            y1 = randint(4,5)
            for event in sense.stick.get_events():
                sense.set_pixel(x, y, (255,255,255))
                
                if event.action == 'pressed' and event.direction == 'up':
                  if y > 0:
                    y -= 1
                    sense.set_pixel(x, y + 1, (0,0,0))
                   
                elif event.action == 'pressed' and event.direction == 'down':
                  if y < 5:
                    y += 1
                    sense.set_pixel(x, y - 1, (0,0,0))
                    

               
            if y1==5:
                obstaculobaixo = [image11,image12,image13,image14,image15,image16,image17,image18]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculobaixo[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y-1, (0,0,0))

                    sleep(0.15)
                    n = n + 1
                    if y == 4 and n == 5:
                        jump += 1
                        
                    if n == 6:
                        y=5
                        
            elif y1 == 4:
                obstaculoalto = [image19,image20,image21,image22,image23,image24,image25,image26]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculoalto[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y - 1, (0,0,0))

                    sleep(0.20)
                    n = n +1
                    if y==3 and n==5:
                        jump += 1
                    if n==6:
                        y=5

        elif numjumps % 2 == 0:
            y1 = randint(4,5)
            for event in sense.stick.get_events():
                sense.set_pixel(x, y, (255,255,255))
                
                if event.action == 'pressed' and event.direction == 'up':
                  if y > 0:
                    y -= 1
                    sense.set_pixel(x, y + 1, (0,0,0))
                   
                elif event.action == 'pressed' and event.direction == 'down':
                  if y < 5:
                    y += 1
                    sense.set_pixel(x, y - 1, (0,0,0))
                    

               
            if y1==5:
                obstaculobaixo = [image11,image12,image13,image14,image15,image16,image17,image18]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculobaixo[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y-1, (0,0,0))

                    sleep(0.15)
                    n = n + 1
                    if y == 4 and n == 5:
                        jump += 1
                        
                    if n == 6:
                        y=5
                        
            elif y1 == 4:
                obstaculoalto = [image19,image20,image21,image22,image23,image24,image25,image26]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculoalto[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y - 1, (0,0,0))

                    sleep(0.20)
                    n = n +1
                    if y==3 and n==5:
                        jump += 1
                    if n==6:
                        y=5
        else:
            y1 = randint(4,5)
            for event in sense.stick.get_events():
                sense.set_pixel(x, y, (255,255,255))
                
                if event.action == 'pressed' and event.direction == 'up':
                  if y > 0:
                    y -= 1
                    sense.set_pixel(x, y + 1, (0,0,0))
                   
                elif event.action == 'pressed' and event.direction == 'down':
                  if y < 5:
                    y += 1
                    sense.set_pixel(x, y - 1, (0,0,0))
                    

               
            if y1==5:
                obstaculobaixo = [image11,image12,image13,image14,image15,image16,image17,image18]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculobaixo[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y-1, (0,0,0))

                    sleep(0.25)
                    n = n + 1
                    if y == 4 and n == 5:
                        jump += 1
                        
                    if n == 6:
                        y=5
                        
            elif y1 == 4:
                obstaculoalto = [image19,image20,image21,image22,image23,image24,image25,image26]
                n=0
                while n<=7:
                    sense.set_pixels(obstaculoalto[n])
                    sense.set_pixel(x, y, (255,255,255))
                    for event in sense.stick.get_events():
                        sense.set_pixel(x, y, (255,255,255))

                        if event.action == 'pressed' and event.direction == 'up':
                            if y > 0:
                                y -= 1
                                sense.set_pixel(x, y + 1, (0,0,0))

                        elif event.action == 'pressed' and event.direction == 'down':
                            if y < 5:
                                y += 1
                                sense.set_pixel(x, y - 1, (0,0,0))

                    sleep(0.15)
                    n = n +1
                    if y==3 and n==5:
                        jump += 1
                    if n==6:
                        y=5

            

        numjumps += 1
                    
    if numjumps > maxjumps:
        if jump > 10:
            sense.show_message('Clear!', scroll_speed = 0.09, text_colour = (255,255,255))
            print(name.get() + ', you scored ' + str(jump) + '/20 in this minigame.')
        elif jump < 11:
            sense.show_message('End', scroll_speed = 0.09, text_colour = (255, 100, 0))
            print(name.get() + ', you scored ' + str(jump) + '/20 in this minigame.')
            print('Unfortunately, it wasn\'t enough to decrease my necessity to exercise...')

    if jump == 20:
        e = 5
        score += 5
    elif 14 < jump < 20:
        e = 4
        
        score += 4
    elif 10 < jump < 15:
        e = 3
        score += 3

def foodfunction():
    global t
    global rt
    global pu 
    global rpu
    global q
    global rq
    global h
    global rh
    global e
    global re
    global f
    global rf
    global stop
    global score
    x, y = 0, 0   
    sleep(3)
    x1 = randint(0,7)
    y1 = randint(0,7)
    bola = 1
    sense.set_pixels(nada)
    sense.set_pixel(x1,y1, r)
    food = 1
    elapsed = timedelta(seconds=0)
    now1 = datetime.now()
    time1 = '%s' % (now1.second)
    
    while food <= 10:
        for event in sense.stick.get_events():
            sense.set_pixel(x, y, (255,255,255))
        
            if event.action == 'pressed' and event.direction == 'up':
                if y > 0:
                    y -= 1
                    sense.set_pixel(x, y + 1, (0,0,0))
                    bola += 1
            elif event.action == 'pressed' and event.direction == 'down':
                if y < 7:
                    y += 1
                    sense.set_pixel(x, y - 1, (0,0,0))
                    bola += 1
            elif event.action == 'pressed' and event.direction == 'right':
                if x < 7:
                    x += 1
                    sense.set_pixel(x-1, y, (0,0,0))
                    bola += 1
            elif event.action == 'pressed' and event.direction == 'left':
                if x > 0:
                    x -=1
                    sense.set_pixel(x+1, y, (0,0,0))
                    bola += 1

        if x==x1 and y==y1:
            food += 1
            x1 = randint(0,7)
            y1 = randint(0,7)
            sense.set_pixel(x1, y1, r)
            bola=1  

        if bola > 18:
            bola=1
            x1 = randint(0,7)
            y1 = randint(0,7)
            sense.set_pixel(x1, y1, r)
   

    if food > 10:
        now2 = datetime.now()
        time2 = '%s' % (now2.second)
        elapsed = int(time2) - int(time1)
        if elapsed < 50:
            print(name.get() + ', you completed this minigame in ' + str(elapsed) + ' seconds')
            sleep(1.5)
            sense.show_message('Clear!', scroll_speed = 0.09, text_colour = (255,255,255))
        elif elapsed > 49:
            sense.show_message('End', scroll_speed = 0.09, text_colour = (255, 100, 0))
            print(name.get() + ', you took too long.')
            print('My hunger will not decrease.')

            
    if elapsed < 17:
        f = 6
        score += 5
    elif 16 < elapsed < 20:
        f = 5
        score += 4
    elif 19 < elapsed < 25:
        f = 4
        score += 3
    elif 24 < elapsed < 30:
        f = 3
        score += 2

def on_press(key):
    global stop
    if key == keyboard.Key.enter:
        stop = True
        return False


def noyes():
    global yesno_choice
    if yesno_choice.get()=="Y":                         
        hjk=Text(app,text= "Your goal in this game is to take care of me while having fun!",grid=[19,1], align="left")
        hjm=Text(app, text= "You will have to pay attention to all my status and clear some games to rise those status." ,grid =[21,1], align='left')
        hfk= Text(app, text= "Depending on your performance, you will achieve different scores.",grid=[23,1], align='left')
        hjl=Text(app,text= "Be careful! If one of those status reaches the lowest possible level I die and you lose the game.",grid=[25,1], align="left")
        dgh= Text(app, text = 'During the game, you will have to take action both in the shell and rasperry pi.', grid=[27,1], align='left')
    elif yesno_choice.get()=="N":
        print(" ")
    update_text = PushButton(app, command = close_window, text= " START GAME!" ,grid=[29,1], align="left")
    
        
def saname():
    welcome_message.set("Hi " + name.get() + ". I am rPet, your new friend!")
    hjp=Text(app,text= "Do you wish to read the instructions?",grid=[13,1], align="left")
    global yesno_choice
    yesno_choice = ButtonGroup(app, options=[ ["Yes", "Y"], ["No", "N"]],grid=[15,1],selected="N", align="left")
    update_text = PushButton(app, command = noyes, text= " CONTINUE" ,grid=[17,1], align="left"
                             )

def close_window():
    app.destroy()
    
    
       
app = App(title="rPet", width=750, height=1000, layout= "grid")

welcome_message = Text(app,text="Welcome! What is your name?", size=30, font="Times New Roman", color = "black", grid=[0,1], align="left")
name = TextBox(app, grid=[5,1], align="left")
update_text = PushButton(app, command = saname, text= " NEXT" ,grid=[7,1], align="left")


        
app.display()

game()




