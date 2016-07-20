from sense_hat import SenseHat
import time
import random
from tkinter import messagebox 
from tkinter import *
title="SMARTJETAS"

root = Tk()

sense=SenseHat()

root.wm_title("SMARTJETAS")

b=[102,59,0]
e=[0,0,0]
g=[0,255,0]
a=[0,0,255]
l=[200,120,0]
i=[125,125,0]
v=[255,0,0]
w=[255,255,255]


imagetrash1= [
    b,e,e,e,e,e,e,b,
    b,b,e,e,e,e,b,b,
    e,b,e,a,a,a,b,e,
    e,b,a,a,a,a,b,e,
    e,b,a,a,a,a,b,e,
    e,b,a,g,a,g,b,e,
    e,b,g,g,g,g,b,e,
    e,b,e,e,e,e,b,e,
    ]

imagetrash2= [

    b,e,e,e,e,e,e,b,
    b,b,e,e,e,e,b,b,
    e,b,e,e,e,e,b,e,
    e,b,e,a,e,a,b,e,
    e,b,a,a,a,a,b,e,
    e,b,a,g,a,g,b,e,
    e,b,g,g,a,g,b,e,
    e,b,e,a,a,a,b,e,
    ]
imagetrash3= [
    b,e,e,e,e,e,e,b,
    b,b,e,e,e,e,b,b,
    e,b,e,e,e,e,b,e,
    e,b,a,e,a,e,b,e,
    e,b,a,a,a,a,b,e,
    e,b,g,a,a,g,b,e,
    e,b,g,a,a,g,b,e,
    e,b,a,a,a,a,b,e,
    ]

imageclean= [
    b,e,e,e,e,e,e,b,
    b,b,e,e,e,e,b,b,
    e,b,e,e,e,e,b,e,
    e,b,e,e,e,e,b,e,
    e,b,e,e,e,e,b,e,
    e,b,a,e,a,e,b,e,
    e,b,a,a,a,a,b,e,
    e,b,a,a,a,a,b,e,
    ]




MAPA = [
    w,w,w,w,w,w,w,w,
    w,a,a,a,a,a,a,w,
    w,a,a,a,a,a,a,w,
    w,a,a,a,a,a,a,w,
    w,a,a,a,a,a,a,w,
    w,a,a,a,a,a,a,w,
    w,a,a,a,a,a,a,w,
    w,w,w,w,w,w,w,w,  
    ]
       


sense.set_pixels (MAPA)

x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]
r=random.choice(x[0:6])
z=random.choice(y[0:6])



co=[9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]

def sujar():
        while True:
                ca=random.choice(co)
                if MAPA[ca]==a:
                   MAPA.pop(ca)
                   MAPA.insert(ca,i)
                   sense.set_pixels(MAPA)
                elif MAPA[ca]==i:
                    MAPA.pop(ca)
                    MAPA.insert(ca,l)
                    sense.set_pixels(MAPA)
                elif MAPA[ca]==l:
                    MAPA.pop(ca)
                    MAPA.insert(ca,v)
                    sense.set_pixels(MAPA)
                elif MAPA[ca]==v:
                        break
                #time.sleep(0.5)


"""Rua1=[9,10,11,12,13,14]
Rua2=[17,18,19,20,21,22]
Rua3=[25,26,27,28,29,30]
Rua4=[33,34,35,36,37,38]
Rua5=[41,42,43,44,45,46]
Rua6=[49,50,51,52,53,54]"""



lines=['Rua1','Rua2','Rua3','Rua4','Rua5','Rua6']
    
def limpar_rua(up):
        ru=lines.index(up)
        if ru==0:
            del MAPA[9:15]
            for n in range(0,6):
                MAPA.insert(9+n,a)
        elif ru==1:
                del MAPA[17:23]
                for n in range(0,6):
                        MAPA.insert(17+n,a)
        elif ru==2:
                del MAPA[25:31]
                for n in range(0,6):
                        MAPA.insert(25+n,a)
        elif ru==3:
                del MAPA[33:39]
                for n in range(0,6):
                        MAPA.insert(33+n,a)
        elif ru==4:
                del MAPA[41:47]
                for n in range(0,6):
                        MAPA.insert(41+n,a)
        elif ru==5:
                del MAPA[49:55]
                for n in range(0,6):
                        MAPA.insert(49+n,a)
                
        sense.set_pixels(MAPA)

def mostrar_estado(ca):
        if MAPA[ca]==a:
                sense.set_pixels(imageclean)
                messagebox.showinfo(title="SMARTJETAS", message= ("A sarjeta está em bom estado"))
        elif MAPA[ca]==i:
                sense.set_pixels(imagetrash3)
                messagebox.showinfo(title="SMARTJETAS", message= ("A sarjeta está ligeiramente suja"))
        elif MAPA[ca]==l:
                sense.set_pixels(imagetrash2)
                messagebox.showinfo(title="SMARTJETAS", message= ("A sarjeta está suja"))
        elif MAPA[ca]==v:
                sense.set_pixels(imagetrash1)
                messagebox.showinfo(title="SMARTJETAS", message= ("A sarjeta está entupida"))

