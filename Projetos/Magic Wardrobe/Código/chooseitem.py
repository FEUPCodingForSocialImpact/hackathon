
def choose_clothe(h,t):
        
    if h<100 and t>=0.0 and t< 10.0:
        f=open("/home/pi/Desktop/Met_0_1")
        lines=f.readlines()
        print ("Weather is Very Cold and there isn't rain.")
        for line in lines:
               elemArray = line.split(' ')
               print elemArray[0]
               print elemArray[1]
               print elemArray[2]
               print elemArray[3]
               print elemArray[4]
               print elemArray[5]
               print elemArray[6]

    if h>=100 and t>=0.0 and t<10.0:
        f=open("/home/pi/Desktop/Met_0_0")
        lines=f.readlines()
        print ("Weather is Very Cold and there is rain.")

        for line in lines:
            elemArray = line.split(' ')
            print elemArray[0]
            print elemArray[1]
            print elemArray[2]
            print elemArray[3]
            print elemArray[4]
            print elemArray[5]
            print elemArray[6]

    if h<100 and t>=10.0 and t<15.0:
        f=open("/home/pi/Desktop/Met_1_1")
        lines=f.readlines()
        print ("Weather is Cold and there isn't rain.")

        for line in lines:
             elemArray = line.split(' ')
             print elemArray[0]
             print elemArray[1]
             print elemArray[2]
             print elemArray[3]
             print elemArray[4]
             print elemArray[5]
             print elemArray[6]

                         

    if h>=100 and t>=10.0 and t<15.0:
        f=open("/home/pi/Desktop/Met_1_0")
        lines=f.readlines()
        print ("Weather is Cold and there is rain.")

        for line in lines:
             elemArray = line.split(' ')
             print elemArray[0]
             print elemArray[1]
             print elemArray[2]
             print elemArray[3]
             print elemArray[4]
             print elemArray[5]
             print elemArray[6]

    if h<100 and t>=15.0 and t<20.0:
        f=open("/home/pi/Desktop/Met_2_1")
        lines=f.readlines()
        print ("Weather is warm and there isn't rain.")

        for line in lines:
             elemArray = line.split(' ')
             print elemArray[0]              
             print elemArray[1]                
             print elemArray[2]                
             print elemArray[3]
             print elemArray[4]
             print elemArray[5]
             print elemArray[6]

    if h>=100 and t>=15.0 and t<20.0:
        f=open("/home/pi/Desktop/Met_2_0")
        lines=f.readlines()
        print ("Weather is warm and there is rain.")

        for line in lines:
                 elemArray = line.split(' ')
                 print elemArray[0]                
                 print elemArray[1]                 
                 print elemArray[2]                 
                 print elemArray[3]
                 print elemArray[4]
                 print elemArray[5]
                 print elemArray[6]


    if (h<100 and t>=20.0):
        f=open("/home/pi/Desktop/Met_3_1")
        
        lines=f.readlines()
        print ("Weather is hot and there isn't rain.")

        for line in lines:
             elemArray = line.split(' ')
             print elemArray[0]                 
             print elemArray[1]                
             print elemArray[2]                 
             print elemArray[3]
             print elemArray[4]
             print elemArray[5]
             print elemArray[6]

    if h>=100 and t>=20 and t<=45.0:
        f=open("/home/pi/Desktop/Met_3_0")
        lines=f.readlines()
        print ("Weather is very hot and there is rain.")

        for line in lines:
             elemArray = line.split(' ')
             print elemArray[0]                 
             print elemArray[1]                 
             print elemArray[2]                 
             print elemArray[3]
             print elemArray[4]
             print elemArray[5]
             print elemArray[6]
             
