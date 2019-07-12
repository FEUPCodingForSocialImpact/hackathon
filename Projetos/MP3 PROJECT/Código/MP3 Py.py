import serial
import time
import random
from sense_hat import SenseHat

PORT = "/dev/ttyACM0y"

##
BAUD = 115200
s = serial.Serial(PORT, timeout=0)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

sense = SenseHat()

playing = False

songs = ['Despacito', 'Star Wars', 'Shooting Stars', 'Mario']

playlist = []

def play_song(nome):
    s.write('{}\n'.format(nome).encode('UTF-8'))
    time.sleep(1)
    reply = s.readline().decode('UTF-8').rstrip()
    if reply == 'started':
        playing = True
        playlisting = True
    while playing:
        reply = s.readline().decode('UTF-8').rstrip()
        if reply == 'ended':
            playing = False
            break
        sense.show_message(nome)

while True:
    print('Escreva o nome da música: ')
    nome = input()
    if nome == 'random':
        nome = random.choice(songs)
    elif nome == 'playlist':
        print('Escreva o nome da música para a playlist: ')
        nome = input()
        while nome != '':
            playlist.append(nome)
            print('Escreva o nome da música para a playlist: ')
            nome = input()
        for nome in playlist:
            play_song(nome)
    play_song(nome)
