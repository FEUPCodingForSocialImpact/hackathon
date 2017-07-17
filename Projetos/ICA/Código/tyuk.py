from sense_hat import SenseHat
from time import sleep
from guizero import App,Text
from guizero import ButtonGroup
from guizero import PushButton, info

def gyroscope():

        global a,b
        sense.set_pixel(a, b, (255, 255, 255))
        sleep(0.01)
        sense.set_pixel(a, b, (0, 0, 255))
        x = sense.get_accelerometer_raw()['x']
        y = sense.get_accelerometer_raw()['y']
        x = round(x, 0)
        y = round(y, 0)
       
        if y == 1 and b > 0:
            sense.set_pixel(a, b, (0, 0, 0))
            b -= 1
            sense.set_pixel(a,b,(0, 0, 255))
        elif y == -1 and b < 7:
            sense.set_pixel(a, b, (0, 0, 0))
            b += 1
            sense.set_pixel(a,b,(0, 0, 255))
        
        elif x ==-1 and a < 7:
            sense.set_pixel(a, b, (0, 0, 0))
            a += 1
            sense.set_pixel(a,b,(0, 0, 255))
        
        elif x == 1 and a > 0:
            sense.set_pixel(a, b, (0, 0, 0))
            a -= 1
            sense.set_pixel(a,b,(0, 0, 255))


def mexer():

    print("Mexer")
 

    x_max = False
    x_min = False       

    while x_max== False or x_min == False:
         w= [100, 100, 100]
         r= [255, 0, 1]
        
         setas_horizontal=[w,w,w,w,w,r,w,w,
                           w,w,w,w,w,w,r,w,
                           r,r,r,r,r,r,r,r,
                           w,w,r,w,w,w,r,w,
                           w,r,w,w,w,r,w,w,
                           r,r,r,r,r,r,r,r,
                           w,r,w,w,w,w,w,w,
                           w,w,r,w,w,w,w,w]
        

         sense.set_pixels(setas_horizontal)
        
        
         acceleration = sense.get_accelerometer_raw()
         x = acceleration['x']
         y = acceleration['y']
         z = acceleration['z']

         x=round(x, 0)
         y=round(y, 0)
         z=round(z, 0)
         print("x={0}, y={1}, z={2}".format(x, y, z))
               
         if x>2:
              x_max= True
         elif x<0:
             x_min = True
        
def amassar():
    sense.clear()
    print("Amassar")    
    y_max = False
    y_min = False
   
        

    while y_max== False or y_min == False:
        w= [100, 100, 100]
        r= [255, 0, 1]
        
        
        setas_verticais=[w,w,r,w,w,r,w,w,
                         w,r,r,r,w,r,w,w,
                         r,w,r,w,r,r,w,w,
                         w,w,r,w,w,r,w,w,
                         w,w,r,w,w,r,w,w,
                         w,w,r,r,w,r,w,r,
                         w,w,r,w,r,r,r,w,
                         w,w,r,w,w,r,w,w]
    
        sense.set_pixels(setas_verticais)
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)

        print("x={0}, y={1}, z={2}".format(x, y, z))
       
        if y>2:
            y_max= True
        elif y<0:
            y_min = True
            
def picar():
    sense.clear() 
    print("Picar")
    z_max = False
    z_min = False
   


    while z_max== False or z_min == False:
        w= [100, 100, 100]
        t= [176, 89, 51]
        setas_up_down=[w,w,t,w,w,t,w,w,
                       w,t,t,t,w,t,w,w,
                       t,w,t,w,t,t,w,w,
                       w,w,t,w,w,t,w,w,
                       w,w,t,w,w,t,w,w,
                       w,w,t,t,w,t,w,t,
                       w,w,t,w,t,t,t,w,
                       w,w,t,w,w,t,w,w]
        
        sense.set_pixels(setas_up_down)
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)

        print("x={0}, y={1}, z={2}".format(x, y, z))
        if z>2:
            z_max= True
        elif z<0:
             z_min = True





