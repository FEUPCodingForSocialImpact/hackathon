from sense_hat import SenseHat
from random import randint
from time import sleep
from guizero import App, Text, TextBox, PushButton, Slider, Picture, info

sense = SenseHat()

sense.clear()

w = (255, 255, 255)
r = (255, 0, 0)
o = (255, 127, 0)
ye = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)

speed = 0.04
sense.show_message("Start press -> for normal, <- for hard or \!/ for insane  difficulty.", speed, text_colour = b)

image = [
e,e,e,e,e,e,e,e,
e,e,w,w,w,w,w,e,
e,e,e,e,e,w,e,e,
e,e,e,e,w,e,e,e,
e,e,e,e,e,w,e,e,
e,e,e,e,e,e,w,e,
e,e,w,e,e,e,w,e,
e,e,e,w,w,w,e,e,
]

image2 = [
e,e,e,e,e,e,e,e,
e,e,e,w,w,w,e,e,
e,e,w,e,e,e,w,e,
e,e,e,e,e,w,e,e,
e,e,e,e,w,e,e,e,
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,e,w,w,w,w,w,e,
]


image3 = [
e,e,e,e,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,w,e,w,e,e,e,
e,e,e,e,w,e,e,e,
e,e,e,e,w,e,e,e,
e,e,e,e,w,e,e,e,
e,e,e,e,w,e,e,e,
e,e,e,e,w,e,e,e,
]

go_message = "GO"

def drawSnake(x1, y1):
    sense.set_pixel(x1, y1, (0, 255, 0))

def drawApple():
    global x2, y2
    x2 = randint(0, 7)
    y2 = randint(0, 7)
    while True:
        if [x2, y2] in pixeis_cobra:
            x2 = randint(0, 7)
            y2 = randint(0, 7)
        else:
            sense.set_pixel(x2, y2, (255, 0, 0))
            break

def normal():
    sense.set_pixels(image)
    sleep(0.5)
    sense.set_pixels(image2)
    sleep(0.5)
    sense.set_pixels(image3)
    sleep(0.5)
    sense.show_message(go_message, speed)
    sleep(0.5)
    sense.clear()
    global sleep_time
    sleep_time = 0.2
    global difficulty
    difficulty = 0

def hard():
    sense.set_pixels(image)
    sleep(0.5)
    sense.set_pixels(image2)
    sleep(0.5)
    sense.set_pixels(image3)
    sleep(0.5)
    sense.show_message(go_message, speed)
    sleep(0.5)
    sense.clear()
    global sleep_time
    sleep_time = 0.1
    global difficulty
    difficulty = 1

def insane():
    sense.set_pixels(image)
    sleep(0.5)
    sense.set_pixels(image2)
    sleep(0.5)
    sense.set_pixels(image3)
    sleep(0.5)
    sense.show_message(go_message, speed)
    sleep(0.5)
    sense.clear()
    global sleep_time
    sleep_time = 0.1
    global difficulty
    difficulty = 2

