from sense_hat import SenseHat
from random import randint
from time import sleep
import serial
import time
import os

sense = SenseHat()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0,153,0)

x = 0
y = 0

PORT = "/dev/ttyACM0"
##
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.setTimeout(0)

# Verificar se o ficheiro que armazena o recorde existe

if (os.path.isfile('recorde.txt') != True):
    fx=open("recorde.txt","w")
    fx.close()

# Ciclo principal (reiniciar o jogo)

while True:

    score=0
    p=5

    matrix = [[BLUE for column in range(8)] for row in range(8)]

    time_elapsed = 0
    last_time = 0

    FRAME_TIME = 400

    sense.show_message('Prima A para jogar', text_colour=RED, back_colour=(10,0,0), scroll_speed=0.05)

    data=s.readline().decode().rstrip()

    while data != '0':
        data=s.readline().decode().rstrip()

    def flatten(matrix):
        flattened = [pixel for row in matrix for pixel in row]
        return flattened

    def gen_pipes(matrix):
        for row in matrix:
            row[-1] = GREEN
        gap = randint(1, 6)
        matrix[gap][-1] = BLUE
        matrix[gap - 1][-1] = BLUE
        matrix[gap + 1][-1] = BLUE
        return matrix

    def move_pipes(matrix):
        for row in matrix:
            for i in range(7):
                row[i] = row[i + 1]
            row[-1] = BLUE
        return matrix

    def draw_bird(event):
        global y
        global x
        sense.set_pixel(x, y, BLUE)

    def check_collision(matrix):
        if matrix[y][x] == GREEN:
            return True
        else:
            return False

    last_time = int(round(time.time() * 1000))
    c=1
    score=-1

    # Ciclo do jogo (leitura de data e ambiente do jogo)
    
    while True:
        data=s.readline().decode().rstrip()
        if data:
            sense.set_pixel(x, y, BLUE)
            if data == '1' and y > 0:
                y-=1
            elif data == '0' and y < 7:
                y+=1
            sense.set_pixel(x, y, YELLOW)
        tempo_atual = int(round(time.time() * 1000))
        time_elapsed = tempo_atual - last_time
        if time_elapsed > FRAME_TIME:
            tempo_extra = time_elapsed % FRAME_TIME
            last_time = int(round(time.time() * 1000)) - tempo_extra
            time_elapsed = tempo_extra
            if score < 14:
                p=5
                if c == 2:
                    s.write("Tocar\n".encode('UTF-8'))
            elif score >= 14 and score <= 40:
                p=4
                if c == 3 and score != 40:
                    s.write("Tocar\n".encode('UTF-8'))
                if score == 40:
                    if c == 4:
                        s.write("Tocar\n".encode('UTF-8'))
            elif score > 40:
                p=3
                if c == 1 and score != 41:
                    s.write("Tocar\n".encode('UTF-8'))
            if c == 1:
                matrix = gen_pipes(matrix)
                if check_collision(matrix):
                    s.write("Lose\n".encode('UTF-8')) 
                    break
            elif c == p:
                c = 0
                score+=1
            matrix = move_pipes(matrix)
            sense.set_pixels(flatten(matrix))
            sense.set_pixel(x, y, YELLOW)   
            if check_collision(matrix):
                s.write("Lose\n".encode('UTF-8'))
                break
            c+=1

    # Certificar se o score é o novo recorde (se sim armazena o valor do score)
    
    fx = open("recorde.txt","r+")
    rec = fx.read()
    if rec=='':
        fx.write(str(score))
        sense.show_message('Parabens, bateu o novo recorde! Score: {0}'.format(score), text_colour=RED, back_colour=(10,0,0), scroll_speed=0.05)
        fx.close()
    else:
        if score > int(rec):
            fx.seek(0)
            fx.truncate()
            fx.write(str(score))
            sense.show_message('Parabens, bateu o recorde! Score: {0}'.format(score), text_colour=RED, back_colour=(10,0,0), scroll_speed=0.05)
            fx.close()
        else:
            sense.show_message('Perdeu! Score: {0}'.format(score), text_colour=RED, back_colour=(10,0,0), scroll_speed=0.05)
    game_over = False

    sleep(1)
