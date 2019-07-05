
from sense_hat import SenseHat
from time import sleep
from shutil import copyfile
from random import randint
import serial

PORT = "/dev/ttyACM0" or "/dev/ttyACM1"

BAUD = 115200
s = serial.Serial(PORT, timeout=0)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

sense = SenseHat()

X = [0, 0, 0]  # Black
O = [255, 255, 255]  # White
A = [0, 100, 0] #Green
R = [255, 0, 0] #Red
P = [255, 0, 125] #Purple
Y = [250, 250, 0] #Yellow
B = [100, 50, 0] #Brown
L = [0, 250, 250] #Blue



calculator_symbol = [
X, X, X, A, A, X, X, X,
X, X, X, A, A, X, X, X,
X, X, X, A, A, X, X, X,
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
X, X, X, A, A, X, X, X,
X, X, X, A, A, X, X, X,
X, X, X, A, A, X, X, X
]

stepcounter_symbol = [
X, R, R, X, X, R, R, X,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
X, R, R, R, R, R, R, X,
X, X, R, R, R, R, X, X,
X, X, X, R, R, X, X, X
]

metronome_symbol = [
X, X, X, P, P, P, P, X,
X, X, X, P, P, P, P, P,
X, X, X, P, P, X, X, X,
X, X, X, P, P, X, X, X,
X, X, X, P, P, X, X, X,
X, P, P, P, P, X, X, X,
P, P, P, P, P, X, X, X,
P, P, P, P, X, X, X, X
]

thermometer_symbol = [
X, X, X, Y, X, X, X, Y,
Y, X, Y, X, X, Y, Y, X,
X, Y, X, Y, Y, X, X, X,
X, X, Y, Y, Y, Y, X, X,
X, X, Y, Y, Y, Y, Y, X,
X, Y, X, Y, Y, X, X, Y,
X, Y, X, X, X, Y, X, X,
Y, X, X, X, X, Y, X, X
]

compass_symbol = [
X, X, O, O, O, O, X, X,
X, O, X, X, X, R, R, X,
O, X, X, X, X, X, R, O,
O, X, X, X, R, X, X, O,
O, X, X, A, A, X, X, O,
O, X, X, A, X, X, X, O,
X, O, X, X, A, X, O, X,
X, X, O, A, A, O, X, X
]


timer_symbol = [
B, B, B, B, B, B, B, B,
X, B, X, X, Y, Y, B, X,
X, X, B, Y, Y, B, X, X,
X, X, X, B, B, X, X, X,
X, X, X, B, B, X, X, X,
X, X, B, Y, X, B, X, X,
X, B, Y, Y, Y, X, B, X,
B, B, B, B, B, B, B, B
]

playstore_symbol = [
A, X, X, X, X, X, X, A,
X, A, X, X, X, X, A, X,
X, X, A, A, A, A, X, X,
X, A, L, A, A, L, A, X,
X, X, A, A, A, A, X, X,
A, A, A, A, A, A, A, A,
A, X, A, L, L, A, X, A,
A, X, A, A, A, A, X, A
]

gameintro = [
X, X, X, Y, Y, X, X, X,
X, X, Y, Y, L, Y, X, X,
X, X, Y, Y, Y, Y, Y, Y,
X, X, X, Y, Y, Y, X, X,
X, X, X, Y, Y, Y, Y, X,
X, Y, Y, Y, Y, Y, Y, X,
X, Y, Y, Y, Y, Y, Y, X,
X, X, Y, Y, Y, Y, X, X
]

paperrock = [
X, X, X, X, X, X, X, X,
X, O, X, X, X, X, X, O,
O, X, O, X, X, X, O, X,
X, O, O, O, X, O, X, X,
X, X, X, O, O, X, X, X,
X, O, O, O, X, O, X, X,
O, X, O, X, X, X, O, X,
X, O, X, X, X, X, X, O
]

snake_game = [
X, X, X, X, A, A, A, R,
X, X, X, X, A, A, A, A,
X, X, X, X, O, O, X, X,
A, A, O, A, A, A, X, X,
A, A, O, A, A, A, X, X,
A, A, X, X, X, X, X, X,
A, A, O, A, A, A, A, X,
A, A, O, A, A, A, A, X
]

