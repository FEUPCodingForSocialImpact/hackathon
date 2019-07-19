from random import randint
from sense_hat import SenseHat
sense = SenseHat()
import serial
import time
import os
dataArr = []
tempArr = []
timeArr = []
myCmd = os.popen('ls /dev/ttyA*').read() 
if 'ACM0' in myCmd:
    PORT = "/dev/ttyACM0"
if 'ACM1' in myCmd:
    PORT = "/dev/ttyACM1"
if 'ACM2' in myCmd:
    PORT = "/dev/ttyACM2"
if 'ACM3' in myCmd:
    PORT = "/dev/ttyACM3"
if 'ACM' not in myCmd:
    print('Ligue o micro:bit ao Raspberry Pi e reinicie o programa.')
    time.sleep(1)
    exit()
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
while True:
    print('Abane o micro:bit para ler a temperatura atual.')
    print('Adicionar esta temperatura à lista? (s/n para terminar)') 
    will_to_continue = input()
    if will_to_continue == 's':
        myCmd = os.popen('ls /dev/ttyA*').read()
        dataTemp = s.readline().decode('ISO-8859-1').rstrip()
        dataArr.append(dataTemp)
        sense.show_message(dataTemp, text_colour = [150, 150, 150], back_colour = [0, 100, 35])
        temp, time = dataTemp.split(' C - ', 1)
        tempArr.append(int(temp))
        timeArr.append(time)
    else:
        try:
            print(dataArr)
            media = int(round(sum(tempArr) / len(tempArr)))
            print('Média = ' + str(media))
            sense.clear()
            break
        except ZeroDivisionError:
            sense.clear()
            break
