from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

from random import randint

#Random Display

sense.set_rotation(180)

import Display


#Le Pergunts


import tkinter
import tkinter as tk
import tkinter.messagebox



top = tkinter.Tk()
def hello():
    result = tkinter.messagebox.askquestion("Parque Inteligente", "É de dia?")
    if result == "yes":
        result2 = tkinter.messagebox.askquestion("Parque Inteligente", "O lugar está ocupado?")
        if result2 == "yes":
            sense.show_message("Por favor dirija-se para um lugar disponivel",scroll_speed=0.05,text_colour=[190,190,0])

            
        else:
            sense.show_message("A carregar carro",scroll_speed=0.05,text_colour=[0,255,0])
            import Lol
            
    else:
        result3 = tkinter.messagebox.askquestion("Parque Inteligente", "A bateria tem carga?")
        if result3 == "yes":
            sense.show_message("A carregar carro",scroll_speed=0.05,text_colour=[0,255,0])
            import Lol
        else:
            result4 = tkinter.messagebox.askquestion("Parque Inteligente", "Existe algum lugar disponivel?")
            if result4=="yes":
                sense.show_message("Por favor dirija-se para um lugar disponivel",scroll_speed=0.05,text_colour=[190,190,0])
            else:
                sense.show_message("Lamentamos o incomodo mas o parque esta lotado",scroll_speed=0.05,text_colour=[255,10,0])
                    
            
B1 = tkinter.Button(top, text = "Park your car", command = hello)
B1.pack()

           