randomizer_symbol = [
X, X, A, X, X, A, X, X,
X, A, A, X, X, A, A, X,
A, A, A, X, X, A, A, A,
X, X, X, A, A, X, X, X,
X, X, X, A, A, X, X, X,
A, A, A, X, X, A, A, A,
X, A, A, X, X, A, A, X,
X, X, A, X, X, A, X, X
]

intro = [
R, R, R, X, X, O, O, X,
R, X, X, R, O, X, X, O,
R, X, X, R, O, X, X, O,
R, R, R, X, O, O, O, O,
R, X, X, X, O, X, X, O,
R, X, X, X, O, X, X, O,
R, X, X, X, O, X, X, O,
R, X, X, X, O, X, X, O
]

sense.set_pixels(intro)


program_list=[timer_symbol, metronome_symbol, calculator_symbol, stepcounter_symbol, thermometer_symbol, compass_symbol, randomizer_symbol, playstore_symbol]
games_list=[paperrock, snake_game]

selected_program=-1
selected_game=-1
inside_games_list=False

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "up" and not inside_games_list:
            if selected_program == -1:
                selected_program=0
            elif selected_program == len(program_list) - 1:
                selected_program=0
            else:
                selected_program+=1
            sense.set_pixels(program_list[selected_program])
        if event.action == "pressed" and event.direction == "down" and not inside_games_list:
            if selected_program == -1:
                selected_program=0
            elif selected_program == 0:
                selected_program=len(program_list) - 1
            else:
                selected_program-=1
            sense.set_pixels(program_list[selected_program])
            
        if event.action == "pressed" and event.direction == "middle" and not inside_games_list:
            dest = '/media/pi/MICROBIT/p.hex'
            if selected_program == 2:
                copyfile('/home/pi/MicrobitProjeto/calculadtor-18.hex', dest)
            elif selected_program == 1:
                copyfile('/home/pi/MicrobitProjeto/metronome-04.hex', dest)
            elif selected_program == 3:
                copyfile('/home/pi/MicrobitProjeto/step-counter-06.hex', dest)
            elif selected_program == 0:
                copyfile('/home/pi/MicrobitProjeto/timer07.hex', dest)
            elif selected_program == 4:
                copyfile('/home/pi/MicrobitProjeto/thermometer-02.hex', dest)
            elif selected_program == 5:
                copyfile('/home/pi/MicrobitProjeto/compass03.hex', dest)
            elif selected_program == 6:
                copyfile('/home/pi/MicrobitProjeto/randomizer04.hex', dest)
            elif selected_program == 7:
                inside_games_list=True
                sense.set_pixels(gameintro)
                continue 


        if event.action == "pressed" and event.direction == "up" and inside_games_list:
            if selected_game == -1:
                selected_game=0
            elif selected_game == len(games_list) - 1:
                selected_game=0
            else:
                selected_game+=1
            sense.set_pixels(games_list[selected_game]) 
        if event.action == "pressed" and event.direction == "down" and inside_games_list:
            if selected_game == -1:
                selected_game=0
            elif selected_game == 0:
                selected_game=len(games_list) - 1
            else:
                selected_game-=1
            sense.set_pixels(games_list[selected_game])

        if event.action == "pressed" and event.direction == "middle" and inside_games_list:
            dest = '/media/pi/MICROBIT/p.hex'
            if selected_game == 0:
                copyfile('/home/pi/MicrobitProjeto/ROCK-PAPER-SCISSORS-03.hex', dest)
            if selected_game == 1:
                copyfile('/home/pi/MicrobitProjeto/snake08.hex', dest)
                sleep(15)
                score = 0
                inverted = False
                speed = 0.50
                snake_pos = [3, 3, 3, 4, 3, 5, 3, 6]
                apple_pos = [randint(0, 7), randint(0, 7)]
                snake_dir = 1
                def draw_apple():
                    sense.set_pixel(apple_pos[0], apple_pos[1], 255, 0, 0)
                def draw_snake(t):
                    global snake_pos, snake_dir
                    if t==1:
                        snake_pos.append(snake_pos[len(snake_pos)-2])
                        snake_pos.append(snake_pos[len(snake_pos)-1])
                    for i in range(1, len(snake_pos) -1):
                        global snake_ops
                        snake_pos[len(snake_pos)-i]=snake_pos[len(snake_pos)-i-2]
                    if snake_dir == 1:
                        snake_pos[1]-=1
                    elif snake_dir == 2:
                        snake_pos[1]+=1
                    elif snake_dir == 3:
                        snake_pos[0]-=1
                    elif snake_dir == 4:
                        snake_pos[0]+=1
                    if snake_pos[0]>7:
                        snake_pos[0]=0
                    if snake_pos[0]<0:
                        snake_pos[0]=7
                    if snake_pos[1]>7:
                        snake_pos[1]=0
                    if snake_pos[1]<0:
                        snake_pos[1]=7
                    for i in range (0, int(len(snake_pos)//2)):
                        if i==0:
                            sense.set_pixel(snake_pos[2*(i)], snake_pos[2*(i)+1], 0,255,0)
                        elif i == 1:
                            sense.set_pixel(snake_pos[2*(i)], snake_pos[2*(i)+1], 0, 150, 0)
                        else:
                            sense.set_pixel(snake_pos[2*(i)], snake_pos[2*(i)+1], 0, 100, 0)
                def move_up():
                    global snake_dir
                    if snake_dir != 2:
                        snake_dir = 1
                def move_down():
                   global snake_dir
                   if snake_dir != 1:
                        snake_dir = 2
                def move_left():
                    global snake_dir
                    if snake_dir != 4:
                        snake_dir = 3
                def move_right():
                    global snake_dir
                    if snake_dir != 3:
                        snake_dir = 4
                if not inverted:
                    sense.stick.direction_up = move_up
                    sense.stick.direction_down = move_down
                    sense.stick.direction_left = move_left
                    sense.stick.direction_right = move_right
                else:
                    sense.stick.direction_down = move_up
                    sense.stick.direction_up = move_down
                    sense.stick.direction_right = move_left
                    sense.stick.direction_left = move_right
                paused = False
                while True:
                    msg=s.readline().decode("UTF-8").rstrip()
                    if msg == 'AB':
                        sense.set_pixels(intro)
                        inside_games_list=False
                        selected_game=-1
                        selected_program=-1
                        copyfile('/home/pi/MicrobitProjeto/nada01.hex', dest)
                        break
                    if msg == 'A':
                        paused = False if paused else True
                    if msg == 'B':
                       f=open("highscore.txt", "r+")
                       s.write("highscore {}\n".format(f.read()).encode('UTF-8'))
                       f.close()
                    if not paused:
                        sense.clear()
                        end = False
                        for i in range (1, int(len(snake_pos)/2)-1):
                            if not end:
                                if snake_pos[0] == snake_pos[2*i] and snake_pos[1] == snake_pos[2*i+1]:
                                    s.write("game over\n".encode('UTF-8'))
                                    f=open("highscore.txt", "r")
                                    hs = f.read()
                                    f.close()     
                                    if hs == '' or int(hs) < score:
                                        f=open("highscore.txt", "w")
                                        f.write(str(score))
                                        f.close()
                                    sense.show_message("You scored " + str(score))       
                                    score = 0
                                    speed = 0.50
                                    snake_pos = [3, 3, 3, 4, 3, 5, 3, 6]
                                    apple_pos = [randint(0, 7), randint(0, 7)]
                                    snake_dir = 1
                                    end = True

                        draw_apple()
                        if apple_pos[0]==snake_pos[0] and apple_pos[1] == snake_pos[1]:
                            draw_snake(1)
                            speed = speed * 0.9
                            apple_pos[0] = randint(0, 7)
                            apple_pos[1] = randint(0, 7)
                            score += 1
                            s.write("score {}\n".format(score).encode('UTF-8'))
                        else:
                            draw_snake(0)
                        sleep(speed)

                    
        if event.action == "pressed" and (event.direction == "left" or event.direction == "right") and inside_games_list:
            sense.set_pixels(intro)
            inside_games_list=False
            selected_game=-1
            selected_program=-1
