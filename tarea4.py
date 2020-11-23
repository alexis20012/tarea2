# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:17:00 2020

@author: ALEXIS20012
"""
import random
def estados(d):
    estadot=d.upper()
    __estadosr=["AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR","CAMPECHE","CHIAPAS","CHIHUAHUA","CIUDAD DE MEXICO",
             "COAHUILA","COLIMA","DURANDO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO","MEXICO","MICHOACAN"
             ,"MORELOS","NAYARIT","NUEVO LEON","OAXACA","PUEBLA","QUERETARO","QUINTANA ROO","SAN LUIS POTOSI"
             ,"SINALOA","SONORA","TABASCO","TAMAULIPAS","TLAXCALA","VERACRUZ","YUCATAN","ZAPATECAS"]
    __estadoa=["AG","BC","BS","CM","CS","CH","DF","CO","CL","DG","GT","GR","HG","JC","MC","MI","MO","NA",
               "NL","OA","PU","QT","QR","SL","SI","SO","TB","TM","TL","VE","YU","ZA"]
    for tmp in range(0,33,1):
        if (tmp==32):
            return "error no se encontro ese estado:"
        if(__estadosr[tmp]==estadot):
            return __estadoa[tmp]
            break
def consonante(datos):
    consola=["B","C","D","F","G","H","J","K","L","M","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
    long=len(datos)
    for tmp in range (1,long,1):
        for tpm in range (0,len(consola),1):
            if (datos[tmp]==" "):
                break 
                break
            if(datos[tmp]==consola[tpm]):
                return consola[tpm]
                break
                break
def fecha(d):
    mes=d.upper()
   #filtro de el mes
    meses=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
    for tmp in range(0,12,1):
        if(meses[tmp]==mes or str(tmp)==mes):
            mes=str(tmp)
            break     
    return mes
def vocales(f):
    vocal=["A","E","I","O","U"]
    for tmp in range(1,len(apellido1),1):
        for tpm in range(0,len(vocal),1):
            if(f[tmp]==vocal[tpm]):
                va=apellido1[tmp]
                return va
                break
                break 
            
apellido1=(str(input("ingrese su primer apellido:"))).upper()
extra=(str(input("en caso de que tu segundo apellido tenga, ""de la"",colocalo aqui, de lo contrario solo da enter:"))).upper()
apellido2=(str(input("ingrese su segundo apellido:"))).upper()
nombre=(str(input("ingrese su nombre:"))).upper()
sexo=(str(input("ingrese\nH/MASCULINO\nM/FEMENINO \n"))).upper()
dia = str(input("ingrese el dia de nacimiento:"))
mes=str(input("ingrese el mes de nacimiento:"))
fecha(mes)
anno=str(input("ingrese el año de nacimiento:")) 
estadoe=str(input("ingrese su estado:"))
estados(estadoe)
log=len(apellido1)
pt=str(random.randrange(0,100,1))
print(nombre,apellido1,extra,apellido2)
print("El CURP es:"+apellido1[0]+vocales(apellido1)+apellido2[0]+nombre[0]+anno[2:4]+fecha(mes)+dia+sexo+estados(estadoe)+consonante(apellido1)+consonante(apellido2)+consonante(nombre)+pt)