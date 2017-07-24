from sense_hat import SenseHat
sense=SenseHat()

#pressão
r = [255,0,0]
w = [255,255,255]
b = [0,0,255]
n = [0, 0, 0]

# Menor que 1014 é r, de 1014 a 1017 é b e maior do que 1017 é w.

image3 = [
n,n,n,n,r,r,r,r,
n,n,n,n,r,b,b,r,
w,n,n,n,r,r,r,r,
n,w,n,n,r,r,b,b,
n,n,w,n,r,b,b,b,
n,n,n,n,b,b,b,b,
n,w,w,n,b,b,b,b,
n,w,w,n,r,r,r,r,
]

#humidade
b = [0,0,255]
l = [51,255,255]
g = [0,255,0]
n = [0,0,0]

#até 70 g, até 80 l, acima de 80 b
image2 = [
n,n,n,n,g,b,l,g,
n,n,n,n,l,b,b,g,
b,n,n,n,l,l,g,g,
n,b,n,n,l,l,g,g,
n,n,b,n,g,l,b,b,
n,n,n,n,l,l,b,b,
n,g,g,n,b,b,b,b,
n,g,g,n,g,g,g,g
]

#temperatura
r = [255,0,0]
y = [255,255,0]
b = [0,0,255]
n = [0,0,0]

#até 25 azul,acima de 25 amarelo, acima de 30 vermelho
image1 = [
n,n,n,n,b,b,y,r,
n,n,n,n,b,y,y,y,
y,n,n,n,b,b,r,r,
n,b,n,n,y,y,r,r,
n,n,b,n,b,r,r,r,
n,n,n,n,y,r,r,r,
n,b,b,n,b,r,r,r,
n,b,b,n,r,r,r,r
]

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'up':
            sense.set_pixels(image1)
        elif event.action == 'pressed' and event.direction == 'left':
            sense.set_pixels(image2)
        elif event.action == 'pressed' and event.direction == 'right':
            sense.set_pixels(image3)
        
