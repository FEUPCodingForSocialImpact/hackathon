
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
done=True
pixel_list = sense.get_pixels()
sense.clear()

##BARRA AZUL
pontos_bot=0
pontos_eu=0
o, j = 3, 0 
v, r = 4, 0
c, d = 5, 0
p, l = 4, 4
x, y = 3, 7
w, z = 4, 7
a, b = 5, 7


def barrabot():
    global v,z,o,j,c,d, crescer
    print("ciclo")   
    if c==2:
        crescer=True
    if c== 7:
        crescer= False
    if crescer:
        sense.set_pixel(c,d, [0, 0,0])
        c += 1
        sense.set_pixel(c,d, [0, 0,250])

        sense.set_pixel(v,r, [0, 0,0])
        v += 1
        sense.set_pixel(v,r, [0, 0,250])

        sense.set_pixel(o,j, [0, 0,0])    
        o += 1
        sense.set_pixel(o,j, [0, 0,250])
    
##        sleep(0.1)
    if not crescer:
            sense.set_pixel(o,j, [0, 0,0])    
            o -= 1
            sense.set_pixel(o,j, [0, 0,250]) 
            
            v -= 1
            sense.set_pixel(v,r, [0, 0,250])
            
            sense.set_pixel(c,d, [0, 0,0])
            c -= 1
            sense.set_pixel(c,d, [0, 0,250])
           ##            sleep(5)
##BARRA ROSA
def barra():
    global x,y,w,z,a,b,c,d
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, [255, 0, 100])
        if event.action == 'pressed' and event.direction == 'right':
            sense.set_pixel(x,y, [0, 0,0])            

            if x <= 4:
               x += 1                            
        if event.action == 'pressed' and event.direction == 'left':
            sense.set_pixel(x,y, [0, 0,0])            

            if x >= 1:
               x -= 1
        sense.set_pixel(w, z, [255, 0, 100])
        if event.action == 'pressed' and event.direction == 'right':
            sense.set_pixel(w,z, [0, 0,0])

            if w <= 5:
               w += 1      
        if event.action == 'pressed' and event.direction == 'left':
            sense.set_pixel(w,z, [0, 0,0])

            if w >= 2:
               w -= 1
        sense.set_pixel(a, b, [255, 0, 100])
        if event.action == 'pressed' and event.direction == 'right':
            sense.set_pixel(a,b, [0, 0,0])

            if a <= 6:
               a += 1       
        if event.action == 'pressed' and event.direction == 'left':
            sense.set_pixel(a,b, [0, 0,0])

            if a >= 3:
               a -= 1
while done:

    sense.set_pixel(3,0, [0, 0, 255])
    sense.set_pixel(4,0, [0, 0, 255])
    sense.set_pixel(5,0, [0, 0, 255])

    sense.set_pixel(3,7, [255, 0, 100])
    sense.set_pixel(4,7, [255, 0, 100])
    sense.set_pixel(5,7, [255, 0, 100])

    sense.set_pixel(4,4, [255, 255, 255])
    sleep(2)

    sense.show_message( "PRESS" , scroll_speed = 0.05 )

#joystick data request
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        
#joystick pressed jogo começa
        if event.action == 'pressed':
            sense.clear()
            sleep (1)
            sense.show_message( "GO" , scroll_speed = 0.05, text_colour=[16, 183, 7] )
            sleep(1)
            done=False
            break

def ballesq():
    global p,x, ball_esq  
    if x>=0:
        p += ball_esq

#movimento bolinha
def movbola():
    global p, l, c, v, o, x, w, a, subir, speed, ball_esq, pontos_eu, pontos_bot
    print("ciclo")
    if l==1:
        subir=False
        if o == p:
            ball_esq = 1
            speed=speed*0.5
        if c == p:
            ball_esq = -1
            speed=speed*0.5
        if v == p:
            ball_esq = 0
            speed=speed*0.5

        if not (c == p or v == p or o == p):
            pontos_eu += 1
            sense.show_message(str(pontos_eu)+"-"+str(pontos_bot), scroll_speed = 0.05, text_colour=[255, 128, 0])
            speed=0.5
            sense.set_pixel(x,y, [0, 0,0])
            sense.set_pixel(w,z, [0, 0,0])
            sense.set_pixel(a,b, [0, 0,0])
            sense.set_pixel(x,y, [255, 0, 100])
            sense.set_pixel(w,z, [255, 0, 100])
            sense.set_pixel(a,b, [255, 0, 100])
