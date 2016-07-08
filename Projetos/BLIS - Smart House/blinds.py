import time
from sense_hat import SenseHat
sense=SenseHat ()


#Colours
o = [255,127,0]
e = [0,0,0]

#Windows
  
  #0
zero = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #1
one = [
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]


    #2
two = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #3
three = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #4
four = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #5
five = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #6
six = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

    #7
seven = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
o,o,o,o,o,o,o,o
]

     #8
eight = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

#Settings


def blinds():
    while True:
        choice = int(input("Choose how closed you want the blinds to be from 0 to 8: "))
        if choice==0:
            sense.set_pixels(zero)
            break

        elif choice==1:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            break

        elif choice==2:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            break

        elif choice==3:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            break

        elif choice==4:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            break

        elif choice==5:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            break

        elif choice==6:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            time.sleep(1)
            sense.set_pixels(six)
            break

        elif choice==7:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            time.sleep(1)
            sense.set_pixels(six)
            time.sleep(1)
            sense.set_pixels(seven)
            break

        elif choice==8:
            sense.set_pixels(zero)
            time.sleep(1)
            sense.set_pixels(one)
            time.sleep(1)
            sense.set_pixels(two)
            time.sleep(1)
            sense.set_pixels(three)
            time.sleep(1)
            sense.set_pixels(four)
            time.sleep(1)
            sense.set_pixels(five)
            time.sleep(1)
            sense.set_pixels(six)
            time.sleep(1)
            sense.set_pixels(seven)
            time.sleep(1)
            sense.set_pixels(eight)
            break

        else:
            print("""Invalid Input

""")

#blinds()
