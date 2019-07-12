from sense_hat import SenseHat
from guizero import *
from time import sleep
from random import choice

sense = SenseHat()

r=(247,86,61)
l=(105,198,247)
g=(132,247,61)
t=(249,247,77)
w=(255,255,255)
c=(183,125,63)
b=(81,61,26)
p=(234,126,173)
a=(2,247,202)
j=(0,0,0)
z=(86,86,30)

state = "menu"

image= [
j,j,j,j,j,j,j,j,
c,c,j,j,j,j,c,c,
c,p,c,c,c,c,p,c,
j,c,a,c,c,a,c,j,
j,c,c,c,c,c,c,j,
j,c,c,b,b,c,c,j,
j,j,c,b,b,c,j,j,
j,j,j,j,j,j,j,j
]
sense.set_pixels(image)
sleep(1)

sense.show_message("Raspie!", scroll_speed=0.05, text_colour=[183,125,63])
y = 4
x = 4
def draw_ball():
        sense.set_pixel(0,7,(132,247,61))
        sense.set_pixel(1,7,(132,247,61))
        sense.set_pixel(2,7,(234,126,173))
        sense.set_pixel(3,7,(234,126,173))
        sense.set_pixel(4,7,(247,86,61))
        sense.set_pixel(5,7,(247,86,61))
        sense.set_pixel(6,7,(105,198,247))
        sense.set_pixel(7,7,(105,198,247))
        sense.set_pixel(3,0,(255,255,255))
        sense.set_pixel(4,0,(255,255,255))
        sense.set_pixel(x,y,(183,125,63))

def draw_ball_pong():
    global state
    global x
    global y
    if ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 0:
        state = "menu"
        x = 4
        y = 4
        return
    if ball_position[0] == 1 and bat_y - 1 <= ball_position[1] <= bat_y + 1:
        ball_velocity[0] = -ball_velocity[0]

    sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 255)
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)


