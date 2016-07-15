#INTERFACE

import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import pygame, os
import time
from time import time, sleep
from pygame import *
from pygame.locals import *
from sense_hat import SenseHat
import ctypes 


sense = SenseHat ()


#Instruções
messagebox.showinfo(title="Instruções", message= "Incidentes: Para desencadear um roubo: roubo(x,y); Para desencadear um incêndio: incêndio(x,y).")


#Equipas Iniciais


messagebox.showinfo(title="Informação", message= "Equipas de Bombeiros: 5 ; Equipas de Polícias: 5 ; Equipas de Técnicos de Inundações: 5 ; Equipas de Técnicos de Falhas Elétricas: 5")




t = sense.get_temperature()
h = sense.get_humidity()

if (t > 35):

    messagebox.showinfo(title="Informação", message= "Os sensores de temperatura indicam que o dia de hoje é muito quente, o que pode provocar incêndios.As equipas de bombeiros na cidade serão alertadas e ligeiramente reforçadas. Alerta Amarelo! Número atual de equipas de bombeiros: 7")

elif (t > 45) and (h > 30):

    messagebox.showinfo(title="Informação", message= "Os sensores de temperatura indicam que o dia de hoje é extremamente quente e a humidade está próxima de zero. Estas condições aumentam a probabilidade de incêndio exponencialmente. As equipas de bombeiros na cidade serão alertadas e bastante reforçadas. Alerta Vermelho! Número atual de equipas de bombeiros: 11")

elif (t > 40):

    messagebox.showinfo(title="Informação", message= "Os sensores de temperatura indicam que o dia de hoje é muito quente, o que pode provocar incêndios. As equipas de bombeiros na cidade serão alertadas e reforçadas. Alerta Laranja!Número atual de equipas de bombeiros: 9")

elif (h > 60):

    messagebox.showinfo(title="Informação", message= "Nível de humidade bastante alto. Probabilidade de Inundação alta. Equipas reforçadas! Número atual de equipas de técnicos de Inundações: 7")



#Cores

v = [255, 0, 0]
g = [79, 79, 79]
bc = [0, 255, 255]
a = [255, 215, 0]
e = [0, 0, 0]
w = [255,255,255]



#Cidade

image= [
w,w,e,e,e,e,w,w,
w,w,e,w,w,e,w,w,
e,e,e,w,w,e,e,e,
w,w,e,e,w,w,e,w,
w,w,w,e,w,w,e,w,
e,e,e,e,e,e,e,e,
w,e,w,w,e,w,w,w,
w,e,w,w,e,w,w,w,
]


#Butões

#Cidade

def cidade():

    image= [
    w,w,e,e,e,e,w,w,
    w,w,e,w,w,e,w,w,
    e,e,e,w,w,e,e,e,
    w,w,e,e,w,w,e,w,
    w,w,w,e,w,w,e,w,
    e,e,e,e,e,e,e,e,
    w,e,w,w,e,w,w,w,
    w,e,w,w,e,w,w,w,
    ]

    sense.set_pixels(image)



    #Construir ou Demolir

def construir_demolir():

    global cons_dem
    cons_dem = tkinter.Tk()
    cons_dem.geometry("200x200")
    cons_dem.wm_title("Escolha as várias opções")
    b0 = ttk.Button(cons_dem, text = "Construir", command = construir_cidade)
    b1 = ttk.Button(cons_dem, text = "Demolir", command = demolir_cidade)

    b0.pack()
    b1.pack()



#Demolir

def demolir_cidade():

    global demo
    demo = tkinter.Tk()
    demo.geometry("200x200")
    demo.wm_title("Escolha as várias opções")
    b0 = ttk.Button(demo, text = "Demolir Apartamento", command = demolir_apartamento)
    b1 = ttk.Button(demo, text = "Demolir Reta Horizontal", command = demolir_linha_h)
    b2 = ttk.Button(demo, text = "Demolir Reta Vertical", command = demolir_linha_v)
    b3 = ttk.Button(demo, text = "Demolir Quarteirão (2x2)", command = demolir_quarteirao)
    b4 = ttk.Button(demo, text = "Demolir Tudo", command = demolir_tudo)

    b0.pack()
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()



#Demolir Apartamento

def demolir_apartamento():

    top = tkinter.Tk()
    top.wm_title("Coordenadas")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 

    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Demolir', command = d_apa)
    b1.pack()
    top.mainloop()

