from sense_hat import SenseHat
from time import sleep
from time import time
import random
import pygame
from pygame.locals import *
import serial

ser = serial.Serial("/dev/ttyACM0", timeout=1)
ser.baudrate = 115200
ser.parity   = serial.PARITY_NONE
ser.databits = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE

screen = pygame.display.set_mode([300,300])

sense = SenseHat()
pygame.init()

r = (255, 0, 0)
b = (0, 0, 255)
g = (0, 255, 0)
e = (0, 0, 0)
w = (255, 255, 255)
a = (255,255,0)
p = (255,105, 180)

sense.show_message("WELCOME TO BOSS FIGHT!",scroll_speed=0.05, text_colour=r, back_colour=e)
sense.show_letter("B", r, back_colour=e)
sleep(0.75)
sense.show_letter("O", r, back_colour=e)
sleep(0.75)
sense.show_letter("S", r, back_colour=e)
sleep(0.75)
sense.show_letter("S", r, back_colour=e)
sleep(0.75)
sense.show_letter("F", r, back_colour=e)
sleep(0.75)
sense.show_letter("I", r, back_colour=e)
sleep(0.75)
sense.show_letter("G", r, back_colour=e)
sleep(0.75)
sense.show_letter("H", r, back_colour=e)
sleep(0.75)
sense.show_letter("T", r, back_colour=e)
sleep(0.75)
sense.clear()

y = 3
x = 4

death_count = 0
cycles = 0

ball_positions = []
ball_directions = []

CPS = 2

cycle_start = 0

def move_balls():
    i = 0
    while i < len(ball_positions):
        if ball_positions[i][0] == 7 and ball_directions[i][0] == 1:
            del ball_positions[i]
            del ball_directions[i]
            continue
        if ball_positions[i][0] == 0 and ball_directions[i][0] == -1:
            del ball_positions[i]
            del ball_directions[i]
            continue
        if ball_positions[i][1] == 7 and ball_directions[i][1] == 1:
            del ball_positions[i]
            del ball_directions[i]
            continue
        if ball_positions[i][1] == 0 and ball_directions[i][1] == -1:
            del ball_positions[i]
            del ball_directions[i]
            continue
        draw_ball(i)
        i += 1
        
def check_collision():
    global y
    global x

    global death_count
    global cycles

    global ball_positions
    global ball_directions

    global CPS

    global cycle_start
    
    i = 0
    while i < len(ball_positions):
        if ball_positions[i][0] == x and ball_positions[i][1] == y:
            death_count += 1
            
            sense.show_message("Press B", scroll_speed=0.08, text_colour=(0, 0, 255))
            sleep(3)
            
            ser.write("Deathmusic\n".encode('UTF-8'))
            
            sense.show_message("Game Over", scroll_speed=0.08, text_colour=(255, 0, 0))
            sense.show_message(f"Deaths: {death_count}", scroll_speed=0.08, text_colour=(255, 0, 0))
            sleep(1)
            y = 3
            x = 4
            cycles = 0
            CPS = 2
            ball_positions = []
            ball_directions = []
            
            cycle_start = current_ms()
            
            ser.write ("Megalovania\n".encode('UTF-8'))
        i += 1

def current_ms():
    return int(round(time() * 1000))

def draw_heart():
    sense.set_pixel (x, y, 255, 0, 0)
    
def draw_ball(i):
    ball_positions[i][0] += ball_directions[i][0]
    ball_positions[i][1] += ball_directions[i][1]  
    sense.set_pixel(ball_positions[i][0], ball_positions[i][1], 255, 255, 255)
       
ser.write("Megalovania\n".encode('UTF-8')) 

