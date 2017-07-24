from sense_hat import SenseHat

sense = SenseHat()

#cores

b=[0, 0, 255]
g=[0, 255, 0]

#imagem

image = [
    b,b,b,b,g,g,g,g,
    b,b,b,b,g,g,g,g,
    g,g,g,b,g,g,g,g,
    g,g,g,b,g,g,g,g,
    b,b,b,b,g,g,g,g,
    b,b,b,b,g,g,g,g,
    b,g,g,b,g,g,g,g,
    b,g,g,b,g,g,g,g,
    ]

sense.set_pixels(image)
    

while True:
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    z = sense.get_accelerometer_raw()['z']

    x = round(x, 0)
    y = round(y, 0)

    if y == -1:
        sense.set_rotation(180)
    elif x == -1:
        sense.set_rotation(90)
    elif x == 1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)
