from guizero import App
from guizero import App,Picture, Text
app = App(title="PingPong Arcade")
creditos = Text(app, text="UJr 2017 - FEUP - Hackathon", size=10, font="Roboto", color="black")
welcome_message = Text(app, text="Press joystick", size=40, font="Roboto Light", color="red")

senhor_inteligente = Picture(app, image="rsz_1batata.gif")


help = Text(app, text="Have Fun", size=20, font="Roboto Light", color="blue")
creditos = Text(app, text="Bruno Mendes", size=10, font="Roboto", color="black")
creditos = Text(app, text="Diogo Pires", size=10, font="Roboto", color="black")
creditos = Text(app, text="Gelson Martins", size=10, font="Roboto", color="black")
creditos = Text(app, text="Maria Terraços", size=10, font="Roboto", color="black")

app.display()