cycle_start = current_ms()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == ord('a')) and x > 0:
                sense.set_pixel(x, y, [0, 0, 0])
                x -= 1
                check_collision()
                draw_heart()
            elif (event.key == K_RIGHT or event.key == ord('d')) and x < 7:
                sense.set_pixel(x, y, [0, 0, 0])
                x += 1
                check_collision()
                draw_heart()
            elif (event.key == K_UP or event.key == ord('w')) and y > 0:
                sense.set_pixel(x, y, [0, 0, 0])
                y -= 1
                check_collision()
                draw_heart()
            elif (event.key == K_DOWN or event.key == ord('s')) and y < 7:
                sense.set_pixel(x, y, [0, 0, 0])
                y += 1
                check_collision()
                draw_heart()
                
    cycle_test = current_ms()
    if cycle_test - cycle_start >= (1 / CPS * 1000):
        cycle_start = cycle_test - (cycle_test - cycle_start) % (1 / CPS)
        
        sense.clear(0, 0, 0)
        draw_heart()
        
        move_balls()
        check_collision() 
        
        cycles += 1
        if cycles / CPS == 30:
            CPS = 3
        if cycles / CPS == 54:
            CPS = 6
        if cycles % 2 == 0:
            ball_positions.append([-1, random.randint(0, 7)])
            ball_directions.append([1, 0])
        if cycles % 3 == 0:
            ball_positions.append([random.randint(0, 7), -1])
            ball_directions.append([0, 1])    
        if cycles % 6 == 0:
            ball_positions.append([random.randint(0, 7), -1])
            ball_directions.append([1, 1])
        if cycles % 12 == 0:
            ball_positions.append([-1, random.randint(0, 7)])
            ball_directions.append([1, 1])
        if cycles == 66:
            
            sense.show_message("You Won", scroll_speed=0.08, text_colour=(0, 255, 0))
            sense.show_message(f"Deaths: {death_count}", scroll_speed=0.08, text_colour=(255, 0, 0))
     
            ser.write ("Pacman\n".encode('UTF-8'))
            
            sense.set_pixels([
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,r,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,e,e,e,
            a,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,r,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            a,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            a,e,e,e,e,e,e,e,
            a,a,e,e,e,e,e,e,
            a,a,e,e,e,e,e,e,
            a,a,e,e,r,e,e,e,
            a,a,e,e,e,e,e,e,
            a,a,e,e,e,e,e,e,
            a,a,e,e,e,e,e,e,
            a,e,e,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            a,a,e,e,e,e,e,e,
            a,a,a,e,e,e,e,e,
            a,a,e,e,e,e,e,e,
            a,e,e,e,r,e,e,e,
            a,e,e,e,e,e,e,e,
            a,a,e,e,e,e,e,e,
            a,a,a,e,e,e,e,e,
            a,a,e,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            a,a,a,e,e,e,e,e,
            a,a,a,a,e,e,e,e,
            a,a,a,a,e,e,e,e,
            a,a,a,a,r,e,e,e,
            a,a,a,a,e,e,e,e,
            a,a,a,a,e,e,e,e,
            a,a,a,a,e,e,e,e,
            a,a,a,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            a,a,a,a,e,e,e,e,
            a,a,a,a,a,e,e,e,
            b,a,a,a,e,e,e,e,
            a,a,a,e,e,r,e,e,
            a,a,a,e,e,e,e,e,
            a,a,a,a,e,e,e,e,
            a,a,a,a,a,e,e,e,
            a,a,a,a,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,a,a,a,a,e,e,e,
            a,a,a,a,a,a,e,e,
            a,b,a,a,a,a,e,e,
            a,a,a,a,a,a,r,e,
            a,a,a,a,a,a,e,e,
            a,a,a,a,a,a,e,e,
            a,a,a,a,a,a,e,e,
            e,a,a,a,a,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,a,a,a,a,e,e,
            e,a,a,a,a,a,a,e,
            a,a,b,a,a,a,e,e,
            a,a,a,a,a,e,e,r,
            a,a,a,a,a,e,e,e,
            a,a,a,a,a,a,e,e,
            e,a,a,a,a,a,a,e,
            e,e,a,a,a,a,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,a,a,a,a,e,
            e,e,a,a,a,a,a,a,
            e,a,a,b,a,a,a,a,
            e,a,a,a,a,a,a,a,
            e,a,a,a,a,a,a,a,
            e,a,a,a,a,a,a,a,
            e,e,a,a,a,a,a,a,
            e,e,e,a,a,a,a,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,a,a,a,a,
            e,e,e,a,a,a,a,a,
            e,e,a,a,b,a,a,a,
            e,e,a,a,a,a,a,e,
            e,e,a,a,a,a,a,e,
            e,e,a,a,a,a,a,a,
            e,e,e,a,a,a,a,a,
            e,e,e,e,a,a,a,a])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,a,a,a,
            e,e,e,e,a,a,a,a,
            e,e,e,a,a,b,a,a,
            e,e,e,a,a,a,a,a,
            e,e,e,a,a,a,a,a,
            e,e,e,a,a,a,a,a,
            e,e,e,e,a,a,a,a,
            e,e,e,e,e,a,a,a])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,a,a,a,
            e,e,e,e,a,a,b,a,
            e,e,e,e,a,a,a,a,
            e,e,e,e,a,a,a,a,
            e,e,e,e,a,a,a,a,
            e,e,e,e,e,a,a,a,
            e,e,e,e,e,e,a,a])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,a,a,b,
            e,e,e,e,e,a,a,a,
            e,e,e,e,e,a,a,a,
            e,e,e,e,e,a,a,a,
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,e,e,a])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,e,a,a,
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,e,a,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e])
            sleep(0.5)
            
            sense.set_pixels([
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e])
            sleep(0.5)
            
            death_count += 1
            sense.show_message("You LOST", scroll_speed=0.08, text_colour=(0, 255, 0))
            sense.show_message(f"Deaths: {death_count}", scroll_speed=0.08, text_colour=(255, 0, 0))
            quit()

    
    






