from guizero import App
from guizero import Picture
import smtplib
import os
import sys
from getpass import getpass
from smtplib import SMTP_SSL
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from picamera import PiCamera
from time import sleep 
from sense_hat import SenseHat

camera = PiCamera()
sense = SenseHat()
i = 0

def busted():
        sense.show_message("BUSTED!!",scroll_speed=0.05, text_colour=[255, 0, 0], back_colour=[255, 255, 255])
                
def hiboss():
        sense.clear()
        sense.show_message("HI BOSS ;)",scroll_speed=0.08, text_colour=[0, 0, 255])

event = sense.stick.wait_for_event()
while True:
        acceleration = sense.get_accelerometer_raw()
        a = acceleration['x']
        b= acceleration['y']
        c = acceleration['z']


        a = abs(a)
        b = abs(b)
        c = abs(c)

        if a > 1 or b > 1 or c > 1:
                camera.capture('/home/pi/Desktop/imagens/image%s.gif' % i)
                busted()
                i = i + 1
                login, password = 'ujuniorifp@gmail.com', 'supersenha2017'
                recipients = [login]

                # create the email
                message = """This is a test...\nYEAHHHHHHHHHHHHHHHHHHHHHHHHHH"""
                msg = MIMEText(message, 'plain', 'utf-8')
                msg['Subject'] = Header('RPI...', 'utf-8')
                msg['From'] = 'My rpi <ujuniorifp@gmail.com>'
                msg['To'] = 'ujuniorifp@gmail.com'

                # send via gmail
                s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
                s.set_debuglevel(1)

                try:
                    s.login(login, 'supersenha2017')
                    s.sendmail(msg['From'], recipients, msg.as_string())
                finally:
                    s.quit()
        for event in sense.stick.get_events():
                if event.action == 'pressed':
                        hiboss()
                        app = App(title="hello world")
                        my_Picture = Picture(app, image='/home/pi/Desktop/imagens/image0.gif')
                        app.display()
                        quit()
                        
           