def d_apa():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())

    if (x <= 7 or x >= 0) and (y <= 7 or y >= 0):
         sense.set_pixel(x,y, e)



    #Demolir Linha Horizontal   

def demolir_linha_h():

    top = tkinter.Tk()
    top.wm_title("Coordenadas de um Ponto da Reta")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Demolir', command = d_li_h)
    b1.pack()
    top.mainloop()

def d_li_h():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())

    if x == 0:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x + 2, y, e),
        sense.set_pixel(x + 3, y, e),
        sense.set_pixel(x + 4, y, e),
        sense.set_pixel(x + 5, y, e),
        sense.set_pixel(x + 6, y, e),
        sense.set_pixel(x + 7, y, e)    
    elif x == 1:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x + 2, y, e),
        sense.set_pixel(x + 3, y, e),
        sense.set_pixel(x + 4, y, e),
        sense.set_pixel(x + 5, y, e),
        sense.set_pixel(x + 6, y, e),
        sense.set_pixel(x-1, y, e)
    elif x == 2:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x + 2, y, e),
        sense.set_pixel(x + 3, y, e),
        sense.set_pixel(x + 4, y, e),
        sense.set_pixel(x + 5, y, e),
        sense.set_pixel(x-2, y, e),
        sense.set_pixel(x-1, y, e)
                        
    elif x == 3:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x + 2, y, e),
        sense.set_pixel(x + 3, y, w),
        sense.set_pixel(x + 4, y, e),
        sense.set_pixel(x-3, y, e),
        sense.set_pixel(x-2, y, e),
        sense.set_pixel(x-1, y, e)
    elif x == 4:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x + 2, y, e),
        sense.set_pixel(x + 3, y, e),
        sense.set_pixel(x-4, y, e),
        sense.set_pixel(x-3, y, e),
        sense.set_pixel(x-2, y, e),
        sense.set_pixel(x-1, y, e)
    elif x == 5:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x + 2, y, e),
        sense.set_pixel(x-5, y, e),
        sense.set_pixel(x-4, y, e),
        sense.set_pixel(x-3, y, e),
        sense.set_pixel(x-2, y, e),
        sense.set_pixel(x-1, y, e)
    elif x == 6:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x + 1, y, e),
        sense.set_pixel(x-6, y, e)
        sense.set_pixel(x-5, y, e),
        sense.set_pixel(x-4, y, e),
        sense.set_pixel(x-3, y, e),
        sense.set_pixel(x-2, y, e),
        sense.set_pixel(x-1, y, e)
    elif x == 7:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x-7, y, e),
        sense.set_pixel(x-6, y, e),
        sense.set_pixel(x-5, y, e),
        sense.set_pixel(x-4, y, e),
        sense.set_pixel(x-3, y, e),
        sense.set_pixel(x-2, y, e),
        sense.set_pixel(x-1, y, e)




    #Demolir Linha Vertical

def demolir_linha_v():

    top = tkinter.Tk()
    top.wm_title("Coordenadas de um Ponto da Reta")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Demolir', command = d_li_v)
    b1.pack()
    top.mainloop()

