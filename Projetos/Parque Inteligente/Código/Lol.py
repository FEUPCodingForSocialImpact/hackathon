import tkinter as tk
from tkinter import *
import tkinter.messagebox

import time

from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(180)

class SampleApp(tk.Tk):
    def __init__(self):
        master = Tk()
        Label(master, text="Qual a percentagem da sua bateria?").grid(row=0)
        self.entry = Entry(master)
        self.entry.grid(row = 0, column = 1)
        Button(master,text = "Confirme", command = self.on_button).grid(row=1, column=0,sticky=W, pady=4)

    def on_button(self):
   
        percentagem_inicial = int(self.entry.get())
        percentagem = 100-percentagem_inicial
        timee = percentagem * 300/100
        msg = "Ira demorar %s minutos ate o seu carro estar carregado" % (timee)
        print (msg)
        sense.show_message (msg, scroll_speed=0.045)

        Roy=percentagem_inicial/100
        while Roy < 1:
            import time
            RoyR = round(255 * (1-Roy))
            RoyG = round(255 * Roy)
            e =[0,0,0]
            g = [0,255,0]
            p = [RoyR, RoyG, 0]

            image = [
            e,e,e,e,e,e,e,e,
            e,e,e,g,e,e,e,e,
            e,g,e,e,e,e,g,e,
            e,e,e,g,e,e,e,e,
            g,e,e,e,e,e,g,e,
            e,e,e,p,e,g,e,e,
            g,e,e,e,e,e,e,g,
            e,e,g,e,e,g,e,e
            ]

            sense.set_pixels(image)
                          
            Roy = Roy + 0.05

            time.sleep(0.6)
            

        price = round((percentagem * 15.84)/100, 2)

        time.sleep(1)

        msg2 = "O custo total e de %s euros. Obrigado :) !" % (price)
        print(msg2)
        sense.show_message (msg2, scroll_speed=0.045)



app = SampleApp()