def move_up_pong(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 0:
        bat_y -= 1


def move_down_pong(event):
    global bat_y
    if event.action == "pressed" and bat_y < 6:
        bat_y += 1

# MENU FUNCTIONS
def move_up(event):
    global y
    sense.set_pixel(x,y, (0,0,0))
    if event.action == 'pressed' and y > 0:
        y -= 1
def move_down(event):
    global y
    sense.set_pixel(x,y, (0,0,0))
    if event.action == 'pressed' and y < 7:
        y += 1

def move_left(event):
    global x
    sense.set_pixel(x,y, (0,0,0))
    if event.action == 'pressed' and x > 0:
        x -= 1

def move_right(event):
    global x
    sense.set_pixel(x,y, (0,0,0))
    if event.action == 'pressed' and x < 7:
        x += 1

def move_middle(event):
        if event.action == 'pressed':
            sense.set_pixels(lights_off)

# Bath
def move_middle_bath(event):
            if event.action == 'pressed':
                sense.set_pixels(bath1)

def move_middle1_bath(event):
            if event.action == 'pressed':
                sense.set_pixels(bath2)



while True:
    sense.clear()
    state = "menu"
    if state == "menu":
        sense.stick.direction_right = move_right
        sense.stick.direction_left = move_left
        sense.stick.direction_down = move_down
        sense.stick.direction_up = move_up
        draw_ball()

    if x == 6 and y == 7 and state == "menu":
        state = "bath"
    if x == 0 and y == 7 and state == "menu":
        state = "fun"
    if x == 1 and y == 7 and state == "menu":
        state = "fun"
    if x == 2 and y == 7 and state == "menu":
        state = "food"
    if x == 4 and y == 7 and state == "menu":
        state = "sleep"
    if x == 3 and y == 7 and state == "menu":
        state = "food"
    if x == 7 and y == 7 and state == "menu":
        state = "bath"
    if x == 5 and y == 7 and state == "menu":
        state = "sleep"
    if x == 3 and y == 0 and state == "menu":
        state = "stats"
    if x == 4 and y == 0 and state == "menu":
        state = "stats"

    if state == "sleep":
        lights_on= [
        j,j,j,j,j,j,t,c,
        j,j,j,j,j,j,t,t,
        j,j,j,j,j,j,j,j,
        j,c,c,j,j,j,j,c,
        j,c,c,c,c,c,c,j,
        r,w,c,c,c,c,w,r,
        r,w,w,w,w,w,w,r,
        r,r,r,r,r,r,r,r
        ]

        lights_off=[
        j,j,j,j,j,j,z,c,
        j,j,j,j,j,j,z,z,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j
        ]
        sense.set_pixels(lights_on)
        sense.stick.direction_middle = move_middle
        sleep(10)
        sense.clear(0,0,0)
        sense.show_message("Well Rested!", scroll_speed=0.045, text_colour=[249,247,77])
        state = "menu"
        x=4
        y=4

    if state == "bath":
        bath0 = [
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        w,j,j,j,j,j,j,w,
        j,w,j,j,j,j,w,j,
        j,j,w,w,w,w,j,j
        ]
        bath1 = [
        j,j,l,j,j,j,l,j,
        j,j,j,j,l,j,j,j,
        j,j,l,j,j,j,l,j,
        j,j,j,j,l,j,j,j,
        j,j,l,j,j,j,l,j,
        w,j,j,j,l,j,j,w,
        j,w,l,j,j,j,w,j,
        j,j,w,w,w,w,j,j
        ]
        bath2 = [
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        w,l,l,l,l,l,l,w,
        j,w,l,l,l,l,w,j,
        j,j,w,w,w,w,j,j
        ]
        sense.set_pixels(bath0)
        sense.stick.direction_middle = move_middle_bath
        sleep(5)


        sense.stick.direction_middle = move_middle1_bath
        sleep(5)
        sense.show_message("All Cleaned Up!", scroll_speed=0.035, text_colour=[105,198,247])
        sense.clear(0,0,0)
        state = "menu"
        x=4
        y=4

    if state == "food":
        eat= [
        j,j,j,p,p,j,j,j,
        j,j,p,p,p,p,j,j,
        j,j,p,p,p,p,j,j,
        j,j,p,w,w,p,j,j,
        j,j,w,w,w,w,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j
        ]

        sense.set_pixels(eat)
        sleep(1)

        eat1= [
        j,j,j,j,j,j,j,j,
        j,j,j,p,p,j,j,j,
        j,j,p,p,p,p,j,j,
        j,j,p,w,w,p,j,j,
        j,j,w,w,w,w,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j
        ]

        sense.set_pixels(eat1)
        sleep(1)

        eat2= [
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,p,p,j,j,j,
        j,j,p,w,w,p,j,j,
        j,j,w,w,w,w,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j
        ]

        sense.set_pixels(eat2)
        sleep(1)

        eat3= [
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,w,w,w,w,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j
        ]

        sense.set_pixels(eat3)
        sleep(1)

        eat4= [
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j,
        j,j,j,c,c,j,j,j
        ]
        sense.set_pixels(eat4)
        sleep(1)

        sense.show_message("Great!", scroll_speed=0.035, text_colour=[234,126,173])
        sense.clear(0,0,0)
        state = "menu"
        x=4
        y=4

    if state == "stats":
        needs = choice(['food', 'sleep', 'to be entertained', 'a bath'])
        sense.show_message('I need {}'. format(needs), scroll_speed=0.05, text_colour=[183,125,63])
        sleep(1)
        state = "menu"
        x = 4
        y = 4

    if state == "fun":

        white = (255,255,255)
        bat_y = 4

        sense.stick.direction_down = move_down_pong
        sense.stick.direction_up = move_up_pong

        ball_position = [3,3]
        ball_velocity = [1,1]

        while state == "fun":
            sense.clear()
            draw_ball_pong()
            draw_bat()
            sleep(0.25)
    sleep(0.25)
