from sense_hat import SenseHat

sense = SenseHat()
sense.clear()




t = sense.get_temperature_from_humidity()
t = round(t, 1)
msg = "Temperature " + str(t)
    
    
# se temperatura >20 rgb[255, 0, 0]
# se temperatura < 20 rgb[0, 255, 0]
# se temperatura <0 rgb[0, 0, 255]

    
if t > 15:
    sense.show_message(msg, scroll_speed = 0.1, text_colour= [255,0, 0])
    
if t < 15:
    sense.show_message(msg, scroll_speed = 0.1, text_colour= [0, 0, 255])

