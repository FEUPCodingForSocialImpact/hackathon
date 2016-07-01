#!/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("localhost", "utilizador1", "1234", "iPantry")
curs=db.cursor()

def add():
    alimento = raw_input("Insira o nome do alimento a adicionar: \n")
    quant = input("Insira a quantidade a adicionar: \n")
    with db:
        curs.execute("""SELECT count(nome) FROM despensa WHERE nome=%s """, (alimento))        
        a = curs.fetchone()
        if a == (1L,):
            curs.execute("""UPDATE despensa SET quantidade = quantidade + %s WHERE nome = %s """, (quant,alimento))
        else:
            curs.execute("""INSERT INTO despensa (nome,quantidade,prioridade)
                            VALUES (%s,%s,0)""",(alimento,quant))
            cat = raw_input("Em que categoria se insere este produto? \n")
            curs.execute("""UPDATE despensa SET categoria = %s WHERE nome =  %s""",(cat,alimento))


def remove():
    alimento = raw_input("Insira o nome do alimento a remover: \n")
    quant = input("Insira a quantidade a remover: \n")
    with db:
        curs.execute("""SELECT count(despensa.nome) FROM despensa WHERE despensa.nome=%s """, (alimento))        
        a = curs.fetchone()        
        if a == (1L,):
            curs.execute("""UPDATE despensa SET despensa.quantidade = despensa.quantidade - %s WHERE despensa.nome = %s """, (quant,alimento))
            curs.execute("""SELECT quantidade FROM despensa WHERE despensa.nome=%s """, (alimento))
            a = curs.fetchone()            
            if a<(0L,):curs.execute("""UPDATE despensa SET despensa.quantidade = 0 WHERE despensa.nome = %s """, (alimento))
        else:
            print "O produto",(alimento),"nao existe na base de dados"

def delete():
     alimento = raw_input("Insira o nome do alimento a eliminar: \n")   
     with db:
       curs.execute("""SELECT count(despensa.nome) FROM despensa WHERE despensa.nome=%s """, (alimento))
       a = curs.fetchone()

       if a == (1L,):
           curs.execute("DELETE FROM despensa WHERE nome=%s",(alimento))
           print (alimento),"foi eliminado da base de bados com sucesso"
       else: print (alimento),"nao existe na base de dados"


def show():
    cat = raw_input("Que categoria pretende visualizar? \n")
    with db:
        curs.execute("""SELECT nome,quantidade FROM despensa WHERE categoria = %s""",(cat))
        lista=curs.fetchall()
        print("")
        for reading in lista:
            print str(reading[0])+"    "+str(reading[1])



def showmissing():
    with db:
        curs.execute("""SELECT nome FROM despensa WHERE quantidade = 0""")
        lista=curs.fetchall()
        print("")
        for reading in lista:
            print str(reading[0])

def showall():
    with db:
        curs.execute("""SELECT nome,quantidade FROM despensa""")
        lista=curs.fetchall()
        print("")
        for reading in lista:
            print str(reading[0])+"    "+str(reading[1])

def priority():
    print("Indique o nome do produto a alternar a 'prioridade': \n")
    alimento = raw_input()
    with db:
        curs.execute("""SELECT prioridade FROM despensa WHERE despensa.nome=%s """, (alimento))        
        a = curs.fetchone()
        if a == (1L,):
            curs.execute("""UPDATE despensa SET prioridade = 0 WHERE despensa.nome = %s """, (alimento))
        else:
            curs.execute("""UPDATE despensa SET prioridade = 1 WHERE nome =  %s""",(alimento))

def showpriority():
    with db:
        curs.execute("""SELECT nome,quantidade FROM despensa WHERE prioridade = 1""")
        lista=curs.fetchall()
        print("")
        for reading in lista:
            print str(reading[0])+"    "+str(reading[1])

def changecat():
    alimento = raw_input("Insira o nome do alimento a mudar de categoria: \n")
    cat = raw_input("Insira o nome da nova categoria em que este produto se ira integrar:\n")
    with db:
        curs.execute("""UPDATE despensa SET categoria = %s WHERE nome =  %s""",(cat, alimento))


print "Bem vindo ao iPantry!"
while 1<2:
    print("")
    com = raw_input("Que acao quer fazer? \n")
    if com == "ADD":
        add()
    elif com == "REMOVE":
        remove()
    elif com == "DELETE":
        delete()
    elif com == "SHOW":
        show()
    elif com == "SHOWMISSING":
        showmissing()
    elif com == "SHOWALL":
        showall()
    elif com == "PRIORITY":
        priority()
    elif com == "SHOWPRIORITY":
        showpriority()
    elif com == "CHANGECATHEGORY":
        changecat()
    elif com == "CREDITS":
        print ("iPantry alpha 1.0.2 desenvolvido por:\nEduardo Teixeira, Joao Lucas Silva Martins, Pinto Rui, Tiago Duarte da Silva")
    elif com == "HELP":
        print ("Comandos disponiveis:")
        print ("ADD, CHANGECATHEGORY, CREDITS,  HELP, PRIORITY, REMOVE, SHOW, SHOWALL, SHOWMISSING, SHOWPRIORITY")
    else:
        print ("Comando invalido")
        
