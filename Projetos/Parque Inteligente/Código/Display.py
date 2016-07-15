from sense_hat import SenseHat

import time

sense = SenseHat()

sense.clear()

from random import randint

sense.set_rotation(180)
a = randint(0,100)/100
b = randint(0,100)/100
c = randint(0,100)/100
d = randint(0,100)/100
e = randint(0,100)/100
f = randint(0,100)/100
g = randint(0,100)/100

h = randint(0,100)/100
i = randint(0,100)/100
j = randint(0,100)/100
ax = randint(0,7)
ay = randint(0,7)
bx = randint(0,7)
by = randint(0,7)
cx = randint(0,7)
cy = randint(0,7)
dx = randint(0,7)
dy = randint(0,7)
ex = randint(0,7)
ey = randint(0,7)
fx = randint(0,7)
fy = randint(0,7)
gx = randint(0,7)
gy = randint(0,7)
hx = randint(0,7)
hy = randint(0,7)
ix = randint(0,7)
iy = randint(0,7)
jx = randint(0,7)
jy = randint(0,7)
timerandom = 0

while timerandom < 16:
    if a < 1:
        aR = round(255 * (1-a))
        aG = round(255 * a)
        sense.set_pixel(ax, ay, [aR, aG, 0])
        a = a + 0.05
    if b < 1:
        bR = round(255 * (1-b))
        bG = round(255 * b)
        sense.set_pixel(bx, by, [bR, bG, 0])
        b = b + 0.05
    if c < 1:
        cR = round(255 * (1-c))
        cG = round(255 * c)
        sense.set_pixel(cx, cy, [cR, cG, 0])
        c = c + 0.05
    if d < 1:
        dR = round(255 * (1-d))
        dG = round(255 * d)
        sense.set_pixel(dx, dy, [dR, dG, 0])
        d = d + 0.05
    if e < 1:
        eR = round(255 * (1-e))
        eG = round(255 * e)
        sense.set_pixel(ex, ey, [eR, eG, 0])
        e = e + 0.05
    if f < 1:
        fR = round(255 * (1-f))
        fG = round(255 * f)
        sense.set_pixel(fx, fy, [fR, fG, 0])
        f = f + 0.05
    if g < 1:
        gR = round(255 * (1-g))
        gG = round(255 * g)
        sense.set_pixel(gx, gy, [gR, gG, 0])
        g = g + 0.05
    if h < 1:
        hR = round(255 * (1-h))
        hG = round(255 * h)
        sense.set_pixel(hx, hy, [hR, hG, 0])
        h = h + 0.05
    if i < 1:
        iR = round(255 * (1-i))
        iG = round(255 * i)
        sense.set_pixel(ix, iy, [iR, iG, 0])
        i = i + 0.05
    if j < 1:
        jR = round(255 * (1-j))
        jG = round(255 * j)
        sense.set_pixel(jx, jy, [jR, jG, 0])
        j = j + 0.05
    time.sleep(0.6)
    timerandom = timerandom + 1
