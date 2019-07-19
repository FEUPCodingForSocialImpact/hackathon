from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = [200, 0, 0]
b = [0, 0, 200]
a = [200, 200, 0]
e = [0, 0, 0]
re = [50, 0, 0]
ae = [50, 50, 0]
w = [200,200,200]

image1 =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e
    ]

image2 =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    ]
image3 =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    ]
image4 =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    ]
image5=[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    ]
image6=[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    ]

imagef = [
    e,re,e,e,e,ae,e,e,
    e,e,e,e,e,e,e,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    b,b,b,b,b,b,b,e,
    ]

def draw_bat():
    sense.set_pixel(x, y, p)
    
x=3
y=1
p=r    
sense.set_pixels(image1)
sleep(0.2)
sense.set_pixels(image2)
sleep(0.2)
sense.set_pixels(image3)
sleep(0.2)
sense.set_pixels(image4)
sleep(0.2)
sense.set_pixels(image5)
sleep(0.2)
sense.set_pixels(image6)
sleep(0.2)
sense.set_pixels(imagef)
sleep(0.5)
sense.set_pixel(1, 0, r)
sleep(1)

pontR=0
pontA=0

def move_left(event):
    global x
    if y==1:
        if event.action == 'pressed' and x>0:
            sense.set_pixel(x,y,e)
            x = x-1

sense.stick.direction_left = move_left


def move_right(event):
    
    global x
    if y==1:
        if event.action == 'pressed' and x<6:
            sense.set_pixel(x,y,e)
            x = x+1
            draw_bat()

sense.stick.direction_right = move_right

def move_fall(event):
    global y
    while y<7 and sense.get_pixel(x,y+1) == b:
        sleep(0.2)
        sense.set_pixel(x,1,e)
        if y>1:
            sense.set_pixel(x,y,b)
        y = y+1
        draw_bat()


sense.stick.direction_down = move_fall

def reset(event):
    global x
    global y
    global p
    if event.action == 'pressed':
        sense.clear
        sense.set_pixel(x,y,e)
        p=r
        x=3
        y=1
        sense.set_pixels(imagef)
        sense.set_pixel(1, 0, r)
        sleep(1)
        draw_bat()
                
sense.stick.direction_up = reset

def vit(x,y,p):
    global sense
    #horizontal
    leftC = countA(x,y,p,-1,0)
    rightC = countA(x,y,p,1,0)
    totalC = leftC + rightC + 1
    
    if totalC >= 4:
        return True
    
    #vertical
 
    downC = countA(x,y,p,0,1)
    totalC = downC + 1
    
    if totalC >= 4:
        return True
    
    #diagonal p
    downC = countA(x,y,p,-1,1)
    upC = countA(x,y,p,1,-1)
    totalC = downC + upC + 1
    
    if totalC >= 4:
        return True
    
    #digaonal n
    upC = countA(x,y,p,-1,-1)
    downC = countA(x,y,p,1,1)
    totalC = upC + downC + 1
    
    if totalC >= 4:
        return True
    
    return False

def countA(x,y,p,xC,yC):
    global sense
    countA = 0
    while True:
        x = x + xC
        if x < 0 or x > 6:
            return countA
        
        y = y + yC
        if y < 2 or y > 7:
            return countA
        
        if sense.get_pixel(x,y) == p:
            countA = countA + 1
        else:
            return countA

def boardf():
    if sense.get_pixel(0,2)!=b and sense.get_pixel(1,2) and sense.get_pixel(2,2)!=b and sense.get_pixel(3,2)!=b and sense.get_pixel(4,2)!=b and sense.get_pixel(5,2)!=b and sense.get_pixel(6,2)!=b and sense.get_pixel(7,2)!=b:
        reset

        
while True:
    draw_bat()
    sleep(0.25)
    if vit(x,y,p):
        if p==r:
            sense.set_pixel(x,y,r)
            sleep(1)
            sense.show_message("YOU WIN", back_colour=b, text_colour=r)
            sense.show_message("YOU WIN", back_colour=b, text_colour=r)
            pontR = pontR + 1
            sense.show_message("SCORE:", back_colour=b, text_colour=r)
            sense.show_message(str(pontR), back_colour=b, text_colour=r)
            sense.show_message("SCORE:", back_colour=b, text_colour=a)
            sense.show_message(str(pontA), back_colour=b, text_colour=a)
            p=b
            x=3
            y=1
            sense.clear
            p=r
            x=3
            y=1
            sense.set_pixels(imagef)
            sense.set_pixel(1, 0, r)
            sleep(1)
        if p==a:
            sense.set_pixel(x,y,a)
            sleep(1)
            sense.show_message("YOU WIN", back_colour=b, text_colour=a)
            sense.show_message("YOU WIN", back_colour=b, text_colour=a)
            pontA = pontA + 1
            sense.show_message("SCORE:", back_colour=b, text_colour=r)
            sense.show_message(str(pontR), back_colour=b, text_colour=r)
            sense.show_message("SCORE:", back_colour=b, text_colour=a)
            sense.show_message(str(pontA), back_colour=b, text_colour=a)
            p=b
            x=3
            y=1
            sense.clear
            p=r
            x=3
            y=1
            sense.set_pixels(imagef)
            sense.set_pixel(1, 0, r)
            sleep(1)
    if y==7 or sense.get_pixel(x,y+1) != b and y!=1:
        sleep(0.5) 
        if sense.get_pixel(x,y) == r:
            sense.set_pixel(x, y, r)
            sense.set_pixel(1,0,re)
            sleep(0.5)
            sense.set_pixel(5,0,a)
            x=3
            y=1
            p=a
        if sense.get_pixel(x,y) == a:
            sense.set_pixel(x,y,a)
            sense.set_pixel(5,0,ae)
            sleep(0.5)
            sense.set_pixel(1,0,r)
            x=3
            y=1
            p=r