# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:25:22 2020

@author: ALEXIS20012
"""
import random
def decifrado():
    c=int(input("ingrese el codigo cifrado:"))
    j=int(input("ingrese la contraseña privada:"))
    n=int(input("ingrese el primer digito de la contraseña publica:"))
    o=pow(c,j)
    i=o/n
    y=int(i)
    y=y*n
    a=o-y
    print("el numero es:",a)
def cifrado(f):
    nom=str(input("ingrese su nombre:"))
    p=int(input("ingrese el primer valor P:"))
    q=int(input("ingrese un valor Q:"))
    n=p*q
    e=(p-1)*(q-1)
    tm=3
    while tm<e:
        pt=random.randrange(3,e,2)
        tmp=e/pt
        tmp2=int(tmp)
        tmp=tmp-tmp2
        if (tmp==0) :
            pass
        else :
            break
    print("la clave publica es ("+str(n)+","+str(pt)+")")
    t=e
    while(t>0):
        t=random.randrange(e,e+100,1)
        tmp=t/pt
        tmp1=int(tmp)
        tm=tmp-tmp1
        print("")
        if(tm>0):
            print("la contraseña privada es:"+str(t))
            break
    a=int(input("ingrese un numero a codificar:"))
    o=float("{:.01}".format((pow(a,pt))/n))
    
    i=int(o)
    c=float((o-i)*n)
    print(c)
    c=round(c)
    print(c)
    texto=("nombre: "+nom+" contraseña publica:("+str(n)+","+str(pt)+")"+" la contraseña privada es:"+str(t)+" el codigo es:"+str(c)+"\n")
    f.write(texto)
    f.close()
menu=1
while(menu>0):
    m=int(input("1.desea generar un codigo \n2.desifrar el codigo \n3.borrar una archivo\n4.sair\n"))
            
            
    if(m==1):
        m=int(input("1.desea modificar el archivo\n2.leer los archivo"))   
        if(m==1):
            f=open("cifrado.txt","a")
            cifrado(f)  
        else:
            f=open("cifrado.txt","r")
            print(f.read())
            f.close()
                
                    
    elif(m==2):
        decifrado()
    elif(m==3):
        f=open("cifrado.txt","w")
    elif(m==4):
        men=str(input("desea salir\n[si]\t[no]"))
        if(men=="si"):
            menu=0
        else:
            pass
    else:
        print("error")
           