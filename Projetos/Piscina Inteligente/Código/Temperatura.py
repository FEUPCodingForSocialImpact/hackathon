from sense_hat import SenseHat
sense = SenseHat()
while True:
    t = sense.get_temperature()
    
    
    t = round(t, 1)


    if t > 24 and t < 30:
        bg = [0, 0, 0]  # green
    elif t < 24:
        bg = [100, 0, 0]  # red
    else:
        bg = [159, 0, 255]
    

    
    msg = "Temperature = %s" % (t)

    sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
    print ("NECESSARIO AQUECER! FECHAR COBERTURA")