def d_li_v():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())
    
    if y== 0:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y+2, e),
        sense.set_pixel(x, y+3, e),
        sense.set_pixel(x, y+4, e),
        sense.set_pixel(x, y+5, e),
        sense.set_pixel(x, y+6, e),
        sense.set_pixel(x, y+7, e)    
    elif y == 1:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y+2, e),
        sense.set_pixel(x, y+3, e),
        sense.set_pixel(x, y+4, e),
        sense.set_pixel(x, y+5, e),
        sense.set_pixel(x, y+6, e),
        sense.set_pixel(x, y-1, e)
    elif y == 2:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y+2, e),
        sense.set_pixel(x, y+3, e),
        sense.set_pixel(x, y+4, e),
        sense.set_pixel(x, y+5, e),
        sense.set_pixel(x, y-2, e),
        sense.set_pixel(x, y-1, e)
    elif y == 3:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y+2, e),
        sense.set_pixel(x, y+3, e),
        sense.set_pixel(x, y+4, e),
        sense.set_pixel(x, y-3, e),
        sense.set_pixel(x, y-2, e),
        sense.set_pixel(x, y-1, e)
    elif y == 4:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y+2, e),
        sense.set_pixel(x, y+3, e),
        sense.set_pixel(x, y-4, e),
        sense.set_
        pixel(x, y-3, e),
        sense.set_pixel(x, y-2, e),
        sense.set_pixel(x, y-1, e)
    elif y == 5:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y+2, e),
        sense.set_pixel(x, y-5, e),
        sense.set_pixel(x, y-4, e),
        sense.set_pixel(x, y-3, e),
        sense.set_pixel(x, y-2, e),
        sense.set_pixel(x, y-1, e)
    elif y == 6:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y+1, e),
        sense.set_pixel(x, y-6, e),
        sense.set_pixel(x, y-5, e),
        sense.set_pixel(x, y-4, e),
        sense.set_pixel(x, y-3, e),
        sense.set_pixel(x, y-2, e),
        sense.set_pixel(x, y-1, e)
    elif y == 7:
        sense.set_pixel(x,y, e),
        sense.set_pixel(x, y-7, e),
        sense.set_pixel(x, y-6, e),
        sense.set_pixel(x, y-5, e),
        sense.set_pixel(x, y-4, e),
        sense.set_pixel(x, y-3, e),
        sense.set_pixel(x, y-2, e),
        sense.set_pixel(x, y-1, e)



    #Demolir Quarteirão

def demolir_quarteirao():

    top = tkinter.Tk()
    top.wm_title("Coordenadas de um Ponto da Reta")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Demolir', command = d_li_v)
    b1.pack()
    top.mainloop()

def d_li_v():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())

    sense.set_pixel(x,y, e),
    sense.set_pixel(x + 1 ,y, e),
    sense.set_pixel(x, y + 1, e),
    sense.set_pixel(x+1, y+1, e)



    #Demolir Tudo 

def demolir_tudo():

    image= [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

    sense.set_pixels(image)



    #Construir

def construir_cidade():

    global cid
    cid = tkinter.Tk()
    cid.geometry("200x200")
    cid.wm_title("Escolha as várias opções")
    b0 = ttk.Button(cid, text = "Construir Apartamento", command = construir_apartamento)
    b1 = ttk.Button(cid, text = "Construir Reta Horizontal", command = construir_linha_h)
    b2 = ttk.Button(cid, text = "Construir Reta Vertical", command = construir_linha_v)
    b3 = ttk.Button(cid, text = "Construir Quarteirão (2x2)", command = construir_quarteirao)

    b0.pack()
    b1.pack()
    b2.pack()
    b3.pack()



    #Construir Apartamento

def construir_apartamento():

    top = tkinter.Tk()
    top.wm_title("Coordenadas")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Construir', command = apa)
    b1.pack()
    top.mainloop()

def apa():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())

    if (x <= 7 or x >= 0) and (y <= 7 or y >= 0):
        sense.set_pixel(x, y, w)



    #Contruir Linha Horizontal

def construir_linha_h():
    
    top = tkinter.Tk()
    top.wm_title("Coordenadas de um Ponto da Reta")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Construir', command = li_h)
    b1.pack()
    top.mainloop()

    
def li_h():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())

    if x == 0:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x + 2, y, w),
        sense.set_pixel(x + 3, y, w),
        sense.set_pixel(x + 4, y, w),
        sense.set_pixel(x + 5, y, w),
        sense.set_pixel(x + 6, y, w),
        sense.set_pixel(x + 7, y, w)    
    elif x == 1:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x + 2, y, w),
        sense.set_pixel(x + 3, y, w),
        sense.set_pixel(x + 4, y, w),
        sense.set_pixel(x + 5, y, w),
        sense.set_pixel(x + 6, y, w),
        sense.set_pixel(x-1, y, w)
    elif x == 2:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x + 2, y, w),
        sense.set_pixel(x + 3, y, w),
        sense.set_pixel(x + 4, y, w),
        sense.set_pixel(x + 5, y, w),
        sense.set_pixel(x-2, y, w),
        sense.set_pixel(x-1, y, w)
    elif x == 3:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x + 2, y, w),
        sense.set_pixel(x + 3, y, w),
        sense.set_pixel(x + 4, y, w),
        sense.set_pixel(x-3, y, w),
        sense.set_pixel(x-2, y, w),
        sense.set_pixel(x-1, y, w)
    elif x == 4:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x + 2, y, w),
        sense.set_pixel(x + 3, y, w),
        sense.set_pixel(x-4, y, w),
        sense.set_pixel(x-3, y, w),
        sense.set_pixel(x-2, y, w),
        sense.set_pixel(x-1, y, w)
    elif x == 5:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x + 2, y, w),
        sense.set_pixel(x-5, y, w),
        sense.set_pixel(x-4, y, w),
        sense.set_pixel(x-3, y, w),
        sense.set_pixel(x-2, y, w),
        sense.set_pixel(x-1, y, w)
    elif x == 6:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x + 1, y, w),
        sense.set_pixel(x-6, y, w),
        sense.set_pixel(x-5, y, w),
        sense.set_pixel(x-4, y, w),
        sense.set_pixel(x-3, y, w),
        sense.set_pixel(x-2, y, w),
        sense.set_pixel(x-1, y, w)
    elif x == 7:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x-7, y, w),
        sense.set_pixel(x-6, y, w),
        sense.set_pixel(x-5, y, w),
        sense.set_pixel(x-4, y, w),
        sense.set_pixel(x-3, y, w),
        sense.set_pixel(x-2, y, w),
        sense.set_pixel(x-1, y, w)



    #Construir Linha Vertical

