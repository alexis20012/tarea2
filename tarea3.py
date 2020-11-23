# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:10:32 2020

@author: ALEXIS20012
"""
def nombrec():
    nombre=str(input("ingrese su nombre:")).upper()
    priapellido=str(input("ingrese su primer apellido:")).upper()
    segapellido=str(input("ingrese su segundo apellido:")).upper()
    
    dia = str(input("ingrese el dia de nacimiento:"))
    mes=str(input("ingrese el mes de nacimiento:"))
    anno=str(input("ingrese el año de nacimiento:")) 
   #filtro de el mes 
    meses=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
    for tmp in range(0,12,1):
        if(meses[tmp]==mes or str(tmp)==mes):
            mes=str[tmp]
            break

    
    print(nombre+" "+priapellido+" "+segapellido)
    print("con fecha "+str(dia)+"/"+str(mes)+"/"+str(anno))
    print("su RFC es:"+priapellido[0]+priapellido[1]+segapellido[0]+nombre[0],end="")    
    print(anno[2:4]+mes+dia)     
     
nombrec()

