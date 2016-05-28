from sense_hat import SenseHat
sense = SenseHat()
import sys
from additem import add_clothe
from chooseitem import choose_clothe
print ("Hello!")


t = sense.get_temperature()
h = sense.get_humidity ()

Question=raw_input("Choose Clothes/Add Clothes?")
if Question=="choose":
        choose_clothe(h,t)

                
                
elif Question=="add":
        add_clothe()

print ("Bye Bye!")

    