def game():
    global a, b, receita_escolhida, sense, colours, preparacao
    sense = SenseHat()
    sense.clear()
    a=0
    b=0
    sense.set_rotation(180)
    sense.set_pixel(6,3, ( 255, 17, 145))
    colours = {}

    colours["amarelo"] = (218, 165, 32) 
    colours["branco"] = (255, 255, 255)
    colours["azul"] = (0, 0, 255)
    colours["rosa"] = (255, 20, 147)
    colours["vermelho"] = (255, 0, 0)
    colours["castanho"] = (139, 69, 19)
    colours["roxo"] = (138, 43, 226)
    colours["verde"] = (34, 139, 34)
    colours["violeta"] =(147, 112, 219)
    colours["azulclaro"] = (0, 255, 255)
    colours["azulesc"] = (25, 25, 112)
    colours["cinza"] = (139, 137, 137)
    colours["laranja"] = (255, 69, 0)
    e = (0, 0, 0)  

    for i in range(11):
        sense.set_pixel(ingredientes[i][2], ingredientes[i][3], colours[ingredientes[i][1]])

    """print("1. Bacalhau à Brás")
    print("2. Bolo de Chocolate")
    print("3. Perinhas de Bacalhau")
    print("4. Carne Estufada com Batatas")
    user_input = input("Escolhe a tua receita:")
    print(user_input)

    if user_input == "1":
        print(receita_1)
        receita_escolhida = receita_1
        #mov_escolhido = mov_1
    if user_input == "2":
        print(receita_2)
        receita_escolhida = receita_2
        #mov_escolhido = mov_2
    if user_input == "3":
        print(receita_3)
        receita_escolhida = receita_3
        #mov_escolhido = mov_3
    if user_input == "4":
        print(receita_4)
        receita_escolhida = receita_4
        #mov_escolhido = mov_4"""

    #print([ingredient for ingredient in ingredientes if (1 == ingredient[2] and 5 == ingredient[3])])
 
    ingredientes_temp = ingredientes[:]
    escolhida_temp = receita_escolhida[:]


    while True:
        gyroscope ()
        sleep(0.05)
        if len([ingredient for ingredient in ingredientes_temp if (a == ingredient[2] and b == ingredient[3  ])]) >= 1:
            #print("receita escolhida ",receita_escolhida)
            #print("igredientes todos ", ingredientes_temp)
            if len([ingredient for ingredient in receita_escolhida if (a == ingredient[2] and b == ingredient[3])]) == 0:
                sense.set_pixel(a, b, (0, 0, 0))
                ingredientes_temp.remove([ingredient for ingredient in ingredientes_temp if (a == ingredient[2] and b == ingredient[3])][0])
                a=0
                b=0
                sleep(0.01)
                #print("ingredientes final ", ingredientes_temp, "\n")
            elif len([ingredient for ingredient in escolhida_temp if (a == ingredient[2] and b == ingredient[3])]) >=1 :
                escolhida_temp.remove([ingredient for ingredient in ingredientes_temp if (a == ingredient[2] and b == ingredient[3])][0])
                if len(escolhida_temp) == 0:
                    sense.clear()
                    a=0
                    b=0
                    break
    #Preparação
    for i in range(len(preparacao)):
        if preparacao[i] == "M":
            mexer()
        elif preparacao[i] == "F":
             forno()
        elif preparacao[i] == "A":
             amassar()
        elif preparacao[i] == "P":
             picar()




def escolha_receita():
    global receita_1, receita_2, receita_3, receita_4, receita_escolhida, receita_decisao, preparacao
    print("entrei")
    s = ""
    if receita_decisao.get() == "A":
        receita_escolhida = receita_1
        preparacao = preparacao_1
        for a in range(len(receita_1)):
            s += receita_1[a][0]
            s += " - "
            s += receita_1[a][1]
            s += " \n"
    elif receita_decisao.get() == "B":
        receita_escolhida = receita_2
        preparacao = preparacao_2
        for b in range(len(receita_2)):
            s += receita_2[b][0]
            s += " - "
            s += receita_2[b][1]
            s += " \n"
    elif receita_decisao.get() == "C":
        receita_escolhida = receita_3
        preparacao = preparacao_3
        for c in range(len(receita_3)):
            s += receita_3[c][0]
            s += " - "
            s += receita_3[c][1]
            s += " \n"
    elif receita_decisao.get() == "D":
        receita_escolhida = receita_4
        preparacao = preparacao_4
        for d in range(len(receita_4)):
            s += receita_4[d][0]
            s += " - "
            s += receita_4[d][1]
            s += " \n"
    info("Receita Escolhida", s )
    game()
    sense.clear()
    sense.show_message(" WE DID IT!!! ")
    

def forno():
 
    sense.show_letter("F",text_colour=[51, 153, 255])
    sleep(1)
    sense.show_letter("O",text_colour=[51, 153, 255])
    sleep(1)
    sense.show_letter("R",text_colour=[51, 153, 255])
    sleep(1)
    sense.show_letter("N",text_colour=[51, 153, 255])
    sleep(1)
    sense.show_letter("O", text_colour=[51, 153, 255])
    sleep(1)

    sense.clear()
    

ingredientes = [["carne", "azul", 1, 5], ["bacalhau", "rosa", 3, 7], ["azeite", "amarelo", 4,0], ["cebola", "verde", 0, 1], ["ovos", "azulesc", 7, 3],["farinha", "cinza", 2, 2], ["sal", "azulclaro", 5, 0],["tomate", "vermelho", 2, 1],["chocolate", "castanho", 4, 4],["açúcar", "roxo", 5, 6], ["batata", "laranja", 5, 2]] 

#Receita_1
receita_1 = [ingredientes[4], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[6], ingredientes[10]]

#Receita_2
receita_2 = [ingredientes[4], ingredientes[5], ingredientes[8], ingredientes[9]]

#Receita_3
receita_3 = [ingredientes[1], ingredientes[10], ingredientes[4], ingredientes[2], ingredientes[3], ingredientes[7]]

#Receita_4
receita_4 = [ingredientes[0], ingredientes[2], ingredientes[3], ingredientes[6], ingredientes[7], ingredientes[10]]

Bacalhau_a_Bras = ["Bacalhau à Brás", receita_1]
Bolo_de_Chocolate = ["Bolo de Chocolate", receita_2]
Perinhas_de_Bacalhau = ["Perinhas de Bacalhau", receita_3]
Carne_Estufada = ["Carne Estufada com Batatas", receita_4]

preparacao_1 = ["P", "M", "F", "M", "P", "M"]
preparacao_2 = ["M", "M", "F", "A", "P"]
preparacao_3 = ["A", "F", "P", "P", "M"]
preparacao_4 = ["P", "M", "F", "P", "A"]

app = App("ICA")
welcome_message = Text(app, text="Escolhe uma Receita:", size=40, font="Times New Roman", color="Black")  
receita_decisao = ButtonGroup(app, options=[ ["Bacalhau à Brás", "A"], ["Bolo de Chocolate", "B"],["Perinhas de Bacalhau", "C"], ["Carne Estufada com Batatas", "D"] ],selected="A", horizontal=False, grid=[2,1], align="left")
decisao_escolha = PushButton(app, command=escolha_receita, text="Próximo", grid=[3,1], align="left")
app.display()