def construir_linha_v():
    
    top = tkinter.Tk()
    top.wm_title("Coordenadas de um Ponto da Reta")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Construir', command = li_v)
    b1.pack()
    top.mainloop()
    

def li_v():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())

    if y== 0:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y+2, w),
        sense.set_pixel(x, y+3, w),
        sense.set_pixel(x, y+4, w),
        sense.set_pixel(x, y+5, w),
        sense.set_pixel(x, y+6, w),
        sense.set_pixel(x, y+7, w)    
    elif y == 1:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y+2, w),
        sense.set_pixel(x, y+3, w),
        sense.set_pixel(x, y+4, w),
        sense.set_pixel(x, y+5, w),
        sense.set_pixel(x, y+6, w),
        sense.set_pixel(x, y-1, w)
    elif y == 2:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y+2, w),
        sense.set_pixel(x, y+3, w),
        sense.set_pixel(x, y+4, w),
        sense.set_pixel(x, y+5, w),
        sense.set_pixel(x, y-2, w),
        sense.set_pixel(x, y-1, w)
    elif y == 3:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y+2, w),
        sense.set_pixel(x, y+3, w),
        sense.set_pixel(x, y+4, w),
        sense.set_pixel(x, y-3, w),
        sense.set_pixel(x, y-2, w),
        sense.set_pixel(x, y-1, w)
    elif y == 4:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y+2, w),
        sense.set_pixel(x, y+3, w),
        sense.set_pixel(x, y-4, w),
        sense.set_pixel(x, y-3, w),
        sense.set_pixel(x, y-2, w),
        sense.set_pixel(x, y-1, w)
    elif y == 5:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y+2, w),
        sense.set_pixel(x, y-5, w),
        sense.set_pixel(x, y-4, w),
        sense.set_pixel(x, y-3, w),
        sense.set_pixel(x, y-2, w),
        sense.set_pixel(x, y-1, w)
    elif y == 6:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y+1, w),
        sense.set_pixel(x, y-6, w),
        sense.set_pixel(x, y-5, w),
        sense.set_pixel(x, y-4, w),
        sense.set_pixel(x, y-3, w),
        sense.set_pixel(x, y-2, w),
        sense.set_pixel(x, y-1, w)
    elif y == 7:
        sense.set_pixel(x,y, w),
        sense.set_pixel(x, y-7, w),
        sense.set_pixel(x, y-6, w),
        sense.set_pixel(x, y-5, w),
        sense.set_pixel(x, y-4, w),
        sense.set_pixel(x, y-3, w),
        sense.set_pixel(x, y-2, w),
        sense.set_pixel(x, y-1, w)



        #Construir Quarteirão

def construir_quarteirao():

    top = tkinter.Tk()
    top.wm_title("Coordenadas do Canto Inferior Esquerdo")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Construir', command = const_quart)
    b1.pack()
    top.mainloop()


def const_quart():

    global e1
    global e2
   
    x = float(e1.get())
    y = float(e2.get())
   
    sense.set_pixel(x,y, w),
    sense.set_pixel(x + 1 ,y, w),
    sense.set_pixel(x, y + 1, w),
    sense.set_pixel(x+1,y+1, w)
    


    #Incendio

