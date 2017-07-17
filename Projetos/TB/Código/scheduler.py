import time 
import datetime
from sense_hat import SenseHat
from time import strftime
from time import sleep
import vlc
from guizero import App, Combo, Text, TextBox, PushButton, Slider, Picture
sense=SenseHat()
events=[]


def neve():
    global n
    n = optnome2.get()
    n = int(n)

def submeter():
    global name, date, time, reminder, events
    event = []
    name = optnome.get()
    day = int(optdia.get())
    month = int(optmes.get())
    year = int(optano.get())
    time=str(opthora.get() + ":" + optmindec.get() + optminuni.get() + " " + optampm.get())
    now_strf = strftime("%I:%M %P")
    reminder = str(opthora2.get() + ":" + optmindec2.get() + optminuni2.get() + " " + optampm2.get())
    date=datetime.date(year, month, day)
    event.append(name)
    event.append(str(date))
    event.append(str(time))
    event.append(reminder)
    events.append(event)

    app2.destroy()

    
    

def abrir_jan():
    app.destroy()
    neve()
    for i in range(n):
        global app2
        app2 = App(title="Criar evento", width=380, height=260, layout="grid")
        #Nome
        global optnome
        lbnome = Text(app2, text="Nome", grid=[0,0], align="left")
        optnome = TextBox(app2, grid=[0,1], align="left")

        #Data
        global optdia, optmes, optano
        lbdia = Text(app2, text="Dia", grid=[1,0], align="left")
        optdia = TextBox(app2, grid=[2,0], align="left")
        lbmes = Text(app2, text="Mes", grid=[1,1], align="left")
        optmes = TextBox(app2, grid=[2,1], align="left")
        lbano = Text(app2, text="Ano", grid=[1,2], align="left")
        optano = TextBox(app2, grid=[2,2], align="left")

        #Hora
        global opthora, optmindec, optminuni, optampm
        lbhora = Text(app2, text="Hora", grid=[3,0], align="left")
        opthora = Combo(app2, options=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], grid=[4,0], align="left")
        lbminuto = Text(app2, text="Minuto", grid=[3,1], align="left")
        optmindec = Combo(app2, options=["0", "1", "2", "3", "4", "5"], grid=[4,1], align="left") 
        optminuni = Combo(app2, options=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], grid=[4,2], align="left")
        lbampm = Text(app2, text="AM/PM", grid=[3,3], align="left")
        optampm = Combo(app2, options=["am", "pm"], grid=[4,3], align="left")

        #Lembrete
        lbnome = Text(app2, text="--Lembrete--", grid=[5,0], align="left")

        #HoraLembrete
        global opthora2, optmindec2, optminuni2, optampm2
        lbhora = Text(app2, text="Hora", grid=[6,0], align="left")
        opthora2 = Combo(app2, options=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], grid=[7,0], align="left")
        lbminuto = Text(app2, text="Minuto", grid=[6,1], align="left")
        optmindec2 = Combo(app2, options=["0", "1", "2", "3", "4", "5"], grid=[7,1], align="left") 
        optminuni2 = Combo(app2, options=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], grid=[7,2], align="left")
        lbampm = Text(app2, text="AM/PM", grid=[6,3], align="left")
        optampm2 = Combo(app2, options=["am", "pm"], grid=[7,3], align="left")

        #Botao
        btsub = PushButton(app2, command=submeter, text="Submeter", grid=[8,0], align="left")

        app2.display()

#Janela1
app = App(title="TB", width=210, height=75, layout="grid")
#Nome
lbnome2 = Text(app, text="Nº de eventos:", grid=[0,0], align="left")
optnome2 = TextBox(app, grid=[0,1], align="left")


#Botao
btsub2 = PushButton(app, command=abrir_jan, text="Submeter", grid=[8,0], align="left")

app.display()

b=[0, 0, 0]
w=[255, 255, 255]

sense.show_message("Clique para continuar")
sense.stick.wait_for_event()

i=0
while True:
    sense.show_message((events[i])[0])
    
    for event in sense.stick.get_events():
        if event.action=="pressed" and event.direction=="middle":
            sense.show_message((events[i])[0]+" "+(events[i])[1]+" "+(events[i])[2])
            a=True
            while a==True:
                now_strf = strftime("%I:%M %P")
                if reminder == now_strf:
                    sense.show_message("Ring!")
                    player = vlc.MediaPlayer("alarmb.mp3")
                    player.play()
                    sleep(1)
                    for event in sense.stick.get_events():
                        if event.action=="pressed" and event.direction=="middle":
                            player.stop()
                            a=False
        else:
            if event.action=="pressed" and event.direction=="down":
                i+=1
                if i>len(events)-1:
                    i=0
                sense.show_message((events[i])[0])
            else:
                if event.action=="pressed" and event.direction=="up":
                    i-=1
                    if i<0:
                        i=len(events)-1
                              
                    sense.show_message((events[i])[0])
