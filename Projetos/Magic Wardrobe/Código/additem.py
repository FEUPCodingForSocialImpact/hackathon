import sys
def add_clothe():

    nr=6
    while nr>5:
        number=raw_input("How many piece of clothe you want to add?")
        if number=="1":
            nr=1
            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            
            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()


        if number=="2":
            nr=2
            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()


        if number=="3":
            nr=3
            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()


        if number=="4":
            nr=4
            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()


        if number=="5":
            nr=5
            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()

            cl=3
            while cl>2:
                clothes=raw_input("What piece of clothe is it?:")
                if clothes=="body": 
                    cl=0
                elif clothes=="legs":
                    cl=2
                elif clothes=="shoes":
                    cl=1
                else:
                    cl=3
            


            ff=3
            while ff>2:
                formal=raw_input("Formality?:")
                if formal=="casual": 
                    ff=0
                elif formal=="formal":
                    ff=2
                elif formal=="sportive":
                    ff=1
                else:
                    ff=3
                
            cc=6
            while cc>5:
                colour=raw_input("Colour?:")
                if colour=="white":
                    cc=1
                elif colour=="red":
                    cc=2
                elif colour=="green":
                    cc=3
                elif colour=="blue":
                    cc=4
                elif colour=="black":
                    cc=5
                else:
                    cc=6


            co=4
            while co>3:
                condition=raw_input("What temperature is the piece of clothe for?:")

                if condition=="very cold":
                    co=0
                elif condition=="cold":
                    co=1

                elif condition=="warm":
                    co=2
                
                elif condition=="hot":
                    co=3

                else:
                    co=4

            wt=2
            while wt>1:
                weather=raw_input("What's the weather that the clothe is for?:")

                if weather=="rainy":
                    wt=0

                elif weather=="sunny":
                    wt=1

                else:
                    wt=2
                    

            all=str(co)+ " " + str(wt)+ " " +str(cc) + " "+  str(ff)+ " " + str(cl)


            if (co==0 and wt==0):
            
                f = open("/home/pi/Desktop/Met_0_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==0 and wt==1):
            
                f = open("/home/pi/Desktop/Met_0_1","a")
                f.write(all+"\n" )
                f.close()


            if (co==1 and wt==0):
            
                f = open("/home/pi/Desktop/Met_1_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==1 and wt==1):
            
                f = open("/home/pi/Desktop/Met_1_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==0):
            
                f = open("/home/pi/Desktop/Met_2_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==2 and wt==1):
            
                f = open("/home/pi/Desktop/Met_2_1","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==0):
            
                f = open("/home/pi/Desktop/Met_3_0","a")
                f.write(all+"\n" )
                f.close()

            if (co==3 and wt==1):
            
                f = open("/home/pi/Desktop/Met_3_1","a")    
                f.write(all+"\n" )
                f.close()

            


            print all
            f = open("/home/pi/Desktop/my_clothes.txt","a")
            f.write(all+"\n" )
            f.close()


        elif number>"5":
            nr=6
            print("You can only add up to 5 new pieces.")