def mostrar_mapa():
        sense.set_pixels(MAPA)

        
Button(root, text='Sujar', command=sujar).grid(row=0, column=0)

for n, k in enumerate (['Rua1','Rua2','Rua3','Rua4','Rua5','Rua6']):
        la=Button(root, text=k, command=lambda up=k: limpar_rua(up)).grid(row=0+n, column=1)

dotsa=['A1','A2','A3','A4','A5','A6']
dotsb=['B1','B2','B3','B4','B5','B6']
dotsc=['C1','C2','C3','C4','C5','C6']
dotsd=['D1','D2','D3','D4','D5','D6']
dotse=['E1','E2','E3','E4','E5','E6']
dotsf=['F1','F2','F3','F4','F5','F6']




"""v = IntVar()

Checkbutton(root, text="Limpar", variable=v).grid(row=3, column=0)
Checkbutton(root, text="Mostrar detalhes", variable=v).grid(row=2, column=0)"""
        
def mostrar_limpar():
        for n, k in enumerate (['A1','A2','A3','A4','A5','A6']):
                Button(root, text=k, command=lambda up=k: limpara(up)).grid(row=0, column=2+n)
                def limpara(up):
                        u=dotsa.index(up)
                        del MAPA[9+u]
                        MAPA.insert(9+u,a)
                        sense.set_pixels(MAPA)
        for n, k in enumerate (['B1','B2','B3','B4','B5','B6']):
                Button(root, text=k, command=lambda up=k: limparb(up)).grid(row=1, column=2+n)
                def limparb(up): 
                        u=dotsb.index(up)
                        del MAPA[17+u]
                        MAPA.insert(17+u,a)
                        sense.set_pixels(MAPA)
        for n, k in enumerate (['C1','C2','C3','C4','C5','C6']):
                Button(root, text=k, command=lambda up=k: limparc(up)).grid(row=2, column=2+n)
                def limparc(up):
                        u=dotsc.index(up)
                        del MAPA[25+u]
                        MAPA.insert(25+u,a)
                        sense.set_pixels(MAPA)
        for n, k in enumerate (['D1','D2','D3','D4','D5','D6']):
                Button(root, text=k, command=lambda up=k: limpard(up)).grid(row=3, column=2+n)
                def limpard(up):
                        u=dotsd.index(up)
                        del MAPA[33+u]
                        MAPA.insert(33+u,a)
                        sense.set_pixels(MAPA)
        for n, k in enumerate (['E1','E2','E3','E4','E5','E6']):
                Button(root, text=k, command=lambda up=k: limpare(up)).grid(row=4, column=2+n)
                def limpare(up):
                        u=dotse.index(up)
                        del MAPA[41+u]
                        MAPA.insert(41+u,a)
                        sense.set_pixels(MAPA)
        for n, k in enumerate (['F1','F2','F3','F4','F5','F6']):
                Button(root, text=k, command=lambda up=k: limparf(up)).grid(row=5, column=2+n)
                def limparf(up):
                        u=dotsf.index(up)
                        del MAPA[49+u]
                        MAPA.insert(49+u,a)
                        sense.set_pixels(MAPA)

def Mostrar_estado():
        for n, k in enumerate (['A1','A2','A3','A4','A5','A6']):
                Button(root, text=k, command=lambda na=n: mostrar_estado(9+na)).grid(row=0, column=2+n)

        for n, k in enumerate (['B1','B2','B3','B4','B5','B6']):
                Button(root, text=k, command=lambda na=n: mostrar_estado(17+na)).grid(row=1, column=2+n)

        for n, k in enumerate (['C1','C2','C3','C4','C5','C6']):
                Button(root, text=k, command=lambda na=n: mostrar_estado(25+na)).grid(row=2, column=2+n)

        for n, k in enumerate (['D1','D2','D3','D4','D5','D6']):
                Button(root, text=k, command=lambda na=n: mostrar_estado(33+na)).grid(row=3, column=2+n)

        for n, k in enumerate (['E1','E2','E3','E4','E5','E6']):
                Button(root, text=k, command=lambda na=n: mostrar_estado(41+na)).grid(row=4, column=2+n)

        for n, k in enumerate (['F1','F2','F3','F4','F5','F6']):
                Button(root, text=k, command=lambda na=n: mostrar_estado(49+na)).grid(row=5, column=2+n)


Button(root, text='Mostrar Limpar', command=lambda: mostrar_limpar()).grid(row=1, column=0)

Button(root, text='Mostrar Estados', command=lambda: Mostrar_estado()).grid(row=2, column=0)

Button(root, text='Mostrar Mapa', command=lambda: mostrar_mapa()).grid(row=3, column=0)

"""listbox = Listbox(root)
listbox.grid()


def Tabela():
        for item in ["Chamar Técnico", "Mostrar detalhes"]:
            listbox.insert(END, item)
            SIM=item.index("Chamar Técnico")
            return SIM"""


    


Button(root, text='Quit', command=root.destroy).grid(row=4, column=0)

root.mainloop()