def incendio():

    top = tkinter.Tk()
    top.wm_title("Coordenadas")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = Button(top, text = 'Criar', command = inc)
    b1.pack()
    top.mainloop()
    
def inc():

    global e1
    global e2
    
    x = int(e1.get())
    y = int(e2.get())
    

    if (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==w):
        sense.set_pixel(x,y, v),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(2),
        sense.set_pixel(x,y, w),
        messagebox.showinfo(title="Informação", message="Os bombeiros chegaram ao local!")

    elif (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==e):
        sense.set_pixel(x,y, v),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, v),
        sleep(2),
        sense.set_pixel(x,y, e),
        messagebox.showinfo(title="Informação", message="Os bombeiros chegaram ao local!")
    
    
    
    
    #Inundação

def inundacao():

    top = tkinter.Tk()
    top.wm_title("Coordenadas")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = ttk.Button(top, text = 'Criar', command = inu)
    b1.pack()
    top.mainloop()
    
def inu():
    
    global e1
    global e2
    
    x = int(e1.get())
    y = int(e2.get())
    

    if (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==w):
        sense.set_pixel(x,y, bc),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(2),
        sense.set_pixel(x,y, w),
        messagebox.showinfo(title="Informação", message="Os técnicos chegaram ao local!")

    elif (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==e):
        sense.set_pixel(x,y, bc),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, bc),
        sleep(2),
        sense.set_pixel(x,y, e),
        messagebox.showinfo(title="Informação", message="Os técnicos chegaram ao local!")
    


    #Falha Elétrica

def eletrica():

    top = tkinter.Tk()
    top.wm_title("Coordenadas")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = ttk.Button(top, text = 'Criar', command = fal)
    b1.pack()
    top.mainloop()
    
def fal():
    
    global e1
    global e2
    
    x = int(e1.get())
    y = int(e2.get())
    

    if (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==w):
        sense.set_pixel(x,y, a),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(2),
        sense.set_pixel(x,y, w),
        messagebox.showinfo(title="Informação", message="Os técnicos chegaram ao local!")

    elif (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==e):
        sense.set_pixel(x,y, a),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, a),
        sleep(2),
        sense.set_pixel(x,y, e),
        messagebox.showinfo(title="Informação", message="Os técnicos chegaram ao local!")

    

    #Roubo

def roubo():

    top = tkinter.Tk()
    top.wm_title("Coordenadas")
    l1 = Label(top, text="Indique o X:")
    l1.pack()
    global e1
    e1 = Entry(top, bd =5)
    e1.pack()
    l2 = Label(top, text="Indique o Y:")
    l2.pack() 
    global e2
    e2 = Entry(top, bd =5)
    e2.pack()
    b1 = ttk.Button(top, text = 'Criar', command = rou)
    b1.pack()
    top.mainloop()
    
def rou():
    
    global e1
    global e2
    
    x = int(e1.get())
    y = int(e2.get())
    

    if (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==w):
        sense.set_pixel(x,y, g),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(0.5),
        sense.set_pixel(x,y, w),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(2),
        sense.set_pixel(x,y, w),
        messagebox.showinfo(title="Informação", message="A polícia chegou ao local!")



    elif (x <= 7 or x >= 0) and (y <= 7 or y >= 0) and (image[8*y+x]==e):
        sense.set_pixel(x,y, g),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(0.5),
        sense.set_pixel(x,y, e),
        sleep(0.5),
        sense.set_pixel(x,y, g),
        sleep(2),
        sense.set_pixel(x,y, e),
        messagebox.showinfo(title="Informação", message="A polícia chegou ao local!")



#Botões Iniciais (init)

root = tkinter.Tk()
root.geometry("400x400")
root.wm_title("SIM City")
b1 = ttk.Button(root, text = 'Cidade Pré-Definida', command = cidade)
b2 = ttk.Button(root, text = "Construa a sua própria cidade", command = construir_demolir)
b3 = ttk.Button(root, text = 'Incêndio', command = incendio)
b4 = ttk.Button(root, text = 'Inundação', command = inundacao)
b5 = ttk.Button(root, text = 'Falha Elétrica', command = eletrica)
b6 = ttk.Button(root, text = 'Roubo', command = roubo)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()