##
##        else:
##            speed=speed*0.5
##        if v == p:
##            ball_esq = 0
##        if p == o:
##            ball_esq = 1
##        if p == c:
##            ball_esq = -1
    
            
            
    if l== 6:
        subir= True
        if x == p:
            ball_esq = -1
            speed=speed*0.5
        if w == p:
            ball_esq = 0
            speed=speed*0.5
        if a == p:
            ball_esq = 1
            speed=speed*0.5
        if not (x == p or a == p or w == p):
            pontos_bot += 1
            sense.show_message(str(pontos_eu)+"-"+str(pontos_bot), scroll_speed = 0.05, text_colour=[255, 128, 0])
            speed=0.5
            sleep(0.5)
            sense.set_pixel(x,y, [0, 0,0])
            sense.set_pixel(w,z, [0, 0,0])
            sense.set_pixel(a,b, [0, 0,0])
            sense.set_pixel(x,y, [255, 0, 100])
            sense.set_pixel(w,z, [255, 0, 100])
            sense.set_pixel(a,b, [255, 0, 100])
##        else:
##            speed=speed*0.5
##            if v == p:
##                ball_esq = 0
##            if p == o:
##                ball_esq = 1
##            if p == c:
##                ball_esq = -1
            
            
def pintarbola():
    global p,l,ball_esq,speed, esquerda
    print("pintarbola ", p, " ", l, " ", ball_esq)
    # faz a bola ir para cima e para baixo    
    if subir:
            sense.set_pixel(p,l, [0, 0,0])
            l -= 1
            if (esquerda and ball_esq == 1) or (not esquerda and ball_esq == -1):
                p -= ball_esq
            if (not esquerda and ball_esq == 1) or (esquerda and ball_esq == -1):
                p += ball_esq
            #sense.set_pixel(p, l, [0, 0,0])
            sense.set_pixel(p,l, [255,255,255])
            sleep(speed)

    if not subir:
            sense.set_pixel(p,l, [0, 0,0])    
            l += 1
            if (esquerda and ball_esq == 1) or (not esquerda and ball_esq == -1):
                p -= ball_esq
            if (not esquerda and ball_esq == 1) or (esquerda and ball_esq == -1):
                p += ball_esq
            sense.set_pixel(p,l, [255, 255,255]) 
            sleep(speed)

#movimento bolinha direcoes
def movbola1():
    global p, l, c, v, o, x, w, a, subir, speed, esquerda
    print("ciclo")
    if p==0:
        esquerda=False
        print("esquerda falso")
            
            
    if p==7:
        esquerda= True
        print("esquerda true")

            
             
    # faz a bola ir para cima e para baixo    
##    if esquerda:
##            sense.set_pixel(p,l, [0, 0,0])
##            p -= 1
##            #sense.set_pixel(p, l, [0, 0,0])
##            sense.set_pixel(p,l, [255,255,255])
##            sleep(speed)
##        
##            
##
##    if not esquerda:
##            sense.set_pixel(p,l, [0, 0,0])    
##            p += 1
##            sense.set_pixel(p,l, [255, 255,255])
##            sleep(speed)


def startagain():
    global pontos_eu, pontos_bot
    if pontos_bot >= 5:
        sense.show_message("You Lost", scroll_speed = 0.05)
        sense.clear()
        pontos_eu=0
        pontos_bot=0
        sense.set_pixel(x,y, [0, 0,0])
        sense.set_pixel(w,z, [0, 0,0])
        sense.set_pixel(a,b, [0, 0,0])
        sense.set_pixel(x,y, [255, 0, 100])
        sense.set_pixel(w,z, [255, 0, 100])
        sense.set_pixel(a,b, [255, 0, 100])
    if pontos_eu >= 5:
        sense.show_message("Congrats", scroll_speed = 0.05)
        sense.clear()
        pontos_eu=0
        pontos_bot=0
        sense.set_pixel(x,y, [0, 0,0])
        sense.set_pixel(w,z, [0, 0,0])
        sense.set_pixel(a,b, [0, 0,0])
        sense.set_pixel(x,y, [255, 0, 100])
        sense.set_pixel(w,z, [255, 0, 100])
        sense.set_pixel(a,b, [255, 0, 100])

        
            
#jogo começa
sense.set_pixel(3,7, [255, 0, 100])
sense.set_pixel(4,7, [255, 0, 100])
sense.set_pixel(5,7, [255, 0, 100])

sense.set_pixel(3,0, [0, 0, 250])
sense.set_pixel(4,0, [0, 0, 250])
sense.set_pixel(5,0, [0, 0, 250])

sense.set_pixel(4,4, [255, 255, 255])

# variaveis
crescer=False
subir=True
speed=0.5
esquerda= True
direita= True
ball_esq=1
pontos_bot=0
pontos_eu=0

while True:
    barra()
    print (x,y) 
    barrabot()
    movbola()
    startagain()
    movbola1()
    pintarbola()
    startagain()
   
#barrazul
sense.stick.wait_for_event()


#Trabalho realizado por:
#Bruno Mendes
#Diogo Pires
#Maria Varanda
#Gelson Almeida
