# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()
import csv
from datetime import datetime
from sense_hat import SenseHat
sense = SenseHat()
import time
from datetime import datetime

root.title("Casa Inteligente")

now = datetime.now()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

opt1 = OptionMenu(root, var1, 'Verao', 'Primavera', 'Outono', 'Inverno')   
opt2 = OptionMenu(root, var2, 13, 14, 15, 16, 17, 18, 19)
opt3 = OptionMenu(root, var3, 20, 21, 22, 23, 24, 25, 26)                 

opt1.pack(fill=X)
opt2.pack(fill=X)
opt3.pack(fill=X)

var1.set('Estação do Ano')
var2.set('Temp. Mínima')
var3.set('Temp. Máxima')

y = [255,255,0]
e = [0,0,0]
f = [125,0,0]
l = [255,127,0]
c = [92,51,23]
j = [255,255,255]
o = [255,0,0]
v = [0,255,0]
r = [255,20,147]

vera = [
e,e,e,e,e,e,e,e,
y,e,e,y,e,e,y,e,
e,y,e,y,e,y,e,e,
e,e,y,y,y,e,e,e,
y,y,y,y,y,y,y,e,
e,e,y,y,y,e,e,e,
e,y,e,y,e,y,e,e,
y,e,e,y,e,e,y,e
]

outono = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,c,e,c,
e,c,c,e,e,e,c,e,
e,e,e,c,e,c,e,e,
e,e,e,c,c,e,e,e,
e,e,e,c,c,e,e,e,
l,f,l,c,c,l,f,l,
f,l,f,c,c,f,l,f
]

inverna = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,o,o,e,
e,e,e,e,o,o,e,j,
e,e,e,o,o,o,e,e,
e,e,o,o,o,o,e,e,
e,o,o,o,o,o,o,e,
e,j,j,j,j,j,j,e,
e,e,e,e,e,e,e,e
]

primavera = [
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,e,r,y,y,r,e,e,
e,e,r,y,y,r,e,e,
e,e,e,r,r,e,e,e,
e,e,e,v,v,e,v,e,
e,e,e,v,v,v,e,e,
e,e,e,v,v,e,e,e,
]

#t = sense.get_temperature()
#t = round(t, 1)
t = input('Qual a temperatura atual?')

#realtime = '%s:%s' % (now.hour, now.minute)
realtime= input("Que horas são?")

fields = 'Despertador', 'Luzes', 'Janelas', 'Máquina de Café', 'Máquina de Lavar Louça', 'Máquina de Lavar Roupa'

def fetch(entries):
    all_entries=[]
    
    for i in range(0,len(entries)):
        current_entry=entries[i]
        all_entries.append(current_entry.get())

    if all_entries[0] == realtime:
        print 'Tocando o Despertador'
    elif all_entries[1] == realtime:
        print 'Acendendo as Luzes'
    elif all_entries[2] == realtime:
        print 'Abrindo as Janelas'
    elif all_entries[3] == realtime:
        print 'Ligando a Máquina de Café'
    elif all_entries[4] == realtime:
        print 'Ligando a Máquina de Lavar Louça'
    elif all_entries[5] == realtime:
        print 'Ligando a Máquina de Lavar Roupa'

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)                  
        lab = Label(row, width=20, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)           
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)
    return entries

def show(entries):
    fetch(entries)
    popup.destroy()


def ask():
    global popup
    popup = Toplevel()
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda e=ents: show(e)) ).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()


def state():
    if var1.get() == 'Verao':
        sense.set_pixels(vera)
    elif var1.get() == 'Outono':
        sense.set_pixels(outono)
    elif var1.get() == 'Inverno':
        sense.set_pixels(inverna)
    elif var1.get() == 'Primavera':
        sense.set_pixels(primavera)

    if t<int(var2.get()):
        print ('Ligando o Aquecedor')
    elif t>int(var3.get()):
        print ('Ligando o Arcondicionado')
    elif int(var2.get())<t and t<int(var3.get()):
        print ('Temperatura ideal')

Button(root, text='Definir Horários', command=ask).pack()
Button(root, command=state, text='Confirmar').pack()

root.mainloop()
