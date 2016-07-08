import time


def ligar_renov():
    seconds=0
    time_start = time.time()
    while True:
        if seconds < 5:
            print (seconds)
            time.sleep(1)
            print (" segundos \n")
            time.sleep(1)
            seconds = time.time() - time_start
        else:
            print ("Ligar a renovação!")
            break


ligar_renov()
