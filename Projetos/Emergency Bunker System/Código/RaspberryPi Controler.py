#Bibliotecas
from sense_hat import SenseHat
import serial
import time
from time import sleep

#Variáveis
format_string = '{}\n'
t=0
x=[]
a=''
X=[0,255,0]
O=[0,0,0]
y='g'
p='STAR WARS'
v='GAMES'

#Listas
morse=['.-', '-...', '-.-.', '-..', '.', '..-.','--.' ,'....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','.--.-.','.-.-.-','--..--','..--..','.----.','-.-.--','-..-.','-.--.','-.--.-','.-...','---...','-.-.-.','-...-','.-.-.','-....-','..--.-','.-..-.','...-..-']
alfabeto=['A',  'B',  'C',  'D',  'E',  'F',  'G',  'H', 'I',  'J',  'K ', 'L',  'M',  'N',  'O',  'P',  'Q',  'R',  'S',  'T',  'U',  'V', 'W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','@','.',',','?' ,"'" ,'!' ,'/' ,'(' ,')' ,'&' ,':' ,';','=','+','-','_','"' ,'$']
frase=[]

## Edit the line below to the correct port
PORT = "/dev/ttyACM0"
##
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
sense = SenseHat()

#Start
while True:
    lights = [
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X
            ]
    sense.set_pixels(lights) 
    data = s.readline().decode('UTF-8').rstrip()
    if data=='HELP':                                                                                    #HElP
        s.write(format_string.format(data).encode('UTF-8'))
        print(data)
        sense.show_message(data, text_colour=(0,0,255 ), back_colour=(0,255,0))
        s.write(format_string.format(y).encode('UTF-8'))
        k=(' ')
        t=0
    elif data=='FIRE':                                                                                  #FIRE       
        s.write(format_string.format(data).encode('UTF-8'))
        print(data)
        sense.show_message(data, text_colour=(255,0,0), back_colour=(0, 0, 0))
        s.write(format_string.format(y).encode('UTF-8'))
        k=(' ')
        t=0
    elif data=='EARTHQUAKE':                                                                            #EARTHQUAKE 
        s.write(format_string.format(data).encode('UTF-8'))
        print(data)
        sense.show_message(data, text_colour=(255,255,0), back_colour=(74,0,0))
        s.write(format_string.format(y).encode('UTF-8'))
        k=(' ')
        t=0
    elif data=='.':                                                                                      #A (.)
        print(data)
        k=('.')
        s.write(format_string.format(y).encode('UTF-8'))
        t=0
    elif data=='ROOM':                                                                                   #ROOM
        print(data)
        s.write(format_string.format('ROOM').encode('UTF-8'))
        k=' '
        t=t+1
    else:                                                                                                 #B (-)
        print(data)
        k=('-')
        s.write(format_string.format(y).encode('UTF-8'))
        t=0
        
    if k!=' ':
        x.append(k)                                                                                           #x
    else:
        for i in x:
            a=a+i
        if a not in morse and a!=' ':
            s.write(format_string.format('ERROR').encode('UTF-8'))
        else:                                                                                               #a
            n=morse.index(a)
            frase.append(alfabeto[n])            
            for w in range(len(frase)):
                if w == (len(frase)-1):
                    print(frase[w])
                else:
                    print((frase[w]),  end='')
        a=''
        x=[]
    if t==2:
        t=0
        if frase==['S', 'T', 'A', 'R', 'W', 'A', 'R', 'S']:                                             #Star Wars
            s.write(format_string.format(p).encode('UTF-8'))
            sense.show_message((p,p,p), text_colour=(0,0,0), back_colour=(236,214,0))
                
        elif frase==['G','A']:                                                                            #Games 
            s.write(format_string.format(v).encode('UTF-8'))
            sense.show_message(v, text_colour=(117,0,234), back_colour=(236,214,0))
            for i in range(5):
                data = s.readline().decode('UTF-8').rstrip()
                if data=='CF':                                                                           #Coin Flipper
                    sense.show_message('F.C.', text_colour=(117,0,234), back_colour=(236,214,0))
                    data = s.readline().decode('UTF-8').rstrip()
                    if data=='F':
                        lights = [
                            O, O, O, O, O, O, O, O,
                            O, O, X, X, O, X, X, O,
                            O, O, X, X, O, X, X, O,
                            O, O, O, O, O, O, O, O,
                            X, O, O, O, O, O, O, X,
                            X, X, X, X, X, X, X, X,
                            X, X, X, X, X, X, X, X,
                            O, O, X, X, X, X, X, O
                            ]
                        
                    else:
                        lights = [
                            X, X, O, O, O, O, X, X,
                            X, X, O, O, O, O, X, X,
                            X, X, O, X, X, O, X, X,
                            X, X, O, X, X, O, X, X,
                            X, X, O, X, X, O, X, X,
                            X, X, O, X, X, O, X, X,
                            X, X, X, X, X, X, X, X,
                            X, X, X, X, X, X, X, X
                            ]
                        
                    sense.set_pixels(lights)
                elif data=='RPS':                                                                                  #ROCK,PAPER OR SCISSORS                                         
                    #sense.show_message('ROCK,PAPER OR SCISSORS', text_colour=(0,0,0), back_colour=(236,214,0))
                    data = s.readline().decode('UTF-8').rstrip()
                    if data=='R':              
                        lights = [
                            O, O, O, O, O, O, O, O,
                            O, O, O, O, O, O, O, O,
                            O, O, X, X, X, X, O, O,
                            O, O, X, X, X, X, O, O,
                            O, O, X, X, X, X, O, O,
                            O, O, X, X, X, X, O, O,
                            O, O, O, O, O, O, O, O,
                            O, O, O, O, O, O, O, O
                            ]
                    elif data=='P':     
                        lights = [
                            X, X, X, X, X, X, X, X,
                            X, X, X, X, X, X, X, X,
                            X, X, O, O, O, O, X, X,
                            X, X, O, O, O, O, X, X,
                            X, X, O, O, O, O, X, X,
                            X, X, O, O, O, O, X, X,
                            X, X, X, X, X, X, X, X,
                            X, X, X, X, X, X, X, X
                            ]
                    else:
                                        
                        lights = [
                            X, X, X, O, O, O, X, X,
                            X, O, X, O, O, X, X, O,
                            X, X, X, O, X, X, O, O,
                            O, O, O, X, X, O, O, O,
                            O, O, O, X, X, O, O, O,
                            X, X, X, O, X, X, O, O,
                            X, O, X, O, O, X, X, O,
                            X, X, X, O, O, O, X, X
                            ]
                    sense.set_pixels(lights)
        else:                                                                                   #Phrase
            for i in range(len(frase)):
                if i == (len(frase)-1):
                    print(frase[i])
                else:
                    print(frase[i],end='')
            for i in range(len(frase)):
                sense.show_message(frase[i], text_colour=(0,0,255), back_colour=(0,0,0))

        frase=[]
        
    






        
