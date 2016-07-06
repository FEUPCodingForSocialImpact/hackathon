import sys
from additem import add_clothe
from chooseitem import choose_clothe
print ("Hello!")

tt=2
while tt>1:
        t=raw_input("Set temperature:")
        t=int(t)
        if t>=0.0 and t<=45.0:
                h=raw_input("Set humidity:")
                tt=1
                h=int(h)
                

        else:
             tt=2 
             print("No clothes available for the weather.")
    
        
Question=raw_input("Choose Clothes/Add Clothes?")
if Question=="choose":
        choose_clothe(h,t)

                
                
elif Question=="add":
        add_clothe()

print ("Bye Bye!")