while True:
        #coordenadas do ponto inicial da cobra e da maça
        x1 = randint(0, 7)
        y1 = randint(0, 7)
        x2 = randint(0, 7)
        y2 = randint(0, 7)

        pixeis_cobra = [[x1, y1]]

        ax1 = 0
        ay1 = 0

        # Iniciar o primeiro pixel com os valores aleatórios definidos anteriormente
        x1 = x1 - ax1 
        y1 = y1 - ay1

        t = 0

        sense.stick.get_events()

        while t == 0:
            for event in sense.stick.get_events():
                if event.action == 'pressed' and event.direction == 'right':
                    normal()
                    t = 1
                if event.action == 'pressed' and event.direction == 'left':
                    hard()
                    t = 1
                if event.action == 'pressed' and event.direction == 'down':
                    insane()
                    t = 1
                    

        drawApple()

        while True:
                x = pixeis_cobra[len(pixeis_cobra) - 1][0] + ax1
                y = pixeis_cobra[len(pixeis_cobra) - 1][1] + ay1
                pixeis_cobra = pixeis_cobra[1:len(pixeis_cobra)]
                if len(pixeis_cobra) > 1:
                    if [x,y] in pixeis_cobra:
                        print (str(x) + "/" + str(y))
                        break
                if x >= 8:
                    if difficulty == 0 or difficulty == 1:    
                        x = 0
                    elif difficulty == 2:
                        break
                if x <= -1:
                    if difficulty == 0 or difficulty == 1:      
                        x = 7
                    elif difficulty == 2:
                        break
                if y >= 8:
                    if difficulty == 0 or difficulty == 1:
                        y = 0
                    elif difficulty == 2:
                        break
                if y <= -1:
                    if difficulty == 0 or difficulty == 1:
                        y = 7
                    elif difficulty == 2:
                        break
                pixeis_cobra.append([x,y])
                drawSnake(x, y)
                sleep(sleep_time)
                #sense.clear()
                for event in sense.stick.get_events():
                    if event.action == 'pressed' and event.direction == 'up':
                        if len(pixeis_cobra) > 1:
                            if [x, y - 1] == pixeis_cobra[len(pixeis_cobra) - 2]:
                                None
                            else:
                                ax1 = 0
                                ay1 = -1
                        else:
                            ax1 = 0
                            ay1 = -1
                    if event.action == 'pressed' and event.direction == 'down':
                        if len(pixeis_cobra) > 1:
                            if [x, y + 1] == pixeis_cobra[len(pixeis_cobra) - 2]:
                                None
                            else:
                                ax1 = 0
                                ay1 = 1
                        else:
                            ax1 = 0
                            ay1 = 1
                    if event.action == 'pressed' and event.direction == 'right':
                        if len(pixeis_cobra) > 1:
                            if [x + 1, y] == pixeis_cobra[len(pixeis_cobra) - 2]:
                                None
                            else:
                                ax1 = 1
                                ay1 = 0
                        else:
                            ax1 = 1
                            ay1 = 0        
                    if event.action == 'pressed' and event.direction == 'left':
                        if len(pixeis_cobra) > 1:
                            if [x - 1, y] == pixeis_cobra[len(pixeis_cobra) - 2]:
                                None
                            else:
                                ax1 = -1
                                ay1 = 0
                        else:
                            ax1 = -1
                            ay1 = 0
                print(pixeis_cobra)
                #nova maçã qnd a cobra a come
                if pixeis_cobra[len(pixeis_cobra) - 1][0] == x2 and pixeis_cobra[len(pixeis_cobra) - 1][1] == y2:
                    drawApple()
                    temp = [[0,0]]
                    temp += pixeis_cobra
                    pixeis_cobra = temp
                    print (pixeis_cobra)
                else:
                    sense.set_pixel(pixeis_cobra[0][0], pixeis_cobra[0][1], (0, 0, 0))
                    
        message = "Game Over"
        message_2 = "NOOB!!"
        message_3 = "Not bad."
        message_4 = "MASTER!!"
        message_5 = "GOD!!"
        score = len(pixeis_cobra)
        message_6 = "score: " + str(score)
        speed = 0.05
        speed_2 = 0.03
        sense.show_message(message, speed, text_colour = o, back_colour = e)
        sense.show_message(message_6, speed, text_colour = b, back_colour = e)
        if score < 5:
            sense.show_message("kys", speed_2, text_colour = r, back_colour = e)
        if 5 < score < 10:
            sense.show_message(message_2, speed_2, text_colour = r, back_colour = e)
        elif 10 < score < 20:
            sense.show_message(message_3, speed_2, text_colour = r, back_colour = e)
        elif 20 < score < 30:
            sense.show_message(message_4, speed_2, text_colour = r, back_colour = e)
        elif score > 30:
            sense.show_message(message_5, speed_2, text_colour = r, back_colour = e)
            
        def say_my_name():
            username.set( my_name.get() )

        def say_my_score():
            score_message.set( my_score.get() )
            
        def say_welcome_message():
            welcome_message.set( welcome_message.get() )
            
        def do_booking():
            info("Score", "{0}, your score was \n {1}".format(my_name.get(), score) )

        app = App(title="Snake v0.1", width=400, height=450, layout="grid")
        welcome_message=Text(app, text="Snake", size=30, font="Algerian", color="darkgreen", grid=[0,2])
        my_name= TextBox(app, grid=[3,2])
        update_text = PushButton(app, command=do_booking, text="Username", grid=[4,2])

        my_snake = Picture(app, image="giphy (1).gif", grid=[1000,2])

        app.display()

        speed = 0.04
        
        sense.show_message("Restart press -> for normal, <- for hard or \!/ for insane  difficulty.", speed, text_colour = ye)

        
