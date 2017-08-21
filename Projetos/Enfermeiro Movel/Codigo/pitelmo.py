import socket 
import string
import time
import random
import os
import sys

from guizero import App, Text, Combo, ButtonGroup, PushButton, TextBox
from smtplib import SMTP_SSL
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from sense_hat import SenseHat

sense = SenseHat()

# funcao so pode ser "transmissor" ou "recetor"
funcao = "transmissor"

#comunicação com outro dispositivo
UDP_IP_OD = "10.250.4.123"
UDP_Port_OD = 8000

#comunicação com o meu dispositivo
UDP_IP_Meu = "10.250.3.103"
UDP_Port_Meu = 8000

global r, b, g, e, y, p, o

r = (255, 0, 0) #Febre
b = (0, 0, 255) #Hipotermia
g = (0, 255, 0) #Normalizado
e = (0, 0, 0) #Paragem Cardiaca
y = (255, 255, 0) #Hipertensão
p = (160, 32, 240) #Hipotensão
o = (255, 255, 255)#Borda

def tipo():
    global funcao
    funcao = escolhaenfermeiro.get()
    #print(funcao)
    app1.destroy()
    
#Interface
app1 = App(title="Escolha o tipo de Enfermeiro: ",width=150, height=100, layout="grid")
escolhaenfermeiro = Combo(app1, options=["transmissor", "recetor"], grid=[0,1])
descricaoenfermeiro = Text(app1, text="Tipos:", grid=[0,0],)
confirmar = PushButton(app1, command=tipo, text="Confirmar", grid=[3,1], align="left")

app1.display()

app = App(title="Enfermeiro Móvel", layout="grid")

welcome_message = Text(app, text="Enfermaria 1", size=40, font="Times New Roman", color="purple", grid=[0,0])
#print(funcao)


#imagem numeros para letras
def imessage(argument):
    switcher = {
        (255, 255, 255): "o",
        (0, 0, 255): "b",
        (0, 255, 0): "g",
        (0, 0, 0): "e",
        (255, 0, 0): "r",
        (255, 255, 0): "y",
        (160, 32, 240): "p",
        "o": (255, 255, 255),
        "b": (0, 0, 255),
        "g": (0, 255, 0),
        "e": (0, 0, 0),
        "r": (255, 0, 0),
        "y": (255, 255, 0),
        "p": (160, 32, 240),
        }
    func = switcher.get(argument, "nothing")
    return func

def geradoraleatorio():
    numero = random.randint(1, 60)
    r = (255, 0, 0) #Febre
    b = (0, 0, 255) #Hipotermia
    g = (0, 255, 0) #Normalizado
    e = (0, 0, 0) #Paragem Cardiaca
    y = (255, 255, 0) #Hipertensão
    p = (160, 32, 240) #Hipotensão
    o = (255, 255, 255)#Borda

    anomalia = True
    a = 1
    global imageString
    image = [o,o,o,o,o,o,o,o]
    imageString = "oooooooo"
    for x in range(6):
        image1 = [o,]
        imageString += "o"
        for z in range(6):
            numero = random.randint(1, 60)
            if numero == 1:
                num = r
                #print(1)
            elif numero == 2:
                num = b
                #print(2)
            elif numero == 3:
                num = p
                #print(3)
            elif numero == 4:
                num = e
                os.system('mpg123 musicas/Alarm\ v1.mp3')
                time.sleep(0.5)
                #print(4)
            elif numero == 5:
                num = y
                #print(5)
            else:
                num = g
            image1.append( num );
            imageString += imessage(num)
            
#Enviar email c/problemas e cama
            if num != g:
                login, password = 'projetoujunior@gmail.com', 'supersenha2017'
                recipients = [login]
                message = """Problema """
                if num == r:
                    anomalia = False
                    num = 'Febre'
                if num == b:
                    anomalia = False
                    num = 'Hipotermia'
                if num == p:
                    anomalia = False
                    num = 'Hipotensão'
                if num == e:
                    anomalia = False
                    num = 'Paragem Cardiaca'
                if num == y:
                    anomalia = False
                    num = 'Hipertensão'
                message += num
                msg = MIMEText(message, 'plain', 'utf-8')
                msg['Subject'] = Header('Problema na cama' + str(x*6+z+1),  'utf-8')
                
                #Problema Interface
                problem_message = Text(app, text='Problema na cama:', size=20, font="Times New Roman", color="blue", grid=[a,0])
                nproblem_message = Text(app, text='' + str(x*6+z+1), size=20, font="Times New Roman", color="red", grid=[a,1])
                problems_message = Text(app, text=' ' + str(num), size=20, font="Times New Roman", color="red", grid=[a,2])
                a+=1
                
                #Enviar email c/problemas e cama
                msg['From'] = 'My rpi <projetoujunior@gmail.com>'
                msg['To'] = 'projetoujunior@gmail.com'
                s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
                s.set_debuglevel(1)
                try:
                    s.login(login, 'supersenha2017')
                    s.sendmail(msg['From'], recipients, msg.as_string())
                finally:
                    s.quit()
            
        image1.append( o )
        imageString += "o"
        image.extend(image1)
    image2 = [o,o,o,o,o,o,o,o]
    imageString += "oooooooo"
    image.extend(image2)
    #print(len(imageString), imageString)
    #print(len(image), image)
    sense.set_pixels(image)
#interface nao ha anomalias
    if anomalia == True:
            noproblem_message = Text(app, text='Não existem anomalias', size=20, font="Times New Roman", color="green", grid=[1,0])

#recetor reforços
def Message(mensagem):
    Message = mensagem
    bytesMessage = bytes(Message, 'UTF-8')
    
    #print ("UDP target IP: ", UDP_IP_OD)
    #print ("UDP target port: ", UDP_Port_OD)
    #print ("message: ", Message) 
    
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    sock.sendto(bytesMessage, (UDP_IP_OD, UDP_Port_OD))

print(funcao)
if funcao == "transmissor":           
    geradoraleatorio()
    #print(funcao)
    app.display()
    Message(imageString)
    #transmissor de reforços
    while True:
        for event in sense.stick.get_events():
            #print(event.direction, event.action)
            if event.action == 'pressed':
                Message("reforcos")
                
elif funcao == "recetor":
    #espera por mensagem de reforços
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet UDP              
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((UDP_IP_Meu, UDP_Port_Meu))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        data = data.decode("UTF-8")
        print (data)
        if data != "reforcos":
            imagedata = []
            for i in range (64):
                imagedata.append(imessage(data[i]))
        sense.set_pixels(imagedata)




        
